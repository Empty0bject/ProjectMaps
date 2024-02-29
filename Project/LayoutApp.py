import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window  import Window
from kivy.uix.label import Label

Window.clearcolor = (216, 222, 232, 1)

class Homepage(App):
    def build(self):
        layout=AnchorLayout(
            anchor_x='center', anchor_y='top')
        lbl=Label(text='MapRoute',
                  color=(0, 0, 0, 1))
        layout.add_widget(lbl)
        return layout
    
class Settings_page(App):
    def build(self):
        pass

class Routeplan_page(App):
    def build(self):
        pass

class Routejor_page(App):
    def build(self):
        pass