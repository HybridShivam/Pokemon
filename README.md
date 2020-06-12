# Pokémon Assets
<p align="center">
 
  ![Offline](https://img.shields.io/badge/PokeAPI-v2-yellowgreen)
  ![Made with](https://img.shields.io/badge/Python-3-red)
</p>

 The highest quality Pokemon images.
 
 Also it contains a smaller version of the dataset from PokeAPI for offline usage (Which I used in my web app).
 
 This repository will be available as a public host for the highest quality Pokemon Images.
 
 Sugimori Artwork to begin with.
 
 Built to serve the [PokéAPI](https://pokeapi.co/) in the future.
 
 Main source is Bulbapedia for Images.
 
 <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/006-Gigantamax.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/384-Mega.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/807.png" width=200px/>
 
# Currently Available:
 *All Forms Included*
* Upto Gen VIII (Compressed)
* Upto Gen VIII HQ (Original Quality)
* Thumbnails
* DataSet from PokeAPI : Pokemon, Pokemon-Species, Moves, Abilities etc. in CSV and JSON format.
 
# Source
 WebScrapped from: 
 [Bulbapedia](http://bulbapedia.bulbagarden.net)

# Getting Started:
**For Fetching Images:**
Generate URLs like this :
https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/001.png
https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/006-Gigantamax.png

Programmatically fetch base forms:
```
this.pokemonImageUrl = 'https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/' + 
                        this.pad(this.pokemon.id, 3) + '.png';
```
*Pad method:*
```
pad(number, length) {
    let str = '' + number;
    while (str.length < length) {
      str = '0' + str;
    }
    return str;
  }
```
*For Forms: Remember to follow Capital Casing with seperation with '-'
e.g. 254-Mega , 800-Dawn-Wings, 792-Full-Moon-Phase, 569-Gigantamax, 413-Sandy, 006-Mega-X, 025-Rock-Star etc.*

**For the python Scripts:**

Just clone the repo or download just the src files.

```
# Install Required Libraries first
python -m pip install requests
python -m pip install beautifulsoup4

# ImageScrapper.py
For Scrapping the URLs to URLs.txt and the exceptional URLs to failed.txt

# Downloader.py
For Downloading images with their id to src/downloads/***.png

# URLs.txt
Contains all the pokemon URLs

# Failed.txt
Contains all the exceptional URLs which can't be fetched due to exceptional naming in their page names like Mr. Mime's
https://bulbapedia.bulbagarden.net/wiki/File:122Mr._Mime.png
```


# Copyright Notice
Please note everything in this repository is copyrighted by the Pokémon Company and its affiliates. This repository is merely a compilation of data collected by the editors of Bulbapedia and Data from Veekun and PokeAPI.
