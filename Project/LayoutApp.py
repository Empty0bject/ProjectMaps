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
    #Settings=Settings()
    #def on_font_press(self, selection):
    #    print("button pressed")
    #    current_settings[0]= self.Settings.Font(selection)
    #    print("font changed")
    #    print(current_settings[0])
    #    RunApp().run()

class Homepage(Screen):
    pass
    #current_settings=current_settings

class RoutePlan_Page(Screen):
    error_disp=StringProperty("")
    RoutePl=RoutePl()
    inp_check=[0, 0]
    print(inp_check)
    #current_settings=current_settings

    #accesses the address info input by the user
    def on_text_val_s(self, widget):
        self.inp_check[0]=1
        self.startingloc_info=widget.text
        print(self.inp_check)
    def on_text_val_d(self, widget):
        self.inp_check[1]=1
        self.endingloc_info=widget.text
        print(self.inp_check)
    
    def on_plan_press(self, widget):
        if self.inp_check!=[1, 1]:
            print("requirements not met")
            error_displ="Please enter a start/desination"
        elif self.inp_check==[0, 0]:
            #returns address information
            loc=self.RoutePl.GeoLoc(self.startingloc_info, self.endingloc_info)
            #returns the starting and ending coordinates of the addresses
            startcoords, descoords=self.RoutePl.GeoLoc(self.startingloc_info, self.endingloc_info)
            #returns the steps for the directions in an array format
            global steps
            steps=self.RoutePl.RouteSteps(startcoords, descoords)
            print(steps)
        print("funtion complete")

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

#global current_settings
#current_settings=["Roboto/Roboto-Regular.ttf"]
kv=Builder.load_file('layout.kv')

class RunApp(App):
    def build(self):
        return kv