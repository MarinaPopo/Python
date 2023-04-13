import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        news = self.html.find_all('article', class_='OPHIx')
        for item in news:
            title = item.find('h2', class_='h9Jmx').text
            href = item.find('a').get('href')
            views = item.find('div', class_="e0SBr").text.strip()

            self.res.append({
                'title': title,
                'href': href,
                'views': views
            })


    def run(self):
        self.get_html()
        self.parsing()
        self.save()

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(f'Новость № {i}\n\nНазвание: {item["title"]}'
                        f'\nСсылка: {item["href"]}\nПросмотры: {item["views"]}'
                        f'\n\n{"*" * 20}\n')
                i += 1


pars = Parser("https://www.e1.ru/text/", "news_e1.txt")
pars.run()