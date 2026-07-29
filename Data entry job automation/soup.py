import requests
from bs4 import BeautifulSoup
import re

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

class CollectData:
    def __init__(self):
        response = requests.get(ZILLOW_URL)
        response.raise_for_status()
        full_data = response.text
        soup = BeautifulSoup(full_data, 'html.parser')
        self.data = soup.find_all(name='li',class_='ListItem-c11n-8-84-3-StyledListCardWrapper')

    def get_address(self):
        addresses = [i.find(name='address').text.strip() for i in self.data]
        return addresses

    def get_price(self):
        prices = [re.search(r"\$[\d,]+",i.find(name='span',class_='PropertyCardWrapper__StyledPriceLine').text).group() for i in self.data]
        return prices

    def get_link(self):
        links = [i.find(name='a',class_='property-card-link').get('href') for i in self.data]
        return links
