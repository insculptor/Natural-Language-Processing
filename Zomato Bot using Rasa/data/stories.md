## only_restaurant
* greet
    - utter_greet
* restaurant_search
    - utter_ask_city
* restaurant_search{"city": "agra"}
    - slot{"city": "agra"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* choose{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"city": "agra"}
    - utter_ask_ifemail
* affirm
    - utter_askemail
* send_email{"email": "er.dr.rd@gmail.com"}
    - slot{"email": "er.dr.rd@gmail.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* affirm
    - utter_goodbye
    - action_reset
    - reset_slots

## restaurant_and_cuisine
* restaurant_search{"cuisine": "chinese", "city": "new delhi"}
    - slot{"city": "new delhi"}
    - slot{"cuisine": "chinese"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_budget
* choose{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"city": "new delhi"}
    - utter_ask_ifemail
* affirm
    - utter_askemail
* send_email{"email": "er.dr.rd@gmail.com"}
    - slot{"email": "er.dr.rd@gmail.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* affirm
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "city": "pune", "budget": "medium"}
    - slot{"budget": "medium"}
    - slot{"city": "pune"}
    - slot{"cuisine": "chinese"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* affirm
    - utter_askemail
* send_email{"email": "er.dr.rd@gmail.com"}
    - slot{"email": "er.dr.rd@gmail.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* affirm
    - utter_ask_anything
* deny
    - utter_goodbye
    - action_reset
    - reset_slots


## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_city
* restaurant_search{"city": "mumbai"}
    - slot{"city": "mumbai"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* choose{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"noresults": "true"}
    - utter_ask_ifemail
* deny
    - utter_ask_anything
* deny
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_city
* restaurant_search{"city": "new delhi"}
    - slot{"city": "new delhi"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* choose{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* affirm
    - utter_askemail
* send_email{"email": "deepika.hariharan@gmail.com"}
    - slot{"email": "deepika.hariharan@gmail.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* affirm
    - utter_goodbye
    - action_reset

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_city
* restaurant_search{"city": "chennai"}
    - slot{"city": "chennai"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_budget
* choose{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* deny
    - utter_ask_anything
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
## interactive_story_5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_city
* restaurant_search{"city": "bijapur"}
    - slot{"city": "bijapur"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* choose{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* affirm
    - utter_askemail
* ask_email{"email": "ab.cd@upgrad.com"}
    - slot{"email": "ab.cd@upgrad.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* affirm
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"city": "varanasi", "budget": "medium"}
    - slot{"budget": "medium"}
    - slot{"city": "varanasi"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"city": "varanasi"}
    - utter_ask_ifemail
* deny
    - utter_ask_anything
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
	
## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "city": "bhopal", "budget": "high"}
    - slot{"budget": "high"}
    - slot{"city": "bhopal"}
    - slot{"cuisine": "north indian"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - action_search_restaurants
    - slot{"city": "bhopal"}
    - utter_ask_ifemail
* send_email{"email": "deepika.hariharan@gmail.com"}
    - slot{"email": "deepika.hariharan@gmail.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"city": "patna"}
    - slot{"city": "patna"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"city": "patna"}
    - utter_ask_ifemail
* deny
    - utter_ask_anything
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "city": "ajmer"}
    - slot{"city": "ajmer"}
    - slot{"cuisine": "north indian"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_budget
* choose{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"noresults": "true"}
    - utter_noresults
* restaurant_search{"cuisine": "chinese", "city": "ajmer"}
    - slot{"city": "ajmer"}
    - slot{"cuisine": "chinese"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "any"}
    - slot{"budget": "any"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* affirm
    - utter_askemail
* send_email{"email": "deepika.hariharan@gmail.com"}
    - slot{"email": "deepika.hariharan@gmail.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "medium", "city": "pune"}
    - slot{"budget": "medium"}
    - slot{"city": "pune"}
    - slot{"cuisine": "chinese"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* deny
    - utter_ask_anything
* deny
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_city
* restaurant_search{"city": "mubmai"}
    - slot{"city": "mubmai"}
    - action_check_city
    - slot{"city_tier12": "false"}
    - utter_repeat
* restaurant_search{"city": "mumbai"}
    - slot{"city": "mumbai"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* choose{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"noresults": "true"}
    - utter_noresults
* deny
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_12
* greet
    - utter_greet
* restaurant_search
    - utter_ask_city
* restaurant_search{"city": "mubmai"}
    - slot{"city": "mubmai"}
    - action_check_city
    - slot{"city_tier12": "false"}
    - utter_repeat
* restaurant_search{"city": "mumbai"}
    - slot{"city": "mumbai"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "any"}
    - slot{"budget": "any"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* send_email
    - utter_askemail
* send_email{"email": "deepika.hariharan@gmail.com"}
    - slot{"email": "deepika.hariharan@gmail.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* affirm
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_13
* greet
    - utter_greet
* restaurant_search
    - utter_ask_city
* restaurant_search{"budget": "medium", "city": "kanpur", "cuisine": "north indian"}
    - slot{"budget": "medium"}
    - slot{"city": "kanpur"}
    - slot{"cuisine": "north indian"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - action_search_restaurants
    - slot{"city": "kanpur"}
    - utter_ask_ifemail
* deny
    - utter_ask_anything
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "city": "cuttack", "budget": "any"}
    - slot{"budget": "any"}
    - slot{"city": "cuttack"}
    - slot{"cuisine": "south indian"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* affirm
    - utter_askemail
* ask_email{"email": "abcdeh"}
    - slot{"email": "abcdeh"}
    - action_check_email
    - slot{"email_validate": "false"}
    - utter_repeat
* ask_email{"email": "sumandhir2011@gmail.com"}
    - slot{"email": "sumandhir2011@gmail.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* affirm
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "city": "agra"}
    - slot{"city": "agra"}
    - slot{"cuisine": "north indian"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* affirm
    - utter_askemail
* send_email{"email": "er.dr.rd@gmail.com"}
    - slot{"email": "er.dr.rd@gmail.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* affirm
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_16
* greet
    - utter_greet
* restaurant_search
    - utter_ask_city
* restaurant_search{"city": "new delhi"}
    - slot{"city": "new delhi"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "any"}
    - slot{"budget": "any"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* affirm
    - utter_askemail
* send_email{"email": "er.dr.rd@gmail.com"}
    - slot{"email": "er.dr.rd@gmail.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"city": "indore"}
    - slot{"city": "indore"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "any"}
    - slot{"budget": "any"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* deny
    - utter_ask_anything
* restaurant_search{"city": "chennai"}
    - slot{"city": "chennai"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* choose{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* affirm
    - utter_goodbye

## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"city": "silliguri"}
    - slot{"city": "silliguri"}
    - action_check_city
    - slot{"city_tier12": "false"}
    - utter_nontier
* restaurant_search{"city": "siliguri"}
    - slot{"city": "siliguri"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - utter_ask_cuisine
* choose{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"buget": "medium"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* deny
    - utter_ask_anything
* deny
    - utter_goodbye
    - action_reset
    - reset_slots

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "city": "goa", "budget": "any"}
    - slot{"budget": "any"}
    - slot{"city": "goa"}
    - slot{"cuisine": "chinese"}
    - action_check_city
    - slot{"city_tier12": "true"}
    - action_search_restaurants
    - slot{"noresults": "false"}
    - utter_ask_ifemail
* affirm
    - utter_askemail
* ask_email{"email": "clinton.r@upgrad.com"}
    - slot{"email": "clinton.r@upgrad.com"}
    - action_check_email
    - slot{"email_validate": "true"}
    - action_send_email
    - slot{"mail_sent": "true"}
* affirm
    - utter_goodbye
    - action_reset
    - reset_slots
