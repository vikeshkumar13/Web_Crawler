import requests
from bs4 import BeautifulSoup
import pandas as pd

prod_name = []
price1 = []
for i in range(1,94):

    url = 'https://www.flipkart.com/search?q=school+shoes+boys+black+black&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'
    url_requests = requests.get(url)

    page_content = BeautifulSoup(url_requests.content,'html.parser')
    name = page_content.findAll('div',{'class':'_2WkVRV'})
    price = page_content.findAll('div',{'class':'_30jeq3'})

    for i in name:
        prod_name.append(i.text)

    for i in price:
        price1.append(i.text)

    data_column = {'name':prod_name,'price':price1}
    df = pd.DataFrame.from_dict(data_column,orient='index')
    df1 = df.T
    df1.to_csv('E:/Flipkart_Scrap_code/Flipkart/Output/shoes.csv')
print('done')