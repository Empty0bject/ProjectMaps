from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from RoutePlan import RoutePl
from kivy.core.text import LabelBase, DEFAULT_FONT

class Settings_Page(Screen):
    pass

class Homepage(Screen):
    pass


class RoutePlan_Page(Screen):
    RoutePl=RoutePl()
    start_display, des_display= StringProperty(""), StringProperty("")
    startloc, desloc= "", ""
    error_display=StringProperty("")

    error_check=[0, 0]
    state="False"

    
    def on_text_val_s(self, widget):
        self.startloc=widget.text
        try:
            startloc_addresses=self.RoutePl.AddressLookup(self.startloc)
            self.start_display=startloc_addresses[0]
            self.error_check[0]=1
            self.error_display=""
        except:
            self.error_display="That address cant be found, please check your inputs"
            self.error_check[0]=0
        
    def on_text_val_d(self, widget):
        self.desloc=widget.text
        try:
            desloc_addresses=self.RoutePl.AddressLookup(self.desloc)
            self.des_display=desloc_addresses[0]
            self.error_check[1]=1
            self.error_display=""
        except:
            self.error_display="That address cant be found, please check your inputs"
            self.error_check[1]=0

    def on_plan_press(self, widget):
        if self.error_check==[1, 1]:
            startcoords, descoords=self.RoutePl.GeoLoc(self.startloc, self.desloc)
            global steps
            steps=self.RoutePl.RouteSteps(startcoords, descoords)
            print(steps)
            self.state="True"
        else:
            print("error caught")
            self.state="False"
        print(self.state)


class RouteJor_Page(Screen):
    count=-1
    try:
        steps=steps
    except:
        steps=[""]
    current_step=StringProperty(steps[0])

    def step_press(self, change):
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