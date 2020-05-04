import requests
import re

# Reading Line by Line
f = open('URLs2.txt', 'r') 
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
        found = re.search('/\d\d\d', url).group(1)
    except AttributeError:
        found = ''
        print('An Error Occured)
    found=found[1:]
    file = requests.get(url, allow_redirects=True)
    open('/downloads/'+found, 'wb').write(file.content)

