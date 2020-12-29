from colorama import init, Fore
import os
import requests
import platform
import time

from discord_webhook import DiscordWebhook


class Initialize():
	init()  # Initialize colorama


class __main__():
	"Spamhook's main class. DO NOT MESS WITH ANYTHING IN HERE!!!!!!!!!"
	
	

	if platform.system() == "Windows": # checking the OS of the device running the tool
	    clr = "cls"
	else:
	    clr = "clear"
	
	os.system(clr)
	
	
	# Heres where the actual tool starts.
	def Spamhook():
		"Spamhook's actual system."
		print("""
|------------------------------------------------------------------------|
| WELCOME TO:                                                            |
| ███████╗██████╗  █████╗ ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗  | Made by LinkerScript
| ██╔════╝██╔══██╗██╔══██╗████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝  | Version: 4.2B
| ███████╗██████╔╝███████║██╔████╔██║███████║██║   ██║██║   ██║█████╔╝   | Type: FREE
| ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗   | Do not skid this.
| ███████║██║     ██║  ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗  | 
| ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝  |
|------------------------------------------------------------------------|
		""")
		webhook = input("($) Enter webhook URL >>> ")
		username = input("($) Enter username to spam with >>> ")
		message = input("($) Enter custom message to spam with >>> ")
		while True:
			spam = DiscordWebhook(url=webhook, content=message, username=username)
			response = spam.execute()
			print("(SYS) >>> Sent webhook with username " + username + " to webhook with message " + message  + " successfully.")
	Spamhook()