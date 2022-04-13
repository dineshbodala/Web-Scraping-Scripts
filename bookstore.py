from bs4 import BeautifulSoup
import requests
from word2number import w2n
source=requests.get('http://books.toscrape.com/')
soup=BeautifulSoup(source.text,'html.parser')
books=soup.find('section').find_all('li')
i=0
for book in books:
    try:
        name=book.find('h3').a.text
        i+=1
        price=book.find('p', class_='price_color').text
        rating=str(book.find('p')).split(' ')
        rating=rating[2]
        x=rating.index('"')
        r=res = w2n.word_to_num(rating[:x])
        print(i,name,r,price)
    except:
        pass
