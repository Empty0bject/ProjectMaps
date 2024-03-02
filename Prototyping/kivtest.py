from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import NumericProperty

import datetime

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '500')
# Config.write() This writes to kivy config


class MoneyManager(FloatLayout):
    month = datetime.datetime.now().strftime("%B")
    date = datetime.datetime.now().strftime("%w")
    fulldate = (month + ", " + date)
    # Make these kivy properties if they are going to be updated
    savings = NumericProperty(0.00)

    def add_savings(self):
        self.savings += 100

class MoneyManagerApp(App):
    def build(self):
        return Builder.load_file('total_wealth.kv')


MoneyManagerApp().run()