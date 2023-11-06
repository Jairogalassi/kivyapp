
import plyer
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDFloatingActionButton


      
class Principal(ScreenManager):
    pass


class myApp(MDApp):
    def make_phone_call(phone_number):
        try:
            plyer.call('+543401416226')
        except plyer.PlyerException:
            # Maneja la excepción si la llamada no se puede realizar
            print("No se puede realizar la llamada telefónica.")
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.theme_style = 'Light'
        Builder.load_file('menu.kv')
        return Principal()
    def change_style(self, checked, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'    
if __name__ == '__main__':
    myApp().run()