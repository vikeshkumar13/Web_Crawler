import requests
from bs4 import BeautifulSoup
import pandas as pd
doctor_name = []
dept = []
url = 'https://www.maxhealthcare.in/find-a-doctor'
requests1 = requests.get(url)
All_page = BeautifulSoup(requests1.content, 'lxml')
name = All_page.findAll('h4',{'class':'font-weight-semi-bold'})
department = All_page.findAll('p',{'class':'text-truncate-line-3'})
for i in name:
    doctor_name.append(i.text)
for i in department:
    dept.append(i.text)

df = pd.DataFrame({'name':doctor_name, 'department':dept})
df.to_csv('Max_doctor.csv')