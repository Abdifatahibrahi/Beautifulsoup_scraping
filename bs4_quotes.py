import requests
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

quotes = soup.findAll('div', {'class': 'quote'})

for quote in quotes:
    text = quote.find('span', {'class': 'text'}).text
    author = quote.find('small', {'class': 'author'}).text

    print(f"{text} by {author} ")
