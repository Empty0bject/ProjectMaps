import openrouteservice
from openrouteservice.geocode import pelias_autocomplete
import json

class RoutePl():
    def __init__(self):
        self.client = openrouteservice.Client(key='5b3ce3597851110001cf6248991939055b9748d3b3fefcf616ea5a79')
    def GeoLoc(self, startloc, desloc):
        startcoord=openrouteservice.geocode.pelias_search(self.client, startloc, focus_point=None, rect_min_x=None, rect_min_y=None, rect_max_x=None, rect_max_y=None, circle_point=None, circle_radius=None, country="GBR", size=None)
        endcoord=openrouteservice.geocode.pelias_search(self.client, desloc, focus_point=None, rect_min_x=None, rect_min_y=None, rect_max_x=None, rect_max_y=None, circle_point=None, circle_radius=None, country="GBR", size=None)
        dump=json.dumps(geocode)
        parsed=json.loads(dump)