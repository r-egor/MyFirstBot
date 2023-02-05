# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup

#Print HTML code from http://quotes.toscrape.com/
def print_quotes():
    response = requests.get('http://quotes.toscrape.com/')
    html_data = BeautifulSoup(response.text)
    quotes = html_data.find_all(class_='quote')


    for quote in quotes:
        quote.find(class_='text').get_text()
        quote.find(class_='author').get_text()
        quote.find(class_='keywords')['content']

        return quotes
