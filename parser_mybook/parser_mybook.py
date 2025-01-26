import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin

URL = 'https://mybook.ru'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36",
}

#1 Подключение
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#2 Получение
def get_data(html):
    bs = BS(html, features="html.parser")
    items = bs.find_all('div', class_='e4xwgl-0 iJwsmp')
    mybook_list = []
    for item in items:
        title = item.find('div', class_='e4xwgl-1 gEQwGK').get_text()
        href = item.find('a').get('href')
        absolute_href = urljoin('https://mybook.ru', href)
        mybook_list.append({'title': title, 'href': absolute_href})
    return mybook_list

#3 Преобразование
def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        mybook_list2 = []
        for page in range(1, 2):
            response = get_html('https://mybook.ru/catalog/books', params={'page': page})
            mybook_list2.extend(get_data(response.text))
        return mybook_list2
    else:
        raise Exception('Error in parsing')

# print(parsing())
