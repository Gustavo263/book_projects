# Esse programa pega todos os produtos da página solicitada e imprimi todos esses itens no prompt de comando.

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math


url = "https://www.kabum.com.br/espaco-gamer/cadeiras-gamer"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, "html.parser")
qtd_items = soup.find("div", id="listingCount").get_text().strip()

index = qtd_items.find(" ")
qtd = qtd_items[:index]

last_page = math.ceil(int(qtd) / 20)

dic_produt = {"marca": [], "preco": []}

for i in range(1, last_page + 1):
    url_page = f"https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched"

    site = requests.get(url_page, headers=headers)
    soup = BeautifulSoup(site.content, "html.parser")
    produts = soup.find_all("div", class_=re.compile("productCard"))

    for produt in produts:
        marca = produt.find("span", class_=re.compile("nameCard")).get_text().strip()
        preco = produt.find("span", class_=re.compile("priceCard")).get_text().strip()

        print(marca, preco)

        dic_produt["marca"].append(marca)
        dic_produt["preco"].append(preco)
    
    print(f"\33[2;49;34m {url_page}\33[m")


# Cria um documento na sua máquina para poder ser executado excel

df = pd.DataFrame(dic_produt)
df.to_csv(r"C:\Users\Gustavo\Downloads/preco_cadeira.csv", encoding="utf-8", sep=";")