import requests
from bs4 import BeautifulSoup
import pandas as pd

name = []

url = "https://www.flipkart.com/search?q=water+bottle&sid=upp%2C3t7&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=water+bottle%7CWater+Bottles+%26+Flasks&requestId=b76e82d9-8851-495c-8d6a-9c7407b45f6f&as-searchtext=water%20bottle"

HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

r=requests.get(url,headers=HEADERS)
soup=BeautifulSoup(r.text,'html.parser')

prod_name = soup.find_all('a',{'class':'wjcEIp'})

for i in prod_name:
    name.append(i.text)

df = pd.DataFrame({'name':name})
print(df)