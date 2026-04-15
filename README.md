# Pokémon Assets
<p align="center">
 
  ![Offline](https://img.shields.io/badge/PokeAPI-v2-yellowgreen)
  ![Made with](https://img.shields.io/badge/Python-3-red)
</p>

 The highest quality Pokemon images.
 
 Customized dataset from PokéAPI for offline usage in [PokéDex Angular App](https://github.com/HybridShivam/pokedex-angular-app).
 
 This repository will be available as a public host for the highest quality Pokemon Images, specifically the Official Sugimori Artwork.
 
 Built to work alongside the [PokéAPI](https://pokeapi.co/).
 
 Main source is Bulbapedia for Images.
 
 <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/0006-Gmax.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/0384-Mega.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/0807-Mega.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/0964-Hero.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/0718-Mega.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/1024-Terastal.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/0154-Mega.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/0652-Mega.png" width=200px/>
 
# Currently Available:
*All images except for thumbnails are available in Compressed (`assets/images/`) and Original (`assets/imagesHQ`) Quality*
* Legends ZA
* Gen I-IX
* Alternate Forms
* Regional Forms
* Mega Evolutions
* Gigantamax Forms
* All Species Thumbnails
* DataSet from PokeAPI : Pokemon, Pokemon-Species, Moves, Abilities etc. in CSV and JSON format.

# Source
 WebScrapped from: 
 [Bulbapedia](http://bulbapedia.bulbagarden.net)


# Getting Started:

## A. Directly Fetching Images from this Repository:
<br>

Fetch base forms:
```
SpeciesID.png (padded 0000)
```
https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/0001.png

For Alternate Forms: 

```
SpeciesID-FormName.png
```
https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/0006-Gmax.png
https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/0254-Mega.png

Get the SpeciesID and Form-Name from PokeAPI and remember to follow Capital Casing with '-' delimiter.<br>
e.g. 0254-Mega , 0800-Dawn, 0569-Gmax, 0413-Sandy, 0006-Mega-X, 0025-Rock-Star, 0964-Hero etc.*

Alternatively,

## B. Scrape Image URLs from Bulbapedia using the scripts:

**Just clone the repo or just download the `src` files.**

```
# Install Required Libraries first
python -m pip install requests
python -m pip install beautifulsoup4
```
<br>

**1. Fetch Image URLs using this script:**

**`src/imageDownloader/ImageScrapper.py`**

This script fetches all base form URLs to `URLs/URLs.txt` and the logs the failed attempts to `ImageScrapperFailedList.txt`

Note: `ImageScrapperFailedList.txt` Contains all the failed names which could't be fetched due to exceptional naming in their page names like Mr. Mime's
https://bulbapedia.bulbagarden.net/wiki/File:122Mr._Mime.png

<br>

**2. Downloading the Images from URLs.txt:**

**`src/imageDownloader/Downloader.py`**

Use this script for Downloading images using the URLs.txt to `downloads/id.png`
(Optional parameter `ReDownloadOnlyCorruptedFiles` to redownload only new/ corrupted files)

Note: `ExceptionalURLs.txt` and `FormURLs.txt` have been manually created, use any download manager to download using them.<br>


## C. Generating the DataSet from PokeAPI:
 1. Just clone the repo or download just the `src` files.
 1. Run `src/dataSet/generateDataSet.py` to generate the dataset.
 Note: `.csv` files are directly from the [Veekun](https://github.com/veekun/pokedex/tree/master/pokedex/data/csv) database.

# Copyright Notice
Please note that everything in this repository is copyrighted by the Pokémon Company and its affiliates. This repository is merely a compilation of data collected by the editors of Bulbapedia and Data from Veekun and PokeAPI.
