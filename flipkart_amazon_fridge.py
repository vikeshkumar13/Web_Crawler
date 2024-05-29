import requests
from bs4 import BeautifulSoup
import pandas as pd

name = []
price = []


def flipkart():
    url = 'https://www.flipkart.com/search?q=fridge&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/121.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'})
    req = requests.get(url, headers=HEADERS)
    web_page = BeautifulSoup(req.content, 'html.parser')
    prod_name = web_page.find_all('div', {'class': 'KzDlHZ'})
    prod_price = web_page.find_all('div', {'class': 'Nx9bqj _4b5DiR'})
    for i in prod_name:
        name.append(i.text)
    for i in prod_price:
        price.append(i.text)

    data = {'name': name, 'price': price}
    df = pd.DataFrame.from_dict(data, orient='index')
    new_df = df.T
    new_df.to_excel('flipkart.xlsx', sheet_name='flipkart', index=False)
    print('done')


#flipkart()


def amazon():
    name1 = []
    price1 = []
    url = 'https://www.amazon.in/s?k=firdge&crid=3BDNUF8U9VSCS&sprefix=firdge%2Caps%2C245&ref=nb_sb_noss_2'
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/121.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'})
    req = requests.get(url, headers=HEADERS)
    web_page = BeautifulSoup(req.content, 'html.parser')
    prod_name = web_page.find_all('h2', {'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})
    prod_price = web_page.find_all('span', {'class': 'a-price-whole'})
    for i in prod_name:
        name1.append(i.text)
    for i in prod_price:
        price1.append(i.text)

    data = {'name': name1, 'price': price1}
    df = pd.DataFrame.from_dict(data, orient='index')
    new_df = df.T
    new_df.to_excel('amazon.xlsx', sheet_name='amazon', index=False)
    print('done')


#amazon()


def copy_data():
    flipkart_df = pd.read_excel('flipkart.xlsx')
    amazon_df = pd.read_excel('amazon.xlsx')

    frames = [flipkart_df, amazon_df]
    result = pd.concat(frames)
    result.to_excel('data.xlsx', index=False)


copy_data()
