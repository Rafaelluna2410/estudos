from bs4 import BeautifulSoup  as rafael
import requests

""" 
telegram = "https://api.telegram.or/bot{}/getUpdates".format('6458851021:AAE1Cal5Iw6Ya3g9J5vCqAqjqWAkbqBAaEU')
response = requests.get(telegram) """
URL = "https://www.mercadolivre.com.br/teclado-gamer-logitech-pro-series-g-pro-qwerty-gx-blue-clicky-ingls-us-cor-preto-com-luz-rgb/p/MLB12866734#polycard_client=recommendations_home_navigation-recommendations&reco_backend=machinalis-homes-pdp-boos&reco_client=home_navigation-recommendations&reco_item_pos=1&reco_backend_type=function&reco_id=82dd121e-3422-4a6a-8d84-3f3ed9ca3b64&wid=MLB1814645392&sid=recos"

teste= {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

site = requests.get(URL, headers=teste)

soup = rafael (site.content, 'html.parser')

""" 
title = soup.find('h1', class_ ='ui-pdp-title').get_text()
price = soup.find('span', class_ ='andes-money-amount__fraction').get_text()


if price <= '750':
    print(title, 'preço: ', price)
    
else:
    print(title, 'muito caro')
 """

def proximapagina(soap):
    paginas = soup.find('button', {'class': 'andes-carousel-snapped__control andes-carousel-snapped__control--next andes-carousel-snapped__control--size-large'})

    if not paginas.find('button', {'class': 'andes-carousel-snapped__control andes-carousel-snapped__control--next andes-carousel-snapped__control--size-large andes-carousel-snapped__control--disabled'}):
        pront()