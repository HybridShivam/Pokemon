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
    url="https://bulbapedia.bulbagarden.net/wiki/File:"+str(id).zfill(3)+name+".png"
    pokemonImagePageUrls.append(url)
    print(name+" "+url)
    id=id+1

# Now Making requests
# Also finding which are exceptional URLs
expectional=[]
id=0
directUrls=[]
for url in pokemonImagePageUrls:
    page = requests.get(url)
    if(page.status_code==200):
        soup=BeautifulSoup(page.content, 'html.parser')
        res=soup.find(class_='fullMedia').find(class_="internal")
        directUrls.append(res['href'])
    else:
        expectional.append(pokemonNames[id])
    id=id+1
print(expectional)

# Storing the data in a File
with open('URLs.txt', 'w') as f:
    for url in directUrls:
        f.write("%s\n" % url)
with open('Failed.txt', 'w') as f:
    for name in expectional:
        f.write("%s\n" % name)
