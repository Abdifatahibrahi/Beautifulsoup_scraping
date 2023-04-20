import requests
from bs4 import BeautifulSoup

for i in range(1,10):
    print(f'Page {i}')
    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')

    quotes = soup.findAll('div', {'class': 'quote'})
    with open('quote3.txt', 'a', encoding='utf-8') as f:
        for quote in quotes:
            text = quote.find('span', {'class': 'text'}).text
            author = quote.find('small', {'class': 'author'}).text

            f.write(text +' by '+ author)
            f.write('\n')


