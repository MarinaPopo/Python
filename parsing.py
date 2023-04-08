import requests
from bs4 import BeautifulSoup
import re
import csv


# res = requests.get('https://www.e1.ru/text/')
# print(res.content)
# print(res.text)
# header = res.find_all


def get_html(url):
    res = requests.get(url)
    return res.text


def refined(s):
    return re.sub(r"\D", "", s)


def write_csv(article):
    with open('e1.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow((article['title'], article['date'], article['views']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    news = soup.find_all('article', class_='OPHIx')

    for n in news:
        title = n.find('h2', class_='h9Jmx').text
        date = n.find('time', class_="_2DfZq").find('a').text
        views = n.find('div', class_="e0SBr").text
        article = {'title': title, "date": date, 'views': views}
        print(article)

        write_csv(article)


def main():
    url = 'https://www.e1.ru/text/'
    get_data(get_html(url))


main()
