import requests
from bs4 import BeautifulSoup
import pandas as pd
data={'title': [], 'price': [], 'links': []}
for i in range(1,21):
    URL = f'https://www.amazon.in/s?k=iphone&page={i}'

    HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

    r=requests.get(URL,headers=HEADERS)
    soup=BeautifulSoup(r.content,'html.parser')
    spans=soup.select('span.a-size-medium.a-color-base.a-text-normal')
    prices=soup.select('span.a-price')
    prod_links=soup.findAll('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

    for i in spans:
        data['title'].append(i.string)
    for i in prices:
        if not ('a-text-price' in i.get('class')):
            data['price'].append(i.find('span').get_text())
            if len(data['price']) == len(data['title']):
                break
    for i in prod_links:
        data['links'].append(i.string)
        print(data['links'])

    df=pd.DataFrame.from_dict(data, orient='index')
    new_df=df.T
    new_df.to_csv('codewithharry.csv', index=False)
print('Successfully Scraped')