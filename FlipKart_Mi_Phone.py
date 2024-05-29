import requests
from bs4 import BeautifulSoup
import pandas as pd
ph_nm = []
ph_pr = []
page_num = input('enter page number - ')
for i in range(1,int(page_num)+1):
    url = 'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=5e094f72-a401-4175-9744-b9edac4d22a1&p%5B%5D=facets.brand%255B%255D%3DMi&page='+str(i)
    req = requests.get(url)
    content = BeautifulSoup(req.content,'html.parser')
    name = content.findAll('div',{'class':'_4rR01T'})
    price = content.findAll('div',{'class':'_30jeq3 _1_WHN1'})
    print('phone in page'+str(i))
    print(len(name))
    for i in name:
        ph_nm.append(i.text)
    for i in price:
        ph_pr.append(i.text)
    data = {'phoneName':ph_nm,'phonePrice':ph_pr}
    df = pd.DataFrame(data)
    df.to_excel('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/miphone.xlsx')
print('done')