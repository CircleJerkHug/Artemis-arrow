import requests
from bs4 import BeautifulSoup

url="https://kissanime.ru/Search/Anime/"
'''
print("Enter the name of anime\n")
name=input()
url_new=url+str(name)
print(url_new)
'''
r=requests.get(url)
print(r)