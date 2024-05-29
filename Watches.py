import requests
from bs4 import BeautifulSoup
import pandas as pd

prod_brand = []
name_prod = []
list_price = []
price = []

for i in range(1, 1030):
    url = 'https://www.flipkart.com/search?q=watches&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_7_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_7_0_na_na_na&as-pos=7&as-type=TRENDING&suggestionId=watches&requestId=6d2939eb-e995-40bc-ae62-bd3effb08dc2&as-backfill=on&page=1'

    url1 = requests.get(url)

    page_content = BeautifulSoup(url1.content, 'html.parser')

    with open('E:/Flipkart_Scrap_code/Flipkart/Output/HTML_Page/Flipkart_Watches.html','w',encoding='utf-8')as f:
           f.write(str(page_content))

    brand = page_content.findAll('div',{'class':'_2WkVRV'})
    name = page_content.findAll('a',{'class':'IRpwTa'})
    list_pr = page_content.findAll('div',{'class':'_3I9_wc'})
    pr = page_content.findAll('div',{'class':'_30jeq3'})

    for i in brand:
            prod_brand.append(i.text)
    for i in name:
            name_prod.append(i.text)
    for i in list_pr:
            list_price.append(i.text)
    for i in pr:
            price.append(i.text)

    data = {'brand_name':prod_brand,'name':name_prod,'list_price':list_price,'price':price}
    df = pd.DataFrame.from_dict(data, orient='index')
    new_df = df.T

    new_df.to_csv('E:/Flipkart_Scrap_code/Flipkart/Output/watches.csv')

print('data saved')
print('Page download successfully')