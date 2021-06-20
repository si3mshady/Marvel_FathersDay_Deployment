import requests
import hashlib
import time
import json
import os 

USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')

try:
    def getCredentials(filename="creds.json"):
        with open(filename, 'r') as file:
            data = file.read()        
            return json.loads(data)  
except Exception:
    pass

def genMD5Hash():
    jsonData = getCredentials(filename="creds.json")
    try:
        publicKey = jsonData.get('publicKey')
        privateKey = jsonData.get('privateKey')
        timestamp = str(time.time())
        authStringsCombined = timestamp  + privateKey  + publicKey        
        authStringsCombined_md5 = hashlib.md5(authStringsCombined.encode())
        md5Hash = authStringsCombined_md5.hexdigest()
        return {"ts":timestamp, "apiKey":publicKey, "hash":md5Hash }  
    except IndexError as e:
        print(e)

def processCharacterAttributes(relatedData):
    # array will hold documents of the same information for all other characters Spectrum has worked with in other comics.
    associatedCharacterList = []
     
    resourceURIList = [rl['resourceURI'] for rl in  relatedData['items']]
   
    for url in resourceURIList:       
        result = requests.get(generateAuthURL(url))
        if result.status_code == 200:           
            for jsonResult in  result.json()['data']['results']:
              
                for i in jsonResult['characters']['items']:                  
                    associatedCharacterList.append(i['name'])
    
        else:
            print('Fail')
            print(result.status_code)
            

def generateCharacterSearchURL(character="falcon"):  
    #generates url string with query params required to fetch data from character via endpoint -> /v1/public/characters
    allParams = genMD5Hash()            
    queryParams = f"?ts={allParams['ts']}&name={character.lower()}&apikey={allParams['apiKey']}&hash={allParams['hash']}"        
    endpoint = "https://gateway.marvel.com:443/v1/public/characters"  + queryParams   
    return endpoint

def fetchCharacterAttributes(character):
    endpoint = generateCharacterSearchURL(character.lower())        
    imageVariant = "/portrait_xlarge."    
    res = requests.get(endpoint) 
    if res.status_code == 200:
                  
        try:
            
            results = res.json()['data']['results'][0]    
            print('Boom!')                   

            characterAttributes = { "name": results['name'], 
            "id": results['id'], "description": results['description'],
            "picture": results['thumbnail']['path'] \
            + imageVariant + results['thumbnail']['extension'] }   
            
            print(characterAttributes.get('picture'))       
            return characterAttributes
           
        
        except Exception as e:
            print(e)

       
    else:
        print(res.status_code)
        print(res.content)

def lambda_handler(event=None,context=None):    
    comicData = fetchCharacterAttributes('spider-man')



lambda_handler()