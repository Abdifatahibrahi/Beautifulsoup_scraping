from requests_html import HTMLSession

url = 'https://coreyms.com/'
session = HTMLSession()
r = session.get(url)

articles = r.html.find('article')
for article in articles:
    headline = article.find('a.entry-title-link', first=True).text
    summary = article.find('div.entry-content p', first=True).text

    try:
        vid_id = article.find('iframe.youtube-player', first=True).attrs['src']
        vid_id = vid_id.split('/')[4].split('?')[0]
        youtube_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        youtube_link = None

    print(headline)
    print(summary)
    print(youtube_link)
    print()

