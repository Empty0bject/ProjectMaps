from LayoutApp import RunApp
import requests
import sys
    

class Main:
	def __init__(self):
		self.Run_App=RunApp().run()

	def run(self):
		self.internet_connection()
		self.RunApp()
		

	def internet_connection(self):
		try:
			response = requests.get("https://openrouteservice.org", timeout=5)
		except requests.ConnectionError or requests.exceptions.ReadTimeout:
			print("Connection lost")
			sys.exit()

if __name__=="__main__":
    main=Main()
    main.run()