import requests
from bs4 import BeautifulSoup

# Retrieve All Pokemon Names
url="https://pokeapi.co/api/v2/pokemon/?limit=807?"
r=requests.get(url)
data=r.json()
# Storing Names
pokemonNames=[]
for i in data['results']:
    pokemonNames.append(i['name'])
pokemonImagePageUrls=[]
id=1
# Generating URLs
for i in pokemonNames:
    name=i.title().replace('-','_')
    url="https://bulbapedia.bulbagarden.net/wiki/File:"+str(id).zfill(3);+name+".png"
    pokemonImagePageUrls.append(url)
    print(name+" "+url)
    id=id+1

# Now Making requests
for url in pokemonImagePageUrls[0:2]:
    page = requests.get(url)
    print(type(page.status_code),page.status_code)
    soup=BeautifulSoup(page.content, 'html.parser')
    res=soup.find(class_='fullMedia').find(class_="internal")
    print(res['href'])

#myurls="https://bulbapedia.bulbagarden.net/wiki/File:154Meganium.png"
##mydivs = soup.findAll("div", {"class": "fullMedia"})
#links = soup.findAll("a", class_="fullMedia internal")
