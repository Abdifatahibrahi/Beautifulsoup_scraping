import requests

for i in range(1,11):
    url = f'https://quotes.toscrape.com/page/{i}/'
    print(i)
    res = requests.get(url)
    html = res.text

    with open('quotes.csv', 'a', encoding='utf-8') as a:
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                quote = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
                quote = quote.strip()

            if '<span>by <small class="author" itemprop="author">' in line:
                author = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '').strip()
                a.write(quote +', '+ author)
                a.write('\n')
