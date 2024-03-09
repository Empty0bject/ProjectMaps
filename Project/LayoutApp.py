from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from RoutePlan import RoutePl
from kivy.core.text import LabelBase, DEFAULT_FONT
from settings import Settings

class Settings_Page(Screen):
    pass

class Homepage(Screen):
    pass

class RoutePlan_Page(Screen):
    start_display, des_display= StringProperty("start test"), StringProperty("des test")
    startloc, desloc= "", ""
    RoutePl=RoutePl()
    error_disp=StringProperty("")

    #accesses the address info input by the user
    def on_text_val_s(self, widget):
        self.startloc=widget.text
        startloc_addresses=self.RoutePl.AddressLookup(self.startloc)
        self.start_display=startloc_addresses[0]
        
    def on_text_val_d(self, widget):
        self.desloc=widget.text
        desloc_addresses=self.RoutePl.AddressLookup(self.desloc)
        self.des_display=desloc_addresses[0]

    def on_plan_press(self, widget): 
        startcoords, descoords=self.RoutePl.GeoLoc(self.startloc, self.desloc)
        global steps
        steps=self.RoutePl.RouteSteps(startcoords, descoords)
        print(steps)

class RouteJor_Page(Screen):
    count=-1
    try:
        steps=steps
    except:
        steps=[""]
    current_step=StringProperty(steps[0])

    def step_press(self, change):
        if self.count<=-2:
            count+=2
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

kv=Builder.load_file('layout.kv')

class RunApp(App):
    def build(self):
        return kv