import requests
from bs4 import BeautifulSoup
import pandas as pd

nm = []
pr = []
lp = []

for i in range(1,12):
    url = "https://www.flipkart.com/q/best-laptops-under-rs-50000"
    httpobject = requests.get(url)
    content = BeautifulSoup(httpobject.text,'html.parser')

    name = content.findAll('div',{'class':'_4rR01T'})
    temp = len(name)
    price = content.findAll('div',{'class':'_30jeq3 _1_WHN1'})
    list_pr = content.findAll('div',{'class':'_3I9_wc _27UcVY'})

    for i in name:
        nm.append(i.text)
        if(len(nm) == temp):
            break
    for i in price:
        pr.append(i.text)
        if(len(pr) == len(nm)):
            break
    for i in list_pr:
        try:
            lp.append(i.text)
        except:
            lp = 0

#df = pd.DataFrame.from_dict({'name':nm,'price':pr,'list':lp},orient='index')
a = {'name':nm,'price':pr,'list':lp}
df = pd.DataFrame.from_dict(a,orient='index')
#df.to_csv('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart\Output/laptop1.csv')
df.transpose()
df.to_csv('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart\Output/laptop1.csv',header=True,encoding='utf-8')