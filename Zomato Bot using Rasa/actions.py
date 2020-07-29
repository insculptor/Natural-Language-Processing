from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
import zomatopy
import json
import re
import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings("ignore")

# Defining Global variables:
# List of tier 1 and tier 2 cities
tier1_2_cities = ['agra', 'ahmedabad', 'ajmer', 'aligarh', 'allahabad', 'amravati', 'amritsar',
                  'asansol', 'aurangabad', 'bangalore', 'bareilly', 'belgaum', 'bhavnagar',
                  'bhiwadi', 'bhopal', 'bhubaneshwar', 'bijapur', 'bikaner', 'bokaro', 'chandigarh',
                  'chennai', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'dharwad', 'durg bhilai',
                  'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'goa', 'gorakhpur',
                  'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 'hyderabad', 'indore',
                  'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi',
                  'jodhpur', 'kakinada', 'kannur', 'kanpur', 'kochi', 'kolhapur', 'kolkata', 'kollam',
                  'kota', 'kottayam', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai',
                  'malappuram', 'mangalore', 'mathura', 'meerut', 'moradabad', 'mumbai',
                  'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'new delhi',
                  'noida', 'palakkad', 'patna', 'pune', 'raipur', 'rajahmundry', 'rajkot',
                  'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar',
                  'sultanpur', 'surat', 'thrissur', 'tirunelveli', 'tiruppur', 'trichy',
                  'trivandrum', 'ujjain', 'vadodara', 'varanasi', 'vijayawada', 'visakhapatnam','warangal']


# List of restaurants from the action_restaurant_search.
# The list was originally populated in action_restaurant_search as well as action_send_mail. 
# However, the action_send_mail was taking longer than 10sec many times thus resulting in a error due to rasa configuration setting.
# Thus, retrieving the list once and storing it globally for acces in action_send_mail due reduce the processing there. 
email_list = ""


def restaurant_details(city,cuisines,upper_budget=5000,lower_budget=50):
    '''
    This function will take the values of location, cuisine and budget range, 
    and will return a DataFrame Object that contains top 10 restaurants in 
    Descending order of rating in the location. 
    
    Parameters:
    location: Location sprecifid by the user.
    cuisines : Cuisine Specified by User.
    upper_budget: Maximum cost for two people, default value is 5000, if none specified.
    lower_budget: Minimum cost for two people, default value is 50, if none specified.
    '''
    #config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
    config={ "user_key":"2cd53b995b0818e559df301ec3b98a06"}
    zomato = zomatopy.initialize_app(config)
    loc = city#tracker.get_slot('location')
    cuisine = cuisines#tracker.get_slot('cuisine')
    location_detail=zomato.get_location(loc, 1)
    d1 = json.loads(location_detail)
    lat=d1["location_suggestions"][0]["latitude"]
    lon=d1["location_suggestions"][0]["longitude"]
    cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
    results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100)
    d = json.loads(results)
    df = json_normalize(d['restaurants'])
    rest= df[['restaurant.user_rating.aggregate_rating', 'restaurant.name','restaurant.location.city','restaurant.location.address','restaurant.average_cost_for_two']]
    rest.sort_values(['restaurant.user_rating.aggregate_rating', 'restaurant.average_cost_for_two'],ascending=False,inplace=True)
    rest['restaurant.location.city'] = rest['restaurant.location.city'].str.lower().str.strip()
    rest['restaurant.location.address'] = rest['restaurant.location.address'].str.strip()
    rest=rest[(rest['restaurant.average_cost_for_two']<=upper_budget) & (rest['restaurant.average_cost_for_two']>=lower_budget)& (rest['restaurant.location.city']== loc)]
    #rest=rest[(rest['restaurant.average_cost_for_two']<=upper_budget) & (rest['restaurant.average_cost_for_two']>=lower_budget)]

    rest= rest.astype(str)
    rest.reset_index(inplace=True)
    rest.drop(columns=['index'],inplace=True)
    return rest.head(10)


def get_restaurant_chat_details(rest):
    '''
    This function takes a DataFrame object (rest) which contains restaurant details
    and return a String that will be used to display restaurants found on the chatbot window.
    '''
    restaurants = rest.head(5)
    details = 'Found top restaurant with following details: \n'
    for i in restaurants.index:
        details = details+  str(restaurants.index.get_loc(i)+1)+'. '+restaurants['restaurant.name'][i]+' in '+restaurants['restaurant.location.address'][i] + ' has been rated '+restaurants['restaurant.user_rating.aggregate_rating'][i]+ '\n'
    return details


