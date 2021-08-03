import requests
from bs4 import BeautifulSoup

#Bulunduğun bölgeyi yazmalısın
arastir = "Mars hava durumu"
url = f"https://www.google.com/search?&q={arastir}"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
update = s.find("div",class_="BNeawe").text
print(update)

