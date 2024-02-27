import openrouteservice
from openrouteservice.geocode import pelias_autocomplete
import json


client = openrouteservice.Client(key='5b3ce3597851110001cf6248991939055b9748d3b3fefcf616ea5a79')

inp=input("Location: ")
geocode=openrouteservice.geocode.pelias_search(client, inp, focus_point=None, rect_min_x=None, rect_min_y=None, rect_max_x=None, rect_max_y=None, circle_point=None, circle_radius=None, country="GBR", size=None)

dump=json.dumps(geocode)
parsed=json.loads(dump)

for item in range(0, (len(parsed["features"]))):
    print(parsed["features"][item]["properties"]["label"], "\n", parsed["features"][item]["geometry"]["coordinates"])