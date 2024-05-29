from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pandas as pd

Pr_Name = []
Pr = []
Mrp = []

url = 'https://www.flipkart.com/q/best-bt-earphones-under-2000'
data = urlopen(url)
url_read = data.read()
site_data = soup(url_read,'html.parser')
page_data = site_data.findAll('div', {'class': '_4ddWXP'})

for i in page_data:
    Product_Name = i.find('a',{'class':'s1Q9rs'}).text
    Price = i.find('div',{'class':'_30jeq3'}).text
    MRP = i.find('div',{'class':'_3I9_wc'}).text
    for j in Product_Name:
        Pr_Name.append(j)
    for j in Price:
        Pr.append(j)
    for j in MRP:
        Mrp.append(j)

    df = pd.DataFrame({'ProdName':[Pr_Name],'Price1':[Pr],'MRP1':[Mrp]})
    df.to_excel('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/FlipkartEarphone.xlsx')
print('data saved successfully')