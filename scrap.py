import requests
from bs4 import BeautifulSoup

KEYWORDS = ['ОС', 'CSS', 'Windows', 'Java', 'Python', '3d', 'БД', 'API']

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    print('bad request')
text = response.text
soup = BeautifulSoup(text, features="html.parser")
articles = soup.find_all('article')
for article in articles:
    preview_area_v1 = article.find_all('div', class_='article-formatted-body article-formatted-body_version-1')
    preview_area_v1 = [p.text.strip().split(' ') for p in preview_area_v1]
    preview_area_v2 = article.find_all('div', class_='article-formatted-body article-formatted-body_version-2')
    preview_area_v2 = [p.text.strip().split(' ') for p in preview_area_v2]
    for el in preview_area_v1:
        for keyword in KEYWORDS:
            if keyword in el:
                link = article.find('h2').find('a').attrs.get('href')
                title = article.find('h2').find('a').text.strip()
                date = article.find('time').attrs.get('title')
                print(f'{date} {title} https://habr.com/{link}')

    for el in preview_area_v2:
        for keyword in KEYWORDS:
            if keyword in el:
                link = article.find('h2').find('a').attrs.get('href')
                title = article.find('h2').find('a').text.strip()
                date = article.find('time').attrs.get('title')
                print(f'{date} {title} https://habr.com/{link}')