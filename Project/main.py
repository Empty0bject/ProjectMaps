#main.py
from LayoutApp import RunApp
import requests
import sys
    

class Main:
	def __init__(self):
		self.running=True
		self.Run_App=RunApp().run()

	def run(self):
		self.RunApp()
		while self.running:
			self.internet_connection()

	def internet_connection(self):
		try:
			response = requests.get("https://openrouteservice.org", timeout=5)
		except requests.ConnectionError or requests.exceptions.ReadTimeout:
			print("Connection lost")
			sys.exit()

if __name__=="__main__":
    main=Main()
    main.run()