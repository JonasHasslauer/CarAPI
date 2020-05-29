from bs4 import BeautifulSoup
import requests
import json
import html
import re


list_all = []

site2 = 'https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/'
content = requests.get(site2)
soup = BeautifulSoup(content.text, 'html.parser')

def get_brand_names():
    for div in soup.find_all('div'):
        for link in div.find_all('a'):
            for img in link.find_all('img'):
                list_all.append(img['alt'])

    list_org = list(set(list_all))

    for x in range(0, len(list_org)-1):
        if list_org[x] == '':
            list_org.remove(list_org[x])
        if list_org[x].islower():
            list_org[x] = list_org[x].capitalize()
        if list_org[x].isupper():
            list_org[x] = list_org[x].lower().capitalize()

    print(sorted(list(set(list_org))))
