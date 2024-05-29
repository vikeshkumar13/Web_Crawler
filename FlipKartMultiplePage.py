import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_Name = []
Price = []
Description = []
Reviews = []

url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page=1"
r = requests.get(url)

soup=BeautifulSoup(r.text,'lxml')
box = soup.find('div',class_="_1YokD2 _3Mn1Gg")
#names = soup.findAll('div',{'class':'_4rR01T'})
names = box.findAll('div',class_="_4rR01T")
for i in names:
    name = i.text
    Product_Name.append(name)
    #print(len(Product_Name))
    #print(Product_Name)
prices = box.findAll('div',class_="_30jeq3 _1_WHN1")
for i in prices:
    name = i.text
    Price.append(name)
#print(Price)
desc = box.findAll('ul',class_="_1xgFaf")
for i in desc:
    name = i.text
    Description.append(name)
#print(Description)
reviews = box.findAll('div',class_="_3LWZlK")
for i in reviews:
    name = i.text
    Reviews.append(name)
#print(len(Reviews))

df = pd.DataFrame({"Product Name":Product_Name,"Prices":Price,"Desc":Description,"Reviews":Reviews})
df.to_csv("C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/MultipageFlipkart.csv")