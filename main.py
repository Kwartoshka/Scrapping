import requests
import re
from bs4 import BeautifulSoup
from datetime import date, timedelta

if __name__ == '__main__':

    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'php', 'id']
    KEYWORDS = set(KEYWORDS)
    nice_articles = []
    url = 'https://habr.com/ru/all/'
    result = requests.get(url)
    page = BeautifulSoup(result.text, 'html.parser')
    articles = page.find_all('article')
    for article in articles:
        res = (article.text.strip().lower())
        check = set(re.findall(r'[а-яёА-ЯЁa-zA-Z]+', res))
        if bool(check & KEYWORDS):
            url = article.find(class_="post__title_link")
            href =  url.attrs.get('href')
            title = url.text
            day = article.find(class_="post__time").text
            if 'сегодня' in day:
                day = date.today()
            elif 'вчера' in day:
                minus = timedelta(days=1)
                day = date.today() - minus
            string = f'{day} - {title} - {href}'
            nice_articles.append(string)




