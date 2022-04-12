from bs4 import BeautifulSoup
import requests

source=requests.get('https://www.imdb.com/chart/top/')
soup=BeautifulSoup(source.text,'html.parser')

print(soup)
