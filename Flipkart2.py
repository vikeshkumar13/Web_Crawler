import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

httpobject = urlopen("https://www.flipkart.com/q/best-laptops-under-rs-50000")
webdata = httpobject.read()

soupdata = BeautifulSoup(webdata,'html.parser')
containers = soupdata.findAll('div',{'class':'_2kHMtA'})

for container in containers:
    productName = container.find('div',{'class':'_4rR01T'})
    star = container.find('div',{'class':'_3LWZlK'})
    try:
        stars = star.text
    except:
        stars = 0
    list_price = container.find('div',{'class':'_3I9_wc _27UcVY'})
    try:
        lp = list_price.text
    except:
        lp = 0

    df = pd.DataFrame({'name':productName,'star':stars,'listprice':lp}, index=[0])
    #print(df)
    df.to_csv('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/Flipkart_Laptops.csv',index=False)


