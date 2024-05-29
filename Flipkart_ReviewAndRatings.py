import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
star_ratings = []

for i in range(1,2):
    url = 'https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/double-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs+%26+Appliances_0_Double+Door&page=1'
    url_object = requests.get(url)
    web_content = BeautifulSoup(url_object.text,'lxml')

    star_rating = web_content.findAll('div', {'class': '_3LWZlK'})
    for r in star_rating:
        star_ratings.append(r.text)

df = pd.DataFrame({'ratings':star_ratings})
print(df)




    #df = pd.DataFrame({'star_ratings':star_ratings})
    #print(df)

























'''data = {}
df1 = pd.DataFrame.from_dict(data,orient='index')
df1_transpose = df1.T
df1_transpose.to_csv('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/Flipkart_Fridge.csv',index=False)
print('done')'''