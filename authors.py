import requests

url = 'https://quotes.toscrape.com/'

res = requests.get(url)
html = res.text

with open('author.txt', 'w') as a:
    for line in html.split('\n'):
        if '<span>by <small class="author" itemprop="author">'in line:
            author = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '').strip()
            a.write(author)
            a.write('\n')