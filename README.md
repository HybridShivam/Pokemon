# Pokémon Assets
<p align="center">
 
  ![Offline](https://img.shields.io/badge/PokeAPI-v2-yellowgreen)
  ![Made with](https://img.shields.io/badge/Python-3-red)
</p>

 The highest quality Pokemon images.
 
 Also it contains a smaller version of the dataset from PokeAPI for offline usage (Which I used in my web app).
 
 This repository will be available as a public host for the highest quality Pokemon Images, specifically the Official Sugimori Artwork.
 
 Built to work alongside the [PokéAPI](https://pokeapi.co/).
 
 Main source is Bulbapedia for Images.
 
 <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/006-Gmax.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/384-Mega.png" width=200px/> <img src="https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/807.png" width=200px/>
 
# Currently Available:
 *All Forms Included*
* Hisuian Forms
* Upto Gen VIII (Compressed)
* Upto Gen VIII HQ (Original Quality)
* Thumbnails
* DataSet from PokeAPI : Pokemon, Pokemon-Species, Moves, Abilities etc. in CSV and JSON format.

# Source
 WebScrapped from: 
 [Bulbapedia](http://bulbapedia.bulbagarden.net)


# Getting Started:

## A. Directly Fetching Images from this Repository:
<br>

Fetch base forms:
```
SpeciesID.png (padded 000)
```
https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/001.png

For Alternate Forms: 

```
SpeciesID-FormName.png
```
https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/006-Gmax.png
https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/254-Mega.png

Get the SpeciesID and Form-Name from PokeAPI and remember to follow Capital Casing with '-' delimiter.<br>
e.g. 254-Mega , 800-Dawn, 569-Gmax, 413-Sandy, 006-Mega-X, 025-Rock-Star etc.*

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
Please note everything in this repository is copyrighted by the Pokémon Company and its affiliates. This repository is merely a compilation of data collected by the editors of Bulbapedia and Data from Veekun and PokeAPI.
