import requests
# h2[class='ds-text-title-s ds-font-bold ds-text-typo']
url = 'https://www.espncricinfo.com/cricket-news'
res = requests.get(url)
html = res.text
print(res.text)
print(res.status_code)


for line in res.text.split('\n'):
    if "h2[class='ds-text-title-s']" in line:
        print(line)

