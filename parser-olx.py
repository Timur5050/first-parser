from bs4 import BeautifulSoup
import requests


def parse(URL):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.60 YaBrowser/20.12.0.966 Yowser/2.5 Safari/537.36'
    }
    session = requests.Session()
    response = session.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('tr', class_='wrap')
    for item in items:
        if item.find('img', class_='fleft'):
            print(item.find('img', class_='fleft').get('alt'))
            print(item.find('img', class_='fleft').get('src'))
            print(item.find('a', class_='thumb').get('href'))


n = int(input("stranichki : "))
for i in range(n):
    URL = "https://www.olx.ua/list/q-ноутбуки/?page=" + str(i + 1)
    parse(URL)
    print("=======================================================================")
