from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock
from kivy.utils import platform
from kivy.core.window import Window

class TrovaTemperatura(App):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.INTERNET, Permission.ACCESS_NETWORK_STATE])
        
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        # widget Image
        self.window.add_widget(Image(source="logo.png"))
        
        # widget TextInput
        self.input_testo = TextInput(
            size_hint=(1,0.2),
            font_size='20sp',
            foreground_color='#000000',
            padding_y='12sp',
            halign='center'
        )
        self.window.add_widget(self.input_testo)
        
        # widget Button buildozer -v android debug
        self.bottone = Button(
            text="VIA!",
            size_hint=(1,0.2),
            bold=True,
            background_color='#0099ff'
        )
        self.window.add_widget(self.bottone)
        self.bottone.bind(on_press=self.trova_temp)
        
        # widget Label
        self.etichetta = Label(
            text="Cerca una città... ",
            font_size='20sp',
            color='#007dd1'
        )
        self.window.add_widget(self.etichetta)
        
        return self.window
        
    def edit_label(self, request, result):
        temp = result['main']['temp']
        self.etichetta.text = f"Oggi a {self.input_testo.text} ci sono {temp}˚C"

    def trova_temp(self, instance):
        posto=self.input_testo.text
        posto = posto.replace(' ', '%20')
        link = f"https://api.openweathermap.org/data/2.5/weather?q={posto}&appid=d7d80b56700431c8027827cc9932af78&units=metric"
        UrlRequest(link, on_success=self.edit_label, on_failure=self.city_not_found)

    def city_not_found(self, request, result):
        self.etichetta.text = "La città che stai cercando è inesistente"
        Clock.schedule_once(self.reset_label, 4)
        
    def reset_label(self, dt):
        self.etichetta.text = "Cerca una città..."
    
TrovaTemperatura().run()
