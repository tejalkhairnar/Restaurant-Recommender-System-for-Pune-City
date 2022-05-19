from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import pandas as pd

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path = r'C:\Users\tejal\Downloads\geckodriver.exe')

#URL = 'https://www.swiggy.com/pune'
URL = 'https://www.swiggy.com/pune/kondhwa-restaurants?page=6'
driver.get(URL)

html=driver.page_source

soup=BeautifulSoup(html, 'lxml')

data1=[]
data2=[]
data3=[]
data4=[]
data5=[]

res_name=soup.find_all('div',attrs={'class':'nA6kb'})

for res_name in soup.find_all('div',attrs={'class':'nA6kb'}):
    print(res_name.text)
    data1.append(res_name.text)

for res_type in soup.find_all('div',attrs={'class':'_1gURR'}):
    print(res_type.text)
    data2.append(res_type.text)

for res_rating in soup.find_all('div',attrs={'class':'_9uwBC wY0my'}):
     print(res_rating.text)
     data3.append(res_rating.text)

for res_time in soup.find_all('div',attrs={'class':'_3Mn31'}):
    print(res_time.text[4:11])
    data4.append(res_time.text[4:11])

for res_amount in soup.find_all('div',attrs={'class':'nVWSi'}):
    print(res_amount.text)
    data5.append(res_amount.text)

while len(data2) < len(data1):
    data2.append("0")
while len(data3) < len(data1):
    data3.append("0")
while len(data4) < len(data1):
    data4.append("0")
while len(data5) < len(data1):
    data5.append("0")

df=pd.DataFrame({'Restaurant':data1, 'Type':data2, 'Rating':data3, 'Delivery Time':data4, 'Amount':data5})
writer = pd.ExcelWriter('new1.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

writer.save()