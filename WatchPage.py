## https://www.reddit.com/r/streetwear/comments/5er27n/python_tutorial_restock_release_monitor_notifier/?st=ivxbcaly&sh=f853a5a1

import time
import requests
import smtplib 
from timeit import default_timer as timer 

start = timer()

def send_email(user, pwd, recipient, subject, body):
	"""INPUT: gmail username, gmail password, a list of recipients, a subject, and a body"""
	gmail_user 	= user
	gmail_pwd 	= pwd
	FROM 		= user
	TO 			= recipient if type(recipient) is list else [recipient]
	SUBJECT 	= subject
	TEXT 		= body

	# prepare actual message
	message = "From: {}\nTo: {}\nSubject: {}\n\n{}".format(FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587) # start Simple Mail Transfer Protocol server on port 587
		server.ehlo() # establish connection
		server.starttls() # put communication in Transport Layer Security mode, encrypting all data
		server.ehlo() # second time
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		server.quit()
		print("Mail sent")
	except Exception as e:
		print("failed to send mail, " + str(e))

def main():


	with requests.Session() as s:
		url 					= "http://www.supremenewyork.com/shop"
		time_between_checks 	= 120 # seconds
		user 					= "justinmi16@mittymonarch.com"
		pwd 					= "legomaniac"
		recipient 				= "justin.mi@berkeley.edu"
		subject 				= "SITE UPDATED"
		body 					= "CHANGE AT " + str(url)

		page1 = s.get(url) # "old page" that will be compared against

		time.sleep(time_between_checks) # pause execution 

		page2 = s.get(url) # "new page" that will be compared against "old page"

		if page1.content == page2.content:
			end = timer()
			if end - start >= 60:
				time_minutes = (end - start) / 60
				print("[-] No change detected @ " + str(url))
				print("Elapsed time: " + str(time_minutes) + " minutes")
			else:
				print("[-] No change detected @ " + str(url))
				print("[-] Elapsed time: " + str(end - start) + " seconds")
		else:
			print(page1.content)
			print(page2.content)
			end = timer()
			if end - start >= 60:
				time_minutes = (end - start) / 60
				print("[+] Change detected @ " + str(url))
				print("[+] Elapsed time: " + str(time_minutes) + " minutes")
			else:
				print("[+] Change detected @ " + str(url))
				print("[+] Elapsed time: " + str(end - start) + " seconds")

			send_email(user, pwd, recipient, subject, body)

		page2 = None

		main()

if __name__ == "__main__":
	main()





