from bs4 import BeautifulSoup
import requests

source=requests.get('https://www.interviewbit.com/blog/reverse-a-linked-list/')
soup=BeautifulSoup(source.text,'html.parser')
code=soup.find_all('pre', class_='EnlighterJSRAW')
print(code[-1].text)

