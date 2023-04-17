import csv
from requests_html import HTMLSession, HTML



with open('simple.html', 'r') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()

match = html.find('#footer', first=True)
print(match)


# csv_file = open('cms_scrape2.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'youtube_link'])
#
# url = 'https://coreyms.com/'
# session = HTMLSession()
# r = session.get(url)
#
# articles = r.html.find('article')
#
# for article in articles:
#     title = article.find('a.entry-title-link', first=True).text
#     summary = article.find('div.entry-content p', first=True).text
#     try:
#         vd_id = article.find('iframe.youtube-player', first=True).attrs['src']
#         vd_id= vd_id.split('/')[4].split('?')[0]
#         yt_link = f'https://youtube.com/watch?v={vd_id}'
#     except Exception as e:
#         yt_link = None
#     print(title)
#     print(summary)
#     print(yt_link)
#
#     csv_writer.writerow([title, summary, yt_link])
#
# csv_file.close()