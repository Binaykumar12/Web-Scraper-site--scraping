import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/"
r= requests.get(url)
# print(r)

soup= BeautifulSoup(r.text,"lxml")
print(soup)