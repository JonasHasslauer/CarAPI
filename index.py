from bs4 import BeautifulSoup
import requests
import json
import html

marken = 'https://www.kfz-auskunft.de/autohersteller.html'
soup = BeautifulSoup(content.text, 'html.parser')
