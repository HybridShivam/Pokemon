import requests
import re

# Reading Line by Line
f = open('URLs.txt', 'r') 
Lines = f.readlines() 
  
count = 0
URLs=[]
# Striping the newline character 
for line in Lines: 
    URLs.append(line.strip())
f.close()

# Downloading
for url in URLs:
    try:
        id = re.search("/\d\d\d", url).group(0)
        id=id[1:]
    except AttributeError:
        id = ''
        print('An Error Occured')
    r = requests.get(url, stream=True)
    with open("downloads/"+id+".png",'wb') as file:
        for chunk in r.iter_content(chunk_size=1024):
          if chunk: 
             file.write(chunk)
