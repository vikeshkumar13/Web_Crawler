#https://www.geeksforgeeks.org/how-to-split-explode-pandas-dataframe-string-entry-to-separate-rows/
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

prod_name = []
prod_price = []

url = 'https://www.flipkart.com/home-kitchen/home-appliances/air-coolers/pr?sid=j9e,abm,52j'
HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/121.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'})
url_request = requests.get(url, headers=HEADERS)

time.sleep(5)

full_page_content = BeautifulSoup(url_request.content, 'html.parser')

name = full_page_content.find_all('a',{'class':'wjcEIp'})
price = full_page_content.find_all('div',{'class':'hl05eU'})

for i in name:
    prod_name.append(i.text)

for j in price:
    prod_price.append(j.text)


data = {'NAME':prod_name, 'PRICE': prod_price}
df = pd.DataFrame.from_dict(data, orient='index').T
print(df.head(10))
price_column = df['PRICE'].str.split(',', expand=True)
print(price_column.head(10))

#df.to_csv('flipkart_cooler.csv', index=False)
#print('DATA SAVED SUCCESSFULLY')