from bs4 import BeautifulSoup
import requests
import json
import html

marken = 'https://www.kfz-auskunft.de/autohersteller.html'
content = requests.get(marken)
soup = BeautifulSoup(content.text, 'html.parser')
print(soup)
