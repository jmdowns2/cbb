import requests
from bs4 import BeautifulSoup


class WebScraper:

    def scrap(self, url):

        # Making a GET request
        r = requests.get(url)

        # check status code for response received
        # success code - 200
        print(r)

        # Parsing the HTML
        self.soup = BeautifulSoup(r.content, 'html.parser')
        print(self.soup.prettify())