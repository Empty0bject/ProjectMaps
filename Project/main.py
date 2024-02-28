#main.py
from LayoutApp import plot_layout
import requests
import sys
    

class Main:
	def __init__(self):
		self.running=True
		self.LayoutApp=plot_layout().run()

	def run(self):
		while self.running:
			self.LayoutApp()
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