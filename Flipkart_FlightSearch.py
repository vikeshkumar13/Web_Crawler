import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
flight_name = []
url = 'https://www.flipkart.com/travel/flights/search?trips=BOM-VNS-30092023&travellers=3-0-0&class=e&tripType=ONE_WAY&isIntl=false&source=Search%20Form'
url1 = requests.get(url)
print(url1)

web_page = BeautifulSoup(url1.content,'lxml')
#print(web_page)

company_name = web_page.findAll('div',{'class':'_2GJTkY'})
for i in company_name:
    flight_name.append(i.text)
print(flight_name)
