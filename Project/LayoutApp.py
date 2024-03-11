#All imports from KIVY needed to manage inputs and screen navigation
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
#Importing the RoutePl class from the file RoutePlan
from RoutePlan import RoutePl
import sys

class Homepage(Screen):
    def app_exit():
        sys.exit()


class RoutePlan_Page(Screen):
    #Initiating all variables used across functions
    #Due to KIVY preloading its files, any variables used for labels that may later be changed must also be initialised
    RoutePl=RoutePl()
    start_display, des_display= StringProperty(""), StringProperty("")
    startloc, desloc= "", ""
    error_display=StringProperty("")

    #error_check checks that both start and destination have an input
    error_check=[0, 0]
    state="False"

    #When the start location information is entered
    def on_text_val_s(self, widget):
        #Gets information from widget
        self.startloc=widget.text

        #Tries to find and output most likely location address from API information
        try:
            #Requests possible address array from API in RoutePl file
            startloc_addresses=self.RoutePl.AddressLookup(self.startloc)
            #Returns the first item to be displayed on the screen
            self.start_display=startloc_addresses[0]
            #valid start info has been input so error_check[0] is changed to 1
            self.error_check[0]=1
            #No errors need to be displayed
            self.error_display=""
        #Means no address information was found and an error should be displayed
        except:
            self.error_display="That address cant be found, please check your inputs"
            self.error_check[0]=0
        
    #When the destination location information is entered
    def on_text_val_d(self, widget):
        self.desloc=widget.text
        try:
            desloc_addresses=self.RoutePl.AddressLookup(self.desloc)
            self.des_display=desloc_addresses[0]
            self.error_check[1]=1
            self.error_display=""
        except:
            self.error_display="That address cant be found, please check your inputs and your internet connection"
            self.error_check[1]=0
    
    #When the plan button has been pressed
    def on_plan_press(self, widget):
        #Checks both start and destination have valid inputs
        if self.error_check==[1, 1]:
            #Requests the coordinates for each address from the GeoLoc class in RoutePl
            startcoords, descoords=self.RoutePl.GeoLoc(self.startloc, self.desloc)
            #Due to KIVY classes not accepting parameters that are not part of the KIVY package, steps must be global in order to access it from the  RouteJor_page class
            global steps
            #Requests the directions from the RouteSteps class in ROutePl
            steps=self.RoutePl.RouteSteps(startcoords, descoords)
            self.state="True"
        else:
            self.state="False"


class RouteJor_Page(Screen):
    count=-1
    #Due to KIVY preloading all its files, if steps has not yet been defined it must be defined as an empty array to prevent errors
    try:
        steps=steps
    except:
        steps=[""]
    current_step=StringProperty(steps[0])

    #When either 'next' or 'previous' step has been clicked
    def step_press(self, change):
        #Checks if the user has reached their destination
        if self.count!=len(steps):
            #Steps has changed by the amount given as a parameter and the new current step is then displayed
            self.count+=change
            self.current_step=str(steps[self.count])
        else:
            self.current_step="You have reached your destination!"


class WindowManager(ScreenManager):
    pass

kv=Builder.load_file('layout.kv')

#Builds the KIVY layout.kv file and runs it
class RunApp(App):
    def build(self):
        return kv