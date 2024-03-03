from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

class Homepage(Screen):
    pass

class Settings(Screen):
    pass

class RoutePlan(Screen):
    pass

class RouteJor(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv=Builder.load_file('layout.kv')

class RunApp(App):
    def build(self):
        return kv
    
RunApp().run()