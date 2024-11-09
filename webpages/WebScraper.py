import requests
from bs4 import BeautifulSoup


class WebScraper:

    def scrape(self, url):
        r = requests.get(url)
        self.soup = BeautifulSoup(r.content, 'html.parser')
