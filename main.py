import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/"
r= requests.get(url)
# print(r)

soup= BeautifulSoup(r.text,"lxml")
# print(soup)

title=soup.find_all("h2",class_="featurette-heading")
# print(title)
for i in title:
    print(i.text)

heading=soup.find_all("p",class_="lead")
print(heading)