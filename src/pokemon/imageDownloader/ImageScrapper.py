import requests
from bs4 import BeautifulSoup

# Scrapes Image URLs from Bulbapedia

# Retrieve All Pokemon Names
url = "https://pokeapi.co/api/v2/pokemon/?limit=1025?"
r = requests.get(url)
data = r.json()
# Storing Names
pokemonNames = []
for i in data["results"]:
    pokemonNames.append(i["name"])
pokemonImagePageUrls = []

exceptionalPokemonNames = {
    29: "Nidoran",
    32: "Nidoran",
    83: "Farfetch%27d",
    122: "Mr._Mime",
    250: "Ho-Oh",
    386: "Deoxys",
    413: "Wormadam-Plant",
    474: "Porygon-Z",
    487: "Giratina",
    492: "Shaymin",
    550: "Basculin-Red",
    555: "Darmanitan",
    641: "Tornadus",
    642: "Thundurus",
    645: "Landorus",
    647: "Keldeo",
    648: "Meloetta",
    669: "Flabébé",
    678: "Meowstic",
    681: "Aegislash-Shield",
    710: "Pumpkaboo",
    711: "Gourgeist",
    718: "Zygarde",
    741: "Oricorio",
    745: "Lycanroc",
    746: "Wishiwashi",
    774: "Minior",
    778: "Mimikyu",
    782: "Jangmo-o",
    783: "Hakamo-o",
    784: "Kommo-o",
    849: "Toxtricity-Amped",
    865: "Sirfetch'd",
    866: "Mr. Rime",
    875: "Eiscue",
    876: "Indeedee",
    877: "Morpeko-Full",
    892: "Urshifu-Single_Strike",
    902: "Basculegion",
    905: "Enamorus",
    1001: "Wo-Chien",
    1002: "Chien-Pao",
    1003: "Ting-Lu",
    1004: "Chi-Yu",
}
# Generating URLs
id = 1
for i in pokemonNames:
    if id in exceptionalPokemonNames:
        name = exceptionalPokemonNames[id]
    else:
        name = i.title().replace("-", "_")
    url = (
        "https://bulbapedia.bulbagarden.net/wiki/File:"
        + str(id).zfill(4)
        + name
        + ".png"
    )
    pokemonImagePageUrls.append(url)
    print(name + " " + url)
    id = id + 1

# Making requests to scrape the pages for direct links to the artwork
expectional = []
id = 0
directUrls = []
for url in pokemonImagePageUrls:
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        res = soup.find(class_="fullMedia").find(class_="internal")
        directUrls.append(res["href"])
    else:
        expectional.append(pokemonNames[id])
    id = id + 1
    print(
        f"Scrapping for direct links: {id}/({len(pokemonImagePageUrls)})",
        end="\r",
    )

print("\nDirect URLs:")
print(*directUrls, sep="\n")
if len(expectional) > 0:
    print("Failed to fetch:")
    print(*expectional, sep="\n")

# Storing the data in text files
with open("URLs/URLs.txt", "w") as f:
    for url in directUrls:
        f.write("%s\n" % url)
with open("ImageScrapperFailedList.txt", "w") as f:
    for name in expectional:
        f.write("%s\n" % name)
