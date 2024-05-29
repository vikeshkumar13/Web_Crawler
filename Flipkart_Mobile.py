import requests
from bs4 import BeautifulSoup
import pandas as pd

mobile_name = []
mobile_price =[]
mobile_list = []

for i in range(1,25):
    url = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_2_7.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp4&fm=neo%2Fmerchandising&iid=M_c9b13d32-0773-4dee-baf5-5eb450bf162e_7.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=2le1qs13i80000001687279818157&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page=1'
    url_data = requests.get(url)
    content = BeautifulSoup(url_data.text,'html.parser')

    name = content.findAll('div',{'class':'_4rR01T'})
    price = content.findAll('div',{'class':'_30jeq3 _1_WHN1'})
    list_pr = content.findAll('div',{'class':'_3I9_wc _27UcVY'})

    for i in name:
        mobile_name.append(i.text)
    for i in price:
        mobile_price.append(i.text)
    for i in list_pr:
        mobile_list.append(i.text)


    data = {'name':mobile_name,'price':mobile_price,'list_pr':mobile_list}
    df = pd.DataFrame.from_dict(data,orient='index')
    df.to_csv("C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/mobile.csv")
    df.transpose()