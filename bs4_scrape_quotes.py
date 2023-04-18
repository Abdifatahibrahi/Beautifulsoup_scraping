import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

# with open('quotes2.txt', 'w') as f:
#     quotes = soup.findAll('span', {'class': 'text'})
#     for quote in quotes:
#         quote = quote.text.strip('“').strip('”')
#         f.write(f'"{quote}"')
#         f.write('\n')

authors = soup.findAll('small', {'class': 'author'})
for author in authors:
    print(author.text)