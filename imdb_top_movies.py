import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

# req = requests.get('https://www.imdb.com/title/tt0468569/', headers=header)
# print(req.status_code)
# html = req.text
# soup2 = BeautifulSoup(html, 'html.parser')
# my_div = soup2.find('div', {'class': ['sc-52d569c6-0', 'kNzJA-D']})
# my_li = my_div.findAll('li')
# movie_duration = my_li[2].text
# generes = soup2.find('div', {'class': 'ipc-chip-list__scroller'})
# m_generes = generes.findAll('span', {'class': 'ipc-chip__text'})
# movie_generes = [genere.text for genere in m_generes]
# movie_generes = ','.join(movie_generes)
#
#
#
# 'https://www.imdb.com/title/tt0468569/'


url = 'https://www.imdb.com/chart/top'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.findAll('tr')
for tr in trs:
    title_column = tr.find('td', {'class': 'titleColumn'})
    movie_name = title_column.find('a').text
    movie_id = title_column.find('a').attrs['href']
    movie_url = f'https://www.imdb.com{movie_id}'
    movie_year = title_column.find('span').text

    req = requests.get(movie_url, headers=header)
    html = req.text
    soup2 = BeautifulSoup(html, 'html.parser')
    my_div = soup2.find('div', {'class': ['sc-52d569c6-0', 'kNzJA-D']})
    my_li = my_div.findAll('li')
    movie_duration = my_li[2].text
    generes = soup2.find('div', {'class': 'ipc-chip-list__scroller'})
    m_generes = generes.findAll('span', {'class': 'ipc-chip__text'})
    movie_generes = [genere.text for genere in m_generes]
    movie_generes = ','.join(movie_generes)

    my_movie_information = {
        'movie_name': movie_name,
        'movie_year': movie_year,
        'movie_duration': movie_duration,
        'movie_generes': movie_generes
    }

    print(my_movie_information)
