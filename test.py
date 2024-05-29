import requests
from bs4 import BeautifulSoup
import pandas as pd
hname = []
hprice = []
for i in range(1,17):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

    target_url = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAso7AFCCXRoZS1sZW5veEgzWARobIgBAZgBMbgBF8gBDNgBAegBAfgBA4gCAagCA7gCnID0pAbAAgHSAiRiNWJmZDA0Ni00ZjQ4LTQ5YzEtYThiOC1iMWExZjllZjY2OTXYAgXgAgE&sid=153bb2d9b5b3d5a152b9364dd66031ba&aid=304142&ss=Shimla&ssne=Shimla&ssne_untouched=Shimla&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2111367&dest_type=city&checkin=2023-07-02&checkout=2023-07-04&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&selected_currency=INR&offset=400"

    resp = requests.get(target_url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    name = soup.findAll('div',{'class':'fcab3ed991 a23c043802'})
    price = soup.findAll('div',{'class':'e729ed5ab6 af8e3083b0'})

    for i in name:
        hname.append(i.text)
    for i in price:
        hprice.append(i.text)

    data = {'name':hname,'price':hprice}
    df = pd.DataFrame.from_dict(data,orient='index')
    df.to_csv('C:/Users/Administrator/Desktop/Flipkart_Scrap_code/Flipkart/Output/Booking.csv')