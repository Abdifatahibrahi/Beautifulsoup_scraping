from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

articles = html.find('div.article')
print(articles)
for article in articles:
    headline = article.find('h2', first=True).text
    summary = article.find('p', first=True).text

    print(headline)
    print(summary)

