from bs4 import BeautifulSoup
import requests

source=requests.get('https://www.imdb.com/chart/top/')
soup=BeautifulSoup(source.text,'html.parser')
smovies=soup.find('tbody',class_='lister-list').find_all('tr')
for i in smovies:
    name=i.find('td', class_='titleColumn').a.text
    rank=i.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
    rating=i.find('td', class_='ratingColumn imdbRating').strong.text
    print(rank,name,rating)
    



    

