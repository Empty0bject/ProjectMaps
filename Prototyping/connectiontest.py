import openrouteservice
from openrouteservice.directions import directions
import requests
import json
import sys

coords = ((-1.5662230584012848, 54.99494634402549),(-1.5808882542425002, 54.99437627680842))

try:
    client = openrouteservice.Client(key='5b3ce3597851110001cf6248991939055b9748d3b3fefcf616ea5a79')
    routes = directions(client, coords, profile='foot-walking')
except requests.exceptions.ConnectionError:
    print("No internet connection, please try again")
    sys.exit()


dump=json.dumps(routes)
parsed=json.loads(dump)


for item in range(0, len(parsed["routes"][0]["segments"][0]["steps"])):
    instruction=parsed["routes"][0]["segments"][0]["steps"][item]["instruction"]
    print(instruction)