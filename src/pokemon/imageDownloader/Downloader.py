import requests
import re
import os.path
from pathlib import Path

FILE_PATH = "URLs/URLs.txt"

# This script will download all files from the URLs/URLs.txt and put them in Downloads directory
downloadDir = "downloads/"


def Download(FileName, response, url):
    # If the downloads folder does not exist, it is created
    if not Path(downloadDir).exists():
        Path(downloadDir).mkdir()

    with open(FileName, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
        print("Downloaded: " + url)


def get_urls(file_path: str):
    f = open(file_path, "r")
    Lines = f.readlines()
    URLs = []
    for line in Lines:
        URLs.append(line.strip())  # Stripping the newline character
    f.close()
    return URLs


def main():
    while True:
        option = input("Re download All files ?(Y,N): ")
        if option in ["Y", "y"]:
            ReDownloadOnlyCorruptedFiles = False
            break
        if option in ["N", "n"]:
            ReDownloadOnlyCorruptedFiles = True
            # Re-download only corrupted files (sometimes <1kb corrupted files are downloaded from Bulbapedia)
            print("Only new/ corrupted files will be downloaded")
            break

    URLs = get_urls(FILE_PATH)
    # Downloading
    for url in URLs:
        try:
            pokemon_id = re.search(r"/\d\d\d\d", url).group(0)
            pokemon_id = pokemon_id[1:]
            fileToDownload = downloadDir + pokemon_id + ".png"
            response = requests.get(url, stream=True)
            if not ReDownloadOnlyCorruptedFiles:
                Download(
                    fileToDownload, response, url
                )  # (Re-)Download all files unconditionally
            elif os.path.exists(fileToDownload):
                file_stat = os.stat(fileToDownload)
                if file_stat.st_size < 1000:
                    Download(fileToDownload)  # Re-download only corrupted files
            else:
                Download(fileToDownload)  # Download new file
        except AttributeError:
            print("An Error Occured for: " + pokemon_id)


if __name__ == "__main__":
    main()
