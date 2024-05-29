import requests
from bs4 import BeautifulSoup
import pandas as pd

prod_name = []
prod_price = []

for i in range(1,60):
    url_object = requests.get('https://www.flipkart.com/search?q=apple+watch&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=apple+watch%7CSmart+Watches&requestId=be899816-16db-4566-b2af-2ed6bbbf7014&as-backfill=on&page=1')
    web_data = BeautifulSoup(url_object.content,'lxml')
    name = web_data.findAll('div',{'class':'_3eWWd-'})#.text#.replace(',','')

    price = web_data.findAll('div',{'class':'_30jeq3'})#.text#.replace(',','')

    for names in name:
        prod_name.append(names.text)
    for prices in price:
        prod_price.append(prices.text)

    data = {'name':prod_name,'price':prod_price}
    df = pd.DataFrame.from_dict(data,orient='index')
    df.to_csv('E:/Flipkart_Scrap_code/Flipkart/Output/Flipkart_AppleWatch.csv')