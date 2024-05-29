'''with open('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/HTML_Page/Flipkart_Sneakers.html','w',encoding='utf-8')as f:
    f.write(r.text)'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

mobile_name = []
mobile_price = []
mobile_review = []
mobile_mrp = []

for i in range(1,21):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    web_page = requests.get('https://www.amazon.in/s?k=phone+under+10000&page=4&crid=3ND09XXTF14L1&qid=1687802285&sprefix=phone%2Caps%2C315&ref=sr_pg_1',headers=headers).text
    soup = BeautifulSoup(web_page,'lxml')

    names = soup.findAll('span',{'class':'a-size-medium a-color-base a-text-normal'})
    prices = soup.findAll('span',{'class':'a-price-whole'})
    reviews = soup.findAll('span',{'class':'a-size-base s-underline-text'})
    mrps = soup.findAll('span', {'class': 'a-offscreen'})

    for name in names:
        mobile_name.append(name.text)
    for price in prices:
        mobile_price.append(price.text)
    for review in reviews:
        mobile_review.append(review.text)
    for mrp in mrps:
        mobile_mrp.append(mrp.text)

    data = {'name':mobile_name,'price':mobile_price,'revewies':mobile_review,'MRP':mobile_mrp}
    df = pd.DataFrame.from_dict(data,orient='index')
    #df.to_csv('E:/Flipkart_Scrap_code/Flipkart/Output/Amazon_mobile.csv')
    print(df)
print('Data saved successfully')
