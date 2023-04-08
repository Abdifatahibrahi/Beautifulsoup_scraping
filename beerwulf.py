from requests_html import HTMLSession

url = 'https://www.beerwulf.com/en-gb'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)
products = r.html.xpath('/html/body/div[1]/div/div[7]/div/div/div/div', first=True)
print(products.absolute_links)
