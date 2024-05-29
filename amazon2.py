import requests
from bs4 import BeautifulSoup
import pandas as pd
HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko)'
                    'Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}
url = 'https://www.amazon.in/s?k=laptop&page=2&crid=2DP11MBS7KNTH&qid=1696436438&sprefix=lap%2Caps%2C268&ref=sr_pg_1'
req = requests.get(url)
