import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

httpObject = urlopen('https://www.flipkart.com/q/best-laptops-under-rs-50000')
webdata = httpObject.read()
soupdata = soup(webdata,'html.parser')

containers = soupdata.findAll('div',{'class':'_2kHMtA'})

for container in containers:
    product = container.find('div',{'class':'_4rR01T'})
    productName = product.text.split('-')[0].strip()

    star = container.find('div', {'class': '_3LWZlK'})
    try:
        stars = star.text
    except:
        stars = 0

    Rating = container.find('span',{'class':'_2_R_DZ'})
    try:
        ratRev = re.findall('\d+,?\d*', Rating.text)
        Ratings = ratRev[0].replace(',','')
        Reviews = ratRev[1].replace(',','')
    except:
        Ratings = 0
        Reviews = 0
    CurrentPrice = container.find('div',{'class':'_30jeq3 _1_WHN1'}).text.replace(',',' ')

    mrp = container.find('div',{'class':'_3I9_wc _27UcVY'})
    try:
        MRP = mrp.text.replace(',','')
    except:
        MRP = 0

    info = container.findAll('li',{'class':'rgWa7D'})
    Processor = info[0].text
    RAM = info[1].text
    Storage = info[3].text
    Image = container.img
    ImageURL = Image.get('src')
    print(productName,stars,Ratings,Reviews,CurrentPrice,MRP,Processor,RAM,Storage,ImageURL)
    print('\n')