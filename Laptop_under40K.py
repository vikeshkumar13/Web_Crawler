import requests
from bs4 import BeautifulSoup
import pandas as pd
url = requests.get('https://www.newegg.com/Touch-Screen-Monitors/SubCategory/ID-514')
web_content = BeautifulSoup(url.text,'html.parser')
print(web_content)