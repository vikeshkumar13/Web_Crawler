import requests
from bs4 import BeautifulSoup
import pandas as pd
brand_name = []
pr = []

url = 'https://www.flipkart.com/mens-formal-shirts/pr?sid=clo%2Cash%2Caxc%2Cmmk%2Cbk1&fm=neo%2Fmerchandising&iid=M_d9de97b4-23dd-47b2-b65d-73eeb55a2788_1_372UD5BXDFYS_MC.V795R35ST9K6&otracker=hp_rich_navigation_4_1.navigationCard.RICH_NAVIGATION_Fashion%7EMen%2527s%2BTop%2BWear%7EMen%2527s%2BFormal%2BShirts_V795R35ST9K6&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L2_view-all&cid=V795R35ST9K6&page=1'

url1 = requests.get(url)
content1 = BeautifulSoup(url1.content,'lxml')

bname = content1.findAll('div',{'class':'_2WkVRV'})
price = content1.findAll('div',{'class':'_30jeq3'})

for i in bname:
    brand_name.append(i.text)
for i in price:
    pr.append(i.text)
    if len(brand_name) == len(pr):
        break
df = pd.DataFrame({'name':brand_name,'price':pr})
print(df)
