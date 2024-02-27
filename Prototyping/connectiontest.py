import openrouteservice
import requests

connection=True
while connection==True:
    try:
        response = requests.get("https://openrouteservice.org", timeout=5)
    except requests.ConnectionError:
        print("Connection lost")