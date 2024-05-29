import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
def amazon():
    name = []
    price = []

    for i in range(1,16):
        time.sleep(3)
        url = f'https://www.amazon.in/s?k=laptop+exchange+offer+with+laptop&page={i}'
        time.sleep(3)
        HEADERS = ({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/121.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

        req = requests.get(url, headers=HEADERS)
        time.sleep(3)
        page_content = BeautifulSoup(req.content, 'html.parser')
        #print(page_content)
        box = page_content.find('div', {
            'class': 'sg-col-20-of-24 s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16'})
        prod = box.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'})
        pr = box.find_all('span', {'class': 'a-price-whole'})

        prod_length = len(prod)
        prod_price = len(pr)
        print(prod_length)
        print(prod_price)



        for i in prod:
            name.append(i.text)
                #print(name)
        for i in pr:
            price.append(i.text)

        df = pd.DataFrame.from_dict({'name': name, 'price': price}, orient='index')
        print(df.T)
        new_df = df.T
        new_df.to_excel('amazon_exchange.xlsx')


amazon()