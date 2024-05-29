import requests
from bs4 import BeautifulSoup
import pandas as pd
pro_name = []
for i in range(1,10):
    url = 'https://www.flipkart.com/search?q=oneplus+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=oneplus+mobile%7CMobiles&requestId=4675d677-f7d1-4e1d-9a76-bd6d27327aaa&as-backfill=on&page=1'
    url1 = requests.get(url)
    print(url1.status_code)
    web_content = BeautifulSoup(url1.content,'lxml')
    #print(web_content)
    product_name = web_content.find_all('div',{'class':'_4rR01T'})
    #print(product_name)
    for i in product_name:
        pro_name.append(i.text)
    #print(pro_name)
    #print(len(pro_name))
df1 = pd.DataFrame({'name':pro_name})
    #print(df1)
df1.to_html('flipkart_Mobile.html')
print('done')