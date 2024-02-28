import kivy
from kivy.app import App
from kivy.uix.label import Label

def read_file():
    f = open("homepage_layout.txt", "r")
    print(f.read())

class plot_layout(App):
    def build(self):
        lbl=Label()
    def homepage(self):
        return self.build.lbl(text="test")
    
read_file()