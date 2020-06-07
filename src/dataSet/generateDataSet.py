import json
import requests as req
import math
import re




gameVersions={"red-blue":1,"yellow":2,"gold-silver":3,"crystal":4,"ruby-sapphire":5,"emerald":6,
              "firered-leafgreen":7,"diamond-pearl":8,"platinum":9,"heartgold-soulsilver":10,"black-white":11,"colosseum":12,
              "xd":13,"black-2-white-2":14,"x-y":15,"omega-ruby-alpha-sapphire":16,"sun-moon":17,"ultra-sun-ultra-moon":18}


def MachineUrlToID(url):
    return int(re.sub(r'http(s)?:\/\/pokeapi.co\/api\/v2\/machine\/(\d+)\/', '\\2', url))
def EvoChainUrlToID(url):
    return int(re.sub(r'http(s)?:\/\/pokeapi.co\/api\/v2\/evolution-chain\/(\d+)\/', '\\2', url))
def PokemonUrlToID(url):
    return int(re.sub(r'http(s)?:\/\/pokeapi.co\/api\/v2\/pokemon\/(\d+)\/', '\\2', url))


def takeInput():
    print('-----------\n\n\n')
    print('What to generate:\n0) All\n1) /pokemon/\n2) /pokemon-species/\n3) /evolution-chain/\n4) /move/\n5) /ability/\nexit) Exit the program')
    print('\n\n\n-----------')
    return input()


def gPokemon():
    print('Generating /pokemon/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/pokemon/?offset=0&limit=10000000000'
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
        DataToWrite['abilities']=data['abilities']
        DataToWrite['base_experience']=data['base_experience']
        DataToWrite['height']=data['height']
        DataToWrite['held_items']=data['held_items']
        DataToWrite['id']=data['id']
        DataToWrite['is_default']=data['is_default']
        DataToWrite['moves']=data['moves']
        DataToWrite['name']=data['name']
        DataToWrite['order']=data['order']
        DataToWrite['species']=data['species']
        DataToWrite['stats']=data['stats']
        DataToWrite['types']=data['types']
        DataToWrite['weight']=data['weight']
        results[DataToWrite['id']]=DataToWrite
    fileName='pokemon.json'
    with open(fileName,'w') as f:
        data={'pokemon':results}
        f.write(json.dumps(data))
        print('Data wrote to '+fileName)

    
def gPokemonSpecies():
    print('Generating /pokemon-species/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit=10000'
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
        DataToWrite['BaH']=data['base_happiness']
        DataToWrite['CaR']=data['capture_rate']
        DataToWrite['Co']=data['color']['name']
        DataToWrite['EgG']=[egg['name'] for egg in data['egg_groups']]
        DataToWrite['EvC']=EvoChainUrlToID(data['evolution_chain']['url'])
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
    with open(fileName,'w') as f:
        data={'pokemon-species':results}
        f.write(json.dumps(data))
        print('Data wrote to '+fileName)

    
'''def gEvolutionChain():
    print('Generating /evolution-chain/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/evolution-chain/?offset=0&limit=100000'
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
        results.append(data)
    fileName='evolution-chain.json'
    with open(fileName,'w') as f:
        data={'evolution-chains':results}
        f.write(json.dumps(data))
        print('Data wrote to '+fileName)'''

def gEvolutionChain():
    print('Generating /evolution-chain/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/evolution-chain/?offset=0&limit=10000'
    print(mainURL)
    r=req.get(mainURL)
    data=r.json()
    # Storing Individual Requests
    URLs=[]
    results=[None]*427
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
    print(results)
    fileName='evolution-chain.json'
    with open(fileName,'w') as f:
        data={'evolution-chains':results}
        f.write(json.dumps(data))
        print('Data wrote to '+fileName)

    
def gMove():
    print('Generating /move/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/move/?offset=0&limit=728'
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
    with open(fileName,'w') as f:
        data={'moves':results}
        f.write(json.dumps(data))
        print('Data wrote to '+fileName)

    
def gAbility():
    print('Generating /ability/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/ability/?offset=0&limit=233'
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
    with open(fileName,'w') as f:
        data={'abilities':results}
        f.write(json.dumps(data))
        print('Data wrote to '+fileName)

    

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
    

    
