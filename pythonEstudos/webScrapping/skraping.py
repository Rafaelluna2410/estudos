from bs4 import BeautifulSoup
import requests


URL = "https://docs.google.com/document/d/e/2PACX-1vSpiaUI14T_1CTGCU1LOn79uCel-UastE9lznOV6HSx2U-OaaYTunxdrPCQR5HP3EpsYXgWsu4EaCCk/pub"

teste= {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

site = requests.get(URL, headers=teste)
soup = BeautifulSoup (site.content, 'html.parser')

paginas = soup.find('div', attrs={'class': 'c19 doc-content'})
print(paginas)