from bs4 import BeautifulSoup
import requests
import pprint


class CreateAPI:


info_dict = {
    'brand': [],
    'picture': [],
    'Baureihen': {
        'Generationen': {
            'Modelle': {
                'Typ': '',
                'Preis': '',
                'Motor': '',
                'Fuel': '',
                'Ausstattung': {
                    'Technik': '',
                    'Comfort': ''
                },
                'Power': '',
                'Bauzeitraum': '',
                'Preis': '',
                'HSN': '',
                'TSN': '',
                'VSN': '',
            },

        },
        'Generation': []
    }
}


def get_dict(self):
    return self.info_dict
