import kivy
from kivy.app import App
from kivy.uix.label import Label
    
class plot_layout(App):
    def build(self):
        lbl=Label(text ="test")
        return lbl
    #def homepage(self):
        #return self.build.lbl()