from bs4 import BeautifulSoup
import requests
source=requests.get('https://webscraper.io/test-sites/tables')
soup=BeautifulSoup(source.text,'html.parser')
index=0
data=soup.find('div', class_='wrapper').find_all('td')
for units in range(0,len(data)-3,4):
    index+=1
    name=data[units+1].text
    lname=data[units+2].text
    id=data[units+3].text
    print(index,name,lname,id)
