import requests
from bs4 import BeautifulSoup
import pandas as pd

name = []
price = []
ratings = []
list_price = []

for i in range(1,4):
    url = 'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.brand%255B%255D%3DHitachi&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_TVs+%26+Appliances_0_Hitachi&page=1'
    url = requests.get(url)
    web_content = BeautifulSoup(url.text,'html.parser')

    prod_name = web_content.findAll('div',{'class':'_4rR01T'})
    prod_price = web_content.findAll('div',{'class':'_30jeq3 _1_WHN1'})
    prod_ratings = web_content.findAll('div',{'class':'_3LWZlK'})
    prod_list = web_content.findAll('div',{'class':'_3I9_wc _27UcVY'})

    for i in prod_name:
        name.append(i.text)

    for i in prod_price:
        price.append(i.text)

    for i in prod_ratings:
        ratings.append(i.text)

    for i in prod_list:
        list_price.append(i.text)

    frame = {'prod_name':name,'prod_price':price,'prod_ratings':ratings,'prod_list':list_price}
    df = pd.DataFrame.from_dict(frame,orient='index')
    df.transpose()
    df.to_csv('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart\Output/SplitAC.csv',header=True,encoding='utf-8')