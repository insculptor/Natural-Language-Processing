from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings("ignore")

def send_email(strTo,email_list):
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
    s.starttls()
    # Authentication
    s.login("myzomatobot@gmail.com", "123abcd*")
    # sending the mail
    s.sendmail(strFrom, strTo, msgRoot.as_string())
    # terminating the session
    s.quit()