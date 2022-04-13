from bs4 import BeautifulSoup
import requests

source=requests.get('https://www.imdb.com/chart/top/')
soup=BeautifulSoup(source.text,'html.parser')
smovies=soup.find_all('td',class_='titleColumn')
for i in smovies:
    i=i.get_text()
    print(i)


    

