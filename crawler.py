from bs4 import BeautifulSoup
import requests
import pprint
# import Collections

class InfoHandler:

    list_all = []
    list_brand = []
    dict = {}
    list_picture = []
    site = ''
    dict = {
        'brand': '',
        'picture': ''
    }

    def set_all_brands(self, brands):
        brands = brands.upper()
        print(brands)

    def set_site(self, add = '', base='https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/'):
        if add == '':
            self.site = base
        else:
            add = add.upper().lower()
            self.site = base + add
        #print(f"The current site is {self.site}")

    def get_site(self):
        return self.site

    def get_content(self):
        content_raw = requests.get(self.get_site())
        soup = BeautifulSoup(content_raw.text, 'html.parser')
        return soup

handler = InfoHandler()
handler.set_site()
soup = handler.get_content()

replace_pic_string = 'https://www.adac.de/_ext/ITR/Tests/Autodaten/Markenlogos/Resized/'

for div in soup.find_all('div'):
    for a in div.find_all('a'):
        for img in a.find_all('img'):
            handler.list_brand.append(img['alt'])
            handler.list_picture.append(img['src'])


for i in range(0, len(handler.list_brand)):
    handler.set_site(add=handler.list_brand[i])
    if handler.list_brand[i] == '':
        continue
    handler.dict = {
        'brand': handler.list_brand[i],
        'picture': handler.list_picture[i],
        'site': handler.get_site()# + handler.list_brand[i]
    }
    pprint.pprint(handler.dict)
