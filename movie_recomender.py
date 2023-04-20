import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


needed_movie = input('Enter the movie name? ')
req = requests.get('https://www.imdb.com/chart/top/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.findAll('tr')
movies = []
for tr in trs:
    title_column = tr.find('td', {'class': 'titleColumn'})
    movie_name = title_column.find('a').text
    movie_id= title_column.find('a').attrs['href']
    if movie_name == needed_movie:
        print(movie_name)
        movie_link = f'https://www.imdb.com/{movie_id}'
        req = requests.get(movie_link, headers=header)

        html = req.text
        soup2 = BeautifulSoup(html, 'html.parser')
        my_div = soup2.find('div', {'class': ['sc-52d569c6-3', 'jBXsRT']})
        my_div2 = my_div.find('div', {'class': 'ipc-metadata-list-item__content-container'})
        direc_link = my_div2.find('a').attrs['href']
        direct_link = f'https://www.imdb.com{direc_link}'
        direct_name = my_div2.find('a').text

        req = requests.get(direct_link, headers=header)
        html = req.text
        soup3 = BeautifulSoup(html, 'html.parser')
        # my_d = soup3.find('div', {'data-testid': 'shoveler-items-container'})
        my_dd = soup3.findAll('div', {'class': 'ipc-primary-image-list-card__content-top'})
        director_movies = []
        for mov in my_dd:
            direct_movies = mov.find('a').text
            director_movies.append(direct_movies)
        print(f'The director favourite movies are {director_movies}')







