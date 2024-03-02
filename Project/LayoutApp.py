import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window  import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import *


Window.clearcolor = kivy.utils.get_color_from_hex('d8dee8')

class Container(AnchorLayout):
    def __init__(self, lbl_text, btn_text):
        self.lbl_text=lbl_text
        self.btn_text=btn_text
        lbl=Label(text=self.lbl_text,
                  color=kivy.utils.get_color_from_hex('8b919d'),
                  anchor_x='top',
                  anchor_y='center')
        btn=Button(text=self.btn_text,
                   background_color=kivy.utils.get_color_from_hex('8b919d'),
                   color=kivy.utils.get_color_from_hex('111111'),
                   size_hint=(.3, .2),
                   anchor_x='center',
                   anchor_y='center')
        self.add_widget(lbl)
        self.add_widget(btn)
    
class Homepage(App):
    def build(self):
        parent=Container('MapRoute', 'Plan route')
        return parent

class Settings_page(App):
    def build(self):
        pass

class Routeplan_page(App):
    def build(self):
        pass

class Routejor_page(App):
    def build(self):
        pass