import requests
from bs4 import BeautifulSoup
import pandas as pd
prod_name=[]
for i in range(1,102):
    url = 'https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&fm=neo%2Fmerchandising&iid=M_ed2dc72b-a888-4880-bb1f-4d7bc2672f03_1_372UD5BXDFYS_MC.EUWLZTDCBGY3&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Electronics%7ELaptop%2BAccessories%7EMouse_EUWLZTDCBGY3&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=EUWLZTDCBGY3&page=1'
    url1 = requests.get(url)
    #print(url1.status_code)
    web_content = BeautifulSoup(url1.content,'lxml')
    name=web_content.find_all('a',{'class':'s1Q9rs'})
    for i in name:
        prod_name.append(i.text)
    #print(name)
df = pd.DataFrame({'name':prod_name})
df.to_csv('mouse.csv')
print('done')