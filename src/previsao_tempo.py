import requests
from geopy.geocoders import Nominatim
import pycep_correios

API_KEY = "4028d31fdc849ecbf85ae65cc204e44a"

class PrevisaoTempo:
    def __init__(self,texto):
        self.texto = texto

    # Falta melhorar, não está recebendo o parametro de texto
    def informar_previsao(self):
        API_KEY = "4028d31fdc849ecbf85ae65cc204e44a"

        endereco = pycep_correios.get_address_from_cep('51300020')  # MELHORAR
        cidade = endereco['cidade']
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        temperatura = requisicao_dic['main']['temp'] - 273.15
        print(f"{int(temperatura)}º Graus Celsius")

