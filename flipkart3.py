import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
httpObject = urlopen("https://www.flipkart.com/q/best-laptops-under-rs-50000")
webdata = httpObject.read()
soupdata = soup(webdata,'lxml')
containers = soupdata.findAll('div',{'class':'_2kHMtA'})
f = open('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/laptops_info.csv','wb')
f.write('product_name,Ratings,Current_price,MRP\n'.encode())
for container in containers:
    #product = container.findAll('div',{'class':'_4rR01T'})
    #print(product[0].text.split('-')[0])
    
    product = container.find('div', {'class': '_4rR01T'})
    product_name = product.text.split('-')[0].strip()
    stars = container.find('div',{'class':'_3LWZlK'})
    try:
        Star = stars.text
    except:
        Star = 0
    Ratings = container.find('span',{'class':'_2_R_DZ'})
    try:
        ratRev = re.findall('\d+,?\d*',Ratings.text)
        Ratings = ratRev[0]
        Reviews = ratRev[1]
    except:
        Ratings = 0
        Reviews = 0

    Current_price = container.find('div',{'class':'_30jeq3 _1_WHN1'}).text.replace(',','')

    mrp = container.find('div',{'class':'_3I9_wc _27UcVY'})
    try:
        MRP = mrp.text.replace(',','')
    except:
        MRP = 0
    f.write(f"{product_name},{Ratings},{Current_price},{MRP}".encode())
f.close()