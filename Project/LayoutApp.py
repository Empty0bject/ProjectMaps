from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from RoutePlan import RoutePl

class Homepage(Screen):
    pass

class Settings_Page(Screen):
    pass

class RoutePlan_Page(Screen):
    RoutePl=RoutePl()
    def on_text_val_s(self, widget):
        self.startingloc_info=widget.text
    def on_text_val_d(self, widget):
        self.endingloc_info=widget.text
    def on_plan_press(self, widget):
        loc=self.RoutePl.GeoLoc(self.startingloc_info, self.endingloc_info)
        startcoords, descoords=self.RoutePl.GeoLoc(self.startingloc_info, self.endingloc_info)
        steps=self.RoutePl.RouteSteps(startcoords, descoords)

class RouteJor_Page(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv=Builder.load_file('layout.kv')

class RunApp(App):
    def build(self):
        return kv