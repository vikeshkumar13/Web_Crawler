import requests
from bs4 import BeautifulSoup
import pandas as pd

mobile_name = []
mobile_price = []
mobile_review = []
mobile_mrp = []

for i in range(1,21):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    web_page = requests.get('https://www.amazon.in/s?k=iphone+14&page=2&qid=1688387053&sprefix=ip%2Caps%2C229&ref=sr_pg_1',headers=headers).text
    soup = BeautifulSoup(web_page,'lxml')

    names = soup.findAll('span',{'class':'a-size-medium a-color-base a-text-normal'})
    '''prices = soup.findAll('span',{'class':'a-price-whole'})
    reviews = soup.findAll('span',{'class':'a-size-base s-underline-text'})
    mrps = soup.findAll('span', {'class': 'a-offscreen'})'''

    for name in names:
        mobile_name.append(name.text)
    '''for price in prices:
        mobile_price.append(price.text)
    for review in reviews:
        mobile_review.append(review.text)
    for mrp in mrps:
        mobile_mrp.append(mrp.text)'''

    #data = {'name':mobile_name,'price':mobile_price,'revewies':mobile_review,'MRP':mobile_mrp}
    data = {'name': mobile_name}
    df1 = pd.DataFrame.from_dict(data, orient='index')
    df1_transpose = df1.T

    df1_transpose.to_csv('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/Iphone14.csv')
#print('Data saved successfully')