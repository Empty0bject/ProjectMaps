from LayoutApp import RunApp
import requests
import sys
    

class Main:
	def __init__(self):
		#This will run the app in the LayoutApp file
		self.Run_App=RunApp().run()

	def run(self):
		connection=self.internet_connection()
		while connection==True:
			self.RunApp()
		

	def internet_connection(self):
		#Requests data from the ORS website
		try:
			#If a responce is recieved then the device is connected to the website
			response = requests.get("https://openrouteservice.org", timeout=5)
			return True
		except requests.ConnectionError or requests.exceptions.ReadTimeout:
			#If not then there is no connection and the program wont run
			return False

#Runs the code present in this file
if __name__=="__main__":
    main=Main()
    main.run()