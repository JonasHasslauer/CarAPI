from bs4 import BeautifulSoup
import requests, pprint

list_all = []

site2 = 'https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/'
content = requests.get(site2)
soup = BeautifulSoup(content.text, 'html.parser')

def get_brand_names():

    replace_pic_string = 'https://www.adac.de/_ext/ITR/Tests/Autodaten/Markenlogos/Resized/'

    for div in soup.find_all('div'):
        for link in div.find_all('a'):
            for img in link.find_all('img'):
                list_all.append(img['alt'])
                dict['brand'].append(img['alt'])

                if len(img['src'].replace(replace_pic_string, '')) > 50:
                    continue
                else:
                    dict['picture'].append(img['src'].replace(replace_pic_string, ''))

    list_org = list(set(list_all))

    for x in range(0, len(list_org)-1):
        if list_org[x] == '':
            list_org.remove(list_org[x])
        if list_org[x].islower():
            list_org[x] = list_org[x].capitalize()
        if list_org[x].isupper():
            list_org[x] = list_org[x].lower().capitalize()

        list_org[x] = list_org[x].upper()


def get_full_pic_link():
    # take replace_big_string
    pass



get_brand_names()