def get_list_for_email(rest):
    '''
    This function will take a data frame object containing the restaurant details 
    and will return a string in html tagged format, which will be used to send email to the user. 
    '''
    email_listitem=''
    for i in rest.index:
        email_listitem=email_listitem+ '<li><b>'+ rest['restaurant.name'][i]+'</b><br/>User Rating: '+rest['restaurant.user_rating.aggregate_rating'][i]+'<br/>Location: '+ rest['restaurant.location.address'][i]+'</b><br/>Cost for two: '+rest['restaurant.average_cost_for_two'][i]+'</li><br/>'
    return email_listitem


def send_email(strTo):
    '''
    This function will send an email to the specified users with list of top 10 restaurants
    in descending order of rating.
    
    The function accepts the below parameters:
    strTo : Email ID of the user
    '''
    global email_list

    # Define the paramaters for email
    strFrom = 'myzomatobot@gmail.com'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Your Nearby Restaurant Details'
    msgRoot['From'] = 'Zomato Bot'
    msgRoot['To'] = strTo
    msgRoot.preamble = 'Hello from Zomato!'
    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)
    # Read the image header for email
    fp = open('zomatoemaillheader.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)
    #email_list = get_list_for_email(rest)
    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<html><body><img src="cid:image1"><br/><p>Hello,<br/></p><p> Your nearby restaurant details are:</p><p><ol>'+email_list+'</ol></p><p>Bon Appetit!</p><p>Regards,<br/>Zomato Bot</p></body></html>', 'html')
    msgAlternative.attach(msgText)
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    try:
        s.starttls()
        # Authentication
        s.login("myzomatobot@gmail.com", "123abcd*")
        # sending the mail
        s.sendmail(strFrom, strTo, msgRoot.as_string())
        # terminating the session
        s.quit()
    except:
        return 0
    return 1


# Check if the city exists entered is either a tier1 or tier 2 city else utter error
class ActionCheckCity(Action):
    def name(self):
        return 'action_check_city'

    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('city')
        city = str(city)

        if city.lower() in tier1_2_cities:
            return [SlotSet('city_tier12',"true")]
        else:
            return [SlotSet('city_tier12',"false")]


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)

        city = tracker.get_slot('city')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')

        global email_list 
        email_list = ""

        if budget == 'low':
            upper_budget = 299
            lower_budget=10
        elif budget == 'medium':
            upper_budget = 700
            lower_budget=301
        elif budget == 'high':
            upper_budget = 10000
            lower_budget=701
        else:
            upper_budget = 10000
            lower_budget=10

        respdf= restaurant_details(city= city,cuisines=cuisine,upper_budget=upper_budget,lower_budget=lower_budget)
        
        if respdf['restaurant.name'].count() > 0:
            email_list = get_list_for_email(respdf)
            response = get_restaurant_chat_details(respdf)
            dispatcher.utter_message(response)
            return [SlotSet('noresults',"false")]
        else:
            #dispatcher.utter_message("Oops! Could not find results in that area!")
            return [SlotSet('noresults',"true")]


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        emailto= tracker.get_slot('email')
        val = send_email(strTo=emailto)

        if val==1:
            response= 'Email sent! Please check you mailbox.'
            dispatcher.utter_message(response)
            return [SlotSet('mail_sent',"true")]
        else:
            response = 'There was some error sending email. Please try later!'
            dispatcher.utter_message(response)
            return [SlotSet('mail_sent',"true")]
			
			
# Check if the email entered is either a valid email address
class ActionCheckEmail(Action):
    def name(self):
        return 'action_check_email'

    def run(self, dispatcher, tracker, domain):
        emailid = tracker.get_slot('email')
        # Make a regular expression 
        # for validating an Email 
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        
        try:
            if(re.search(regex,emailid)):
                return [SlotSet('email_validate',"true")]
            else:
                return [SlotSet('email_validate',"false")]
            dispatcher.utter_message("Oops! Could not validate the email!")
        except:
            return [SlotSet('email_validate',"false")] 
            dispatcher.utter_message("Oops! Could not validate the email!")


class ActionResetSlots(Action):
    def name(self):
        return 'action_reset'
	
    def run(self, dispatcher, tracker, domain):
        #AllSlotsReset()
        return [AllSlotsReset()]


class ActionRestarted(Action): 	
    def name(self): 		
        return 'action_restarted' 	

    def run(self, dispatcher, tracker, domain): 
        return[Restarted()]