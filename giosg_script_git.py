#!/usr/bin/env python3

import smtplib
import time
import requests
import sys
import json

from datetime import datetime

org_id = "organization_id"
app_id = "app_id"
auth = "webhook_auth_token"
auth_user = "user_auth_token"
WEBHOOK_ENDPOINT = "webhook_log_entry_api_url" % (org_id, app_id)
user_id = "user_id"
EMPTY_CHAT = "empty_chat_api_url" % (user_id)

#post to create new webhook
def function_web():
	response.get(url=WEBHOOK_ENDPOINT, headers = {"Authorization": auth_user})

#create a new webhook using empty chat, no visitor
def second():
	s = requests.get(url=WEBHOOK_ENDPOINT, headers = {"Authorization": auth_user})		


#function to send email if there is a problem in webhook creation
def sendEmail(message):
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("adress@gmail.com", "password")
	server.sendmail(
		"from@gmail.com",
		"to@gmail.com",
		message)
	server.quit()	

#create webhook and check webhook log entries
def first():
	#post to create a new webhook
	r = requests.post(url = EMPTY_CHAT, headers = {"Authorization": auth})
	if r.status_code != requests.codes.created:
		sendEmail("no webhook created from post")
	else:
		m = r.json()
		#get webhook logs from app
		s = requests.get(url=WEBHOOK_ENDPOINT, headers = {"Authorization": auth_user})
		a = s.json()
		#if you are not sure what you get from requests, you can print the response json
		#print(m)
		#print(a)
		if m["id"] == a["results"][0]["resource_id"]:
			#taking the status parameters from 5 first webhooks and sending them in the mail
			d = a["results"][0]["status"]
			c = a["results"][1]["status"]
			f = a["results"][2]["status"]
			e = a["results"][3]["status"]
			k = a["results"][4]["status"]
			message = d + '\n' + c + '\n' + f + '\n' + e + '\n' + k
			sendEmail(message)
		elif m["id"] == a["results"][1]["resource_id"]:
			return None	
		elif m["id"] == a["results"][2]["resource_id"]:
			return None
		elif m["id"] == a["results"][3]["resource_id"]:
			return None
		elif m["id"] == a["results"][4]["resource_id"]:
			return None			
		else:	
			sendEmail(d)
		
def main(argv):
	first()

if __name__ == "__main__":
	main(sys.argv[1:])



