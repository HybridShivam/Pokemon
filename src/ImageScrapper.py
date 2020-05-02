import requests
from bs4 import BeautifulSoup


url="https://pokeapi.co/api/v2/pokemon/?limit=807?"
r=requests.get(url)
data=r.json()
pokemonNames=[]
for i in data['results']:
    pokemonNames.append(i['name'])
pokemonImagePageUrls=[]
for i in pokemonNames:
    pokemonImagePageUrls.append(i)
    print(i)
'''
myurls="https://bulbapedia.bulbagarden.net/wiki/File:154Meganium.png"


page = requests.get("https://bulbapedia.bulbagarden.net/wiki/File:154Meganium.png")
soup=BeautifulSoup(page.content, 'html.parser')
#mydivs = soup.findAll("div", {"class": "fullMedia"})
#links = soup.findAll("a", class_="fullMedia internal")
res=soup.find(class_='fullMedia').find(class_="internal")
print(res['href'])
'''
