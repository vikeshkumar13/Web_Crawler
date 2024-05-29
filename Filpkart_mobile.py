import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

prod_name = []

for i in range(1, 46):
    url = 'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_6_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_6_0_na_na_na&as-pos=6&as-type=TRENDING&suggestionId=mobiles&requestId=e5ad3cf6-1555-4c44-a739-e9b655613e3a&page=' + str(
        i)
    print(url)
    re = requests.get(url)
    time.sleep(2)

    page = BeautifulSoup(re.content, 'html.parser')

    name = page.findAll('div', {'class': 'KzDlHZ'})
    for i in name:
        prod_name.append(i.text)

    df = pd.DataFrame({'name': prod_name})
    df1 = pd.DataFrame({'url': url}, index=[0])

print(df)
df.to_excel('Flipkart_mobile.xlsx')
new_df = df1.T
new_df.to_excel('url.xlsx', index=False)
print('data saved')
