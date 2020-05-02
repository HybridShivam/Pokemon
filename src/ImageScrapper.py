import requests
from bs4 import BeautifulSoup

# Retrieve All Pokemon Names
url="https://pokeapi.co/api/v2/pokemon/?limit=807?"
r=requests.get(url)
data=r.json()
# Storing Names
pokemonNames=[]
for i in data['results'][0:10]:
    pokemonNames.append(i['name'])
pokemonImagePageUrls=[]
id=1
# Generating URLs
for i in pokemonNames:
    name=i.title().replace('-','_')
    url="https://bulbapedia.bulbagarden.net/wiki/File:"+str(id).zfill(3)+name+".png"
    pokemonImagePageUrls.append(url)
    print(name+" "+url)
    id=id+1

# Now Making requests
# Also finding which are exceptional URLs
expectional=[]
id=0
for url in pokemonImagePageUrls[0:2]:
    page = requests.get(url)
    if(page.status_code==200):
        soup=BeautifulSoup(page.content, 'html.parser')
        res=soup.find(class_='fullMedia').find(class_="internal")
        print(res['href'])
    else:
        exceptional.append(pokemonNames[id])
print(exceptional)
#myurls="https://bulbapedia.bulbagarden.net/wiki/File:154Meganium.png"
##mydivs = soup.findAll("div", {"class": "fullMedia"})
#links = soup.findAll("a", class_="fullMedia internal")
