import pandas as pd
import requests
from bs4 import BeautifulSoup

name = []
price = []
ratings = []

for i in range(1,85):
    url = 'https://www.flipkart.com/search?q=mouse+wireless+mouse&sid=6bo%2Cai3%2C2ay&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mouse+wireless+mouse%7CMouse&requestId=4bf6eff5-315e-462d-b1e4-3c8ae708385d&as-backfill=on&page=1'
    url1 = requests.get(url)
    web_content = BeautifulSoup(url1.content,'html.parser')

    mouse_name = web_content.findAll('a',{'class':'s1Q9rs'})
    mouse_price = web_content.findAll('div',{'class':'_30jeq3'})
    mouse_ratings = web_content.findAll('div',{'class':'_3LWZlK'})

    for i in mouse_name:
        name.append(i.text)
    for i in mouse_price:
        price.append(i.text)
    for i in mouse_ratings:
        ratings.append(i.text)

    data = {'name':name,'price':price,'ratings':ratings}
    df = pd.DataFrame.from_dict(data, orient='index')
    new_df = df.T
    new_df.to_csv('C:/Users/vikes/Desktop/mouse_analysis/mouse.csv',index=False)
print('data saved')