#main.py
from layout import plot_layout
import requests
import sys
    

class Main:
	def __init__(self):
		self.running=True
		self.layout=plot_layout()

	def run(self):
		while self.running:
			self.layout.homepage()
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