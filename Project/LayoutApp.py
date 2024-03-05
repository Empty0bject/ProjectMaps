from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from RoutePlan import RoutePl
from settings import Settings

class Homepage(Screen):
    pass

class Settings_Page(Screen):
    Settings=Settings()
    def on_font_press(self, selection):
        settings_store[0]=self.Settings.Font(selection)

class RoutePlan_Page(Screen):
    font_selection=settings_store[0]
    RoutePl=RoutePl()

    #accesses the address info input by the user
    def on_text_val_s(self, widget):
        self.startingloc_info=widget.text
    def on_text_val_d(self, widget):
        self.endingloc_info=widget.text
    
    def on_plan_press(self, widget):
        #returns address information
        loc=self.RoutePl.GeoLoc(self.startingloc_info, self.endingloc_info)
        #returns the starting and ending coordinates of the addresses
        startcoords, descoords=self.RoutePl.GeoLoc(self.startingloc_info, self.endingloc_info)
        #returns the steps for the directions in an array format
        global steps
        steps=self.RoutePl.RouteSteps(startcoords, descoords)

class RouteJor_Page(Screen):
    count=-1
    try:
        steps=steps
    except:
        steps=[""]
    print(steps)
    current_step=StringProperty(steps[0])
    def step_press(self, change):
        if self.count<=-2:
            count+=1
        if self.count!=len(steps):
            try:
                self.count+=change
                self.current_step=str(steps[self.count])
            except:
                pass
        else:
            self.current_step="You have reached your destination!"
        

class WindowManager(ScreenManager):
    pass

global settings_store
settings_store=["standard"]
kv=Builder.load_file('layout.kv')

class RunApp(App):
    def build(self):
        return kv