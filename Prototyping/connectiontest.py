import openrouteservice
import urllib.request

connection=True
while connection==True:
    try:
        urllib.request.urlopen("https://openrouteservice.org")
        print("Connected")
    except urllib.error.URLError:
        print("Connection lost")