import requests
for i in range(1,11):
    print(i)
    url = f'https://quotes.toscrape.com/page/{i}/'
    res = requests.get(url)
    html = res.text
    with open('quotes.txt', 'a', encoding='utf-8') as f:
        for line in html.split("\n"):
            if '<span class="text" itemprop="text">' in line:
                quote = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>','')
                quote = quote.strip()
                f.write(quote)
                f.write("\n")