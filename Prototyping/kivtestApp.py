import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class Homepage(BoxLayout):
    count=0
    my_text=StringProperty("0")
    text_input_str=StringProperty("Enter text")
    def on_button_click(self):
        self.count+=1
        self.my_text= str(self.count)
    def on_text_validate(self, widget):
        self.text_input_str=widget.text
        
class KivtestApp(App):
    pass

KivtestApp().run()