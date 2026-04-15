import json
import requests as req
import math
import re
import csv

def load_version_data():
    games = {}
    gameVersions = {}
    with open('versions.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            games[row['identifier']] = int(row['id'])
    with open('version-groups.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            gameVersions[row['identifier']] = int(row['id'])
    return gameVersions, games

gameVersions, games = load_version_data()

def MachineUrlToID(url):
    return int(re.sub(r'http(s)?:\/\/pokeapi.co\/api\/v2\/machine\/(\d+)\/', '\\2', url))
def EvoChainUrlToID(url):
    return int(re.sub(r'http(s)?:\/\/pokeapi.co\/api\/v2\/evolution-chain\/(\d+)\/', '\\2', url))
def PokemonUrlToID(url):
    return int(re.sub(r'http(s)?:\/\/pokeapi.co\/api\/v2\/pokemon\/(\d+)\/', '\\2', url))
def AbilityUrlToID(url):
    return int(re.sub(r'http(s)?:\/\/pokeapi.co\/api\/v2\/ability\/(\d+)\/', '\\2', url))
def SpeciesUrlToID(url):
    return int(re.sub(r'http(s)?:\/\/pokeapi.co\/api\/v2\/pokemon-species\/(\d+)\/', '\\2', url))
def TypeUrlToID(url):
    return int(re.sub(r'http(s)?:\/\/pokeapi.co\/api\/v2\/type\/(\d+)\/', '\\2', url))


def takeInput():
    print('-----------\n')
    print('What to generate:\n0) All\n1) /pokemon/\n2) /pokemon-species/\n3) /evolution-chain/\n4) /move/\n5) /ability/\nexit) Exit the program')
    print('\n-----------')
    return input()


def gPokemon():
    print('Generating /pokemon/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/pokemon/?offset=0&limit=100000'
    print(mainURL)
    r=req.get(mainURL)
    data=r.json()
    # Storing Individual Requests
    URLs=[]
    results=dict()
    count=0
    total=len(data['results'])
    for i in data['results']:
        count=count+1
        percent=math.floor((count/total)*100)
        if(percent%2==0):
            print(str(percent)+'% ('+str(count)+'/'+str(total)+')')
        url=i['url']
        URLs.append(i['url'])
        response=req.get(url)
        data=response.json()
        DataToWrite=dict()
        DataToWrite['Ab']=[]
        for ability in data['abilities']:
            abi=dict()
            abi['n']=ability['ability']['name']
            abi['id']=AbilityUrlToID(ability['ability']['url'])
            abi['isH']=ability['is_hidden']
            DataToWrite['Ab'].append(abi)
        DataToWrite['BE']=data['base_experience']
        DataToWrite['H']=data['height']
        DataToWrite['HI']=[]
        for i in data['held_items']:
            item=dict()
            item['n']=i['item']['name']
            version_id=len(i['version_details'])-1 # Start with the latest version for the item
            while(version_id>=0):
                latestVersion=i['version_details'][version_id]
                if(latestVersion['version']['name'] !='xd'): # skip XD
                    item['%']=latestVersion['rarity']
                    break
                else:
                    version_id=version_id-1
            if('%' in item):
                DataToWrite['HI'].append(item)
        DataToWrite['id']=data['id']
        DataToWrite['isD']=data['is_default']
        DataToWrite['N']=data['name']
        DataToWrite['Sp']={'n':data['species']['name'],'id':SpeciesUrlToID(data['species']['url'])}
        DataToWrite['St']=[]
        for i in data['stats']:
            item=dict()
            item['n']=i['stat']['name']
            item['EV']=i['effort']
            item['bs']=i['base_stat']
            DataToWrite['St'].append(item)
        DataToWrite['T']=[]
        for i in data['types']:
            item=dict()
            item['n']=i['type']['name']
            item['id']=TypeUrlToID(i['type']['url'])
            DataToWrite['T'].append(item)
        DataToWrite['W']=data['weight']
        results[DataToWrite['id']]=DataToWrite
    fileName='pokemon.json'
    
    total_entries = len(results)
    # Use newline='\n' to force 1-byte LF line endings
    with open(fileName, 'w', encoding='utf-8', newline='\n') as f:
        f.write('{"pokemon":{\n')
        # results.items() will follow the API's insertion order
        for index, (p_id, p_data) in enumerate(results.items()):
            # separators=(',', ':') removes the structural whitespace
            json_line = json.dumps(p_data, separators=(',', ':'))
            line = f'"{p_id}":{json_line}'
            # Add comma and newline for all except the last entry
            if index < total_entries - 1:
                f.write(line + ',\n')
            else:
                f.write(line + '\n')
        f.write('}}')
    print(f'Done! Saved {fileName} ({total_entries} entries)')

    
def gPokemonSpecies():
    print('Generating /pokemon-species/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/pokemon-species/?&limit=1025'
    print(mainURL)
    r=req.get(mainURL)
    data=r.json()
    # Storing Individual Requests
    URLs=[]
    results=[]
    count=0
    total=len(data['results'])
    for i in data['results']:
        count=count+1
        percent=math.floor((count/total)*100)
        if(percent%2==0):
            print(str(percent)+'% ('+str(count)+'/'+str(total)+')')
        url=i['url']
        URLs.append(i['url'])
        response=req.get(url)
        data=response.json()
        DataToWrite=dict()
        evoChainID=None
        if(data['evolution_chain']!=None):
            evoChainID=EvoChainUrlToID(data['evolution_chain']['url'])
        DataToWrite['BaH']=data['base_happiness']
        DataToWrite['CaR']=data['capture_rate']
        DataToWrite['Co']=data['color']['name']
        DataToWrite['EgG']=[egg['name'] for egg in data['egg_groups']]
        DataToWrite['EvC']=evoChainID
        DataToWrite['FTE']=[]
        DataToWrite['FD']=None
        DataToWrite['FoS']=data['forms_switchable']
        DataToWrite['GeR']=data['gender_rate']
        DataToWrite['Gen']=data['generation']['name']
        DataToWrite['GrR']=data['growth_rate']['name']
        DataToWrite['GDi']=data['has_gender_differences']
        DataToWrite['HaC']=data['hatch_counter']
        DataToWrite['id']=data['id']
        DataToWrite['iB']=data['is_baby']
        DataToWrite['name']=data['name']
        DataToWrite['varieties']=[]
        for entry in data['flavor_text_entries']:
            flavor=dict()
            if(entry['language']['name']=='en'):
                flavor['v']=entry['version']['name']
                flavor['e']=entry['flavor_text']
                DataToWrite['FTE'].append(flavor)
        # Sorts the list in-place based on the integer value in gameVersions
        DataToWrite['FTE'].sort(key=lambda x: games.get(x['v'], 999))
        for entry in data['form_descriptions']:
            if(entry['language']['name']=='en'):
                DataToWrite['FD']=entry['description']
                break
        for entry in data['genera']:
            if(entry['language']['name']=='en'):
                DataToWrite['G']=entry['genus']
        for entry in data['varieties']:
            variety=dict()
            variety['isD']=entry['is_default']
            variety['n']=entry['pokemon']['name']
            variety['id']=PokemonUrlToID(entry['pokemon']['url'])
            DataToWrite['varieties'].append(variety)
        results.append(DataToWrite)
    fileName='pokemon-species.json'
    # Pre-calculate minified strings for each species
    # separators=(',', ':') removes all internal spaces
    lines = [json.dumps(species, separators=(',', ':')) for species in results]
    
    # Use newline='\n' to force 1-byte LF line endings for Windows/Git efficiency
    with open(fileName, 'w', encoding='utf-8', newline='\n') as f:
        f.write('{"pokemon-species":[\n')
        f.write(',\n'.join(lines))
        f.write('\n]}')
    print(f'Done! Saved {fileName} ({len(results)} entries)')


def gEvolutionChain():
    print('Generating /evolution-chain/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/evolution-chain/?offset=0&limit=100000'
    print(mainURL)
    r=req.get(mainURL)
    data=r.json()
    # Storing Individual Requests
    URLs=[]
    max_id = int(data['results'][-1]['url'].strip('/').split('/')[-1])
    results=[None]*(max_id) # Pre-size the list to accommodate all IDs, including any gaps
    count=0
    total=len(data['results'])
    for i in data['results']:
        count=count+1
        percent=math.floor((count/total)*100)
        if(percent%2==0):
            print(str(percent)+'% ('+str(count)+'/'+str(total)+')')
        url=i['url']
        URLs.append(i['url'])
        response=req.get(url)
        data=response.json()
        results[data['id']-1]=data
    # print(results)
    fileName='evolution-chain.json'
    processed_lines = []
    for chain in results:
        if chain is None:
            # Represents a missing ID in the array to keep indices aligned
            processed_lines.append('null')
        else:
            # 1. Minify the individual chain
            # separators=(',', ':') is vital to keep the file size down
            line = json.dumps(chain, separators=(',', ':'))
            # 2. Apply your custom Regex cleanups
            # Simply Evolution Trigger Objects to their name string
            line = re.sub(r'{"name":("[A-Za-z-]+"),"url":"https://pokeapi\.co/api/v2/evolution-trigger/\d+/"}', r'\1', line)
            # Convert Pokemon Species URLs to just their ID number
            line = re.sub(r'url":"https://pokeapi\.co/api/v2/pokemon-species/(\d+)/"', r'id":\1', line)
            processed_lines.append(line)

    # Use newline='\n' to force LF format for Windows/Git consistency
    with open(fileName, 'w', encoding='utf-8', newline='\n') as f:
        f.write('{"evolution-chains":[\n')
        f.write(',\n'.join(processed_lines))
        f.write('\n]}')
    print(f'Done! Saved {fileName} ({len(processed_lines)} entries)')


def gMove():
    print('Generating /move/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/move/?offset=0&limit=919'
    print(mainURL)
    r=req.get(mainURL)
    data=r.json()
    # Storing Individual Requests
    URLs=[]
    results=[]
    count=0
    total=len(data['results'])
    for i in data['results']:
        count=count+1
        percent=math.floor((count/total)*100)
        if(percent%2==0):
            print(str(percent)+'% ('+str(count)+'/'+str(total)+')')
        url=i['url']
        URLs.append(i['url'])
        response=req.get(url)
        data=response.json()
        DataToWrite=dict()
        DataToWrite['id']=data['id']
        DataToWrite['generation']=data['generation']['name']
        DataToWrite['machines']=dict()
        DataToWrite['flavor_text_entries']=dict()
        for entry in data['flavor_text_entries']:
            if(entry['language']['name']=='en'):
                DataToWrite['flavor_text_entries'][gameVersions[entry['version_group']['name']]]=entry['flavor_text']
        for entry in data['effect_entries']:
            if(entry['language']['name']=='en'):
                effectEntry=dict()
                effectEntry['effect']=entry['effect']
                effectEntry['short_effect']=entry['short_effect']
                DataToWrite['effect_entries']=effectEntry
                break
        for entry in data['machines']:
            DataToWrite['machines'][gameVersions[entry['version_group']['name']]]=MachineUrlToID(entry['machine']['url'])
        results.append(DataToWrite)
    fileName='move.json'
    lines = [json.dumps(move, separators=(',', ':')) for move in results]

    # Use newline='\n' to force LF line endings (1 byte vs 2 for CRLF)
    with open(fileName, 'w', encoding='utf-8', newline='\n') as f:
        f.write('{"moves":[\n')
        f.write(',\n'.join(lines))
        f.write('\n]}')
    print(f'Done! Saved {fileName} ({len(results)} entries)')

    
def gAbility():
    print('Generating /ability/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/ability/?offset=0&limit=311'
    print(mainURL)
    r=req.get(mainURL)
    data=r.json()
    # Storing Individual Requests
    URLs=[]
    results=[]
    count=0
    total=len(data['results'])
    for i in data['results']:
        count=count+1
        percent=math.floor((count/total)*100)
        if(percent%2==0):
            print(str(percent)+'% ('+str(count)+'/'+str(total)+')')
        url=i['url']
        URLs.append(i['url'])
        response=req.get(url)
        data=response.json()
        DataToWrite=dict()
        DataToWrite['id']=data['id']
        DataToWrite['generation']=data['generation']['name']
        DataToWrite['flavor_text_entries']=dict()
        for entry in data['flavor_text_entries']:
            if(entry['language']['name']=='en'):
                DataToWrite['flavor_text_entries'][gameVersions[entry['version_group']['name']]]=entry['flavor_text']
        for entry in data['effect_entries']:
            if(entry['language']['name']=='en'):
                effectEntry=dict()
                effectEntry['effect']=entry['effect']
                effectEntry['short_effect']=entry['short_effect']
                DataToWrite['effect_entries']=effectEntry
                break
        results.append(DataToWrite)
    fileName='ability.json'
    # Minify each ability individually
    # separators=(',', ':') removes spaces after punctuation
    lines = [json.dumps(ability, separators=(',', ':')) for ability in results]

    # Force LF line endings for consistency across your Firebase assets
    with open(fileName, 'w', encoding='utf-8', newline='\n') as f:
        f.write('{"abilities":[\n')
        f.write(',\n'.join(lines))
        f.write('\n]}')
    print(f'Done! Saved {fileName} ({len(results)} entries)')


choice=takeInput()
while(choice!='exit'):
    if(choice=='0'):
        gPokemon()
        gPokemonSpecies()
        gEvolutionChain()
        gMove()
        gAbility()
    elif(choice=='1'):
        gPokemon()
    elif(choice=='2'):
        gPokemonSpecies()
    elif(choice=='3'):
        gEvolutionChain()
    elif(choice=='4'):
        gMove()
    elif(choice=='5'):
        gAbility()
    else:
        print('Enter 0,1,2,3,4,5 or exit')
    choice=takeInput()