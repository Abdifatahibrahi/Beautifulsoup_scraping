import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
req = requests.get(url)
html = req.text

soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.findAll('tr')
for tr in trs:
    title_column = tr.find('td', {'class':'titleColumn'})
    movie_name = title_column.a.text
    movie_year = title_column.find('span').text
    title_rating = tr.find('td', {'class': 'ratingColumn'})
    movie_rating = title_rating.find('strong').text
    print(movie_name, movie_year, movie_rating)
