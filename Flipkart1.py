import requests
from bs4 import BeautifulSoup
import pandas as pd

nm = []
pr = []
rt = []
ram = []

for i in range(1,24):
    url = 'https://www.flipkart.com/search?q=redmi+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=redmi+mobile%7CMobiles&requestId=fc1f3633-a88c-4e4c-ab94-a8ae65569a4a&as-backfill=on&page=1'
    req = requests.get(url)
    content = BeautifulSoup(req.content,'html.parser')

    name = content.find_all('div',class_='_4rR01T')
    price = content.find_all('div',{'class':'_30jeq3 _1_WHN1'})
    ratings = content.find_all('div',{'class':'_3LWZlK'})
    RAM = content.findAll('li',{'class':'rgWa7D'})

    for i in name:
        nm.append(i.text)

    for i in price:
        pr.append(i.text)
        if(len(pr) == len(nm)):
            break

    for i in range(len(ratings)):
        rt.append(ratings[i].text)
        if(len(rt) == len(nm)):
            break

    for i in range(len(nm)):
        ram.append(RAM[i].text)
        if(len(ram) == len(pr)):
            break

data = {'name':nm,'price':pr,'ratings':rt,'Desc':ram}
df = pd.DataFrame(data)
df.to_csv('E:/Flipkart_Scrap_code/Flipkart/Output/RedmiMobile.csv',index=False)
print(' Data Saved ')