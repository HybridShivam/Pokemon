# Pokémon
 The highest quality Pokemon images.
 
 Also it contains a smaller version of the data from PokeAPI for offline usage (Which I used in my web app).
 
 This repository will be available as a public host for the highest quality Pokemon Images.
 
 Sugimori Artwork to begin with.
 
 Built to serve the [PokéAPI](https://pokeapi.co/) in the future.
 
 Main source is Bulbapedia.
 
 ![Pokémon](https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/006-Gigantamax.png)
 
 
# Currently Available:
 *All Forms Included*
* Upto Gen VIII (Compressed)
* Upto Gen VIII HQ (Original Quality)
* Pokemon, Pokemon-Species, Moves, Abilities etc.

*Technically speaking, The scripts can be used to download all the images of Pokémons who are listed in the PokéApi and Bulbapedia has the image.[ Except for a few Pokemon with exceptional names ]*
 
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

# Contribute
**Now I have switched to webscraping the image URLs.**

**URLs.txt contains all the Bulbapedia URLs scrapped.**

**But you Can still contribute in any form you feel like.**

**Like Rescaling the images for various purposes e.g. Thumbnails.**

*Guidelines:*
 * All Pokemon names must be renamed to their national dex no. and with appropriate formatting to facilitate easy access.
 * Please ensure that the quality requirements for the section are met.
 * You can add other assets as well but be sure to stick to the quality.

*Thanks for your valuable contribution.*

# Copyright Notice
Please note everything in this repository is copyrighted by the Pokémon Company and its affiliates. This repository is merely a compilation of data collected by the editors of Bulbapedia.
