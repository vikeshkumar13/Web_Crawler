'''with open('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/HTML_Page/Flipkart_Fridge.html','w',encoding='utf-8')as f:
    f.write(str(web_content))'''
# print(url_object.status_code)

import requests
from bs4 import BeautifulSoup
import pandas as pd

f_name = []
f_price = []
f_lPrice = []
star_ratings = []
f_ratings_Reviews = []

for i in range(1,18):
    url = 'https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/double-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs+%26+Appliances_0_Double+Door&page=1'
    url_object = requests.get(url)

    web_content = BeautifulSoup(url_object.text,'lxml')
    with open('E:/Flipkart_Scrap_code/Flipkart/Output/HTML_Page/Flipkart_Fridge.html','w',encoding='utf-8')as f:
        f.write(str(web_content))

    name = web_content.findAll('div',{'class':'_4rR01T'})
    for n in name:
        f_name.append(n.text)

    price = web_content.findAll('div',{'class':'_30jeq3 _1_WHN1'})
    for p in price:
        f_price.append(p.text)

    list_price = web_content.findAll('div',{'class':'_3I9_wc _27UcVY'})
    for lp in list_price:
        f_lPrice.append(lp.text)

    star_rating = web_content.findAll('div', {'class': '_3LWZlK'})
    for r in star_rating:
        try:
            star_ratings.append(r.text)
        except:
            star_ratings = 0

    Rating = web_content.findAll('span', {'class': '_2_R_DZ'})
    for i in Rating:
        try:
            f_ratings_Reviews.append(i.text)
        except:
            f_ratings_Reviews = 0

data = {'name':f_name,'price':f_price,'list_price':f_lPrice,'star_ratings':star_ratings,'ratings_reviews':f_ratings_Reviews}
df1 = pd.DataFrame.from_dict(data,orient='index')
df1_transpose = df1.T
df1_transpose.to_csv('E:/Flipkart_Scrap_code/Flipkart/Output/Flipkart_Fridge_new.csv',index=False)
print('done')