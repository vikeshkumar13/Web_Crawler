import requests
from bs4 import BeautifulSoup
import pandas as pd

product_name = []
product_price = []
for i in range(1, 2):
    url = 'https://www.flipkart.com/q/wireless-mouse?page=1'

    url_data = requests.get(url)

    content = BeautifulSoup(url_data.content, 'html.parser')

    #with open('E:/Flipkart_Scrap_code/Flipkart/Output/HTML_Page/Flipkart_Mouse.html', 'w', encoding='utf-8') as f:
     #   f.write(str(content))

    name = content.findAll('a', {'class': 's1Q9rs'})
    price = content.findAll('div', {'class': '_30jeq3'})

    for i in name:
        product_name.append(i.text)

    for i in price:
        product_price.append(i.text)
        if len(product_name) == len(product_price):
            break

    df = pd.DataFrame({'name': product_name, 'price': product_price})
    df['price'] = df['price'].str.replace(r'\W','')

    df.to_csv('E:/Flipkart_Scrap_code/Flipkart/Output/Flipkart_mouse2.csv', index=False, encoding='utf-8')
    #df.columns = df.columns.str.replace('[â‚¹]', '')

print('File Write Successfully on the above location in xlsx format & Html file also downloaded !')