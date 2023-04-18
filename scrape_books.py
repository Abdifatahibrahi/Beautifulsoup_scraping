import csv
from requests_html import HTMLSession


for i in range(1, 20):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'

    session = HTMLSession()
    r = session.get(url)

    books = r.html.find('li.col-xs-6')

    books_file = open('books.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(books_file)
    csv_writer.writerow(['Book Title', 'Price'])

    for book in books:
        title = book.find('h3 a', first=True).attrs['title']
        price = book.find('p.price_color', first=True).text

        csv_writer.writerow([title, price])
    books_file.close()