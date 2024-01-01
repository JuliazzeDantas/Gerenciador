from kivy.app import App
from kivy.app import Builder

import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        
        self.root.ids["moeda1"].text = f"Dollar: U${self.get_value('USD')}"
        self.root.ids["moeda2"].text = f"Euro: E${self.get_value('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin: B${self.get_value('BTC')}"

    def get_value(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        request = requests.get(link)
        value = request.json()[f'{moeda}BRL']['bid']
        return value
    
MeuAplicativo().run()