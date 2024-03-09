import openrouteservice
from openrouteservice.geocode import pelias_autocomplete
from openrouteservice.directions import directions
import json

class RoutePl():
    def __init__(self):
        self.client = openrouteservice.Client(key='5b3ce3597851110001cf6248991939055b9748d3b3fefcf616ea5a79')

    def AddressLookup(self, inp):
        info=json.dumps(openrouteservice.geocode.pelias_search(self.client, inp, focus_point=(-1.6142742628790723, 54.975358527736724), rect_min_x=None, rect_min_y=None, rect_max_x=None, rect_max_y=None, circle_point=(-1.6142742628790723, 54.975358527736724), circle_radius=50, country="GBR", size=None))
        info=json.loads(info)
        pos_address=[]

        for address in range(0, (len(info["features"]))):
            pos_address.append(info["features"][address]["properties"]["label"])
        return pos_address

    def GeoLoc(self, startinp, desinp):
        startinfo=json.dumps(openrouteservice.geocode.pelias_search(self.client, startinp, focus_point=None, rect_min_x=None, rect_min_y=None, rect_max_x=None, rect_max_y=None, circle_point=None, circle_radius=None, country="GBR", size=None))
        desinfo=json.dumps(openrouteservice.geocode.pelias_search(self.client, desinp, focus_point=None, rect_min_x=None, rect_min_y=None, rect_max_x=None, rect_max_y=None, circle_point=None, circle_radius=None, country="GBR", size=None))
        
        startinfo=json.loads(startinfo)
        desinfo=json.loads(desinfo)

        for item in range(0, (len(startinfo["features"]))):
            startinfo_pos=startinfo["features"][item]["geometry"]["coordinates"]
        for item in range(0, (len(desinfo["features"]))):
            desinfo_pos=desinfo["features"][item]["geometry"]["coordinates"]
        
        print("geoloc complete")
        return startinfo_pos, desinfo_pos

    def RouteSteps(self, startcoords, descoords):
        coords=(startcoords, descoords)
        routes = directions(self.client, coords, profile='foot-walking')

        dump=json.dumps(routes)
        parsed=json.loads(dump)
        steps=[]

        for item in range(0, len(parsed["routes"][0]["segments"][0]["steps"])):
            instruction=parsed["routes"][0]["segments"][0]["steps"][item]["instruction"]
            steps.append(instruction)
        
        return steps