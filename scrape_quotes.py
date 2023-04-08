import requests
url = 'https://quotes.toscrape.com/'

res = requests.get(url)
print(res.status_code)
html = res.text

with open('quotes.txt', 'w') as f:
    for line in html.split("\n"):
        if '<span class="text" itemprop="text">' in line:
            quote = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>','')
            quote = quote.strip()
            f.write(quote)
            f.write("\n")