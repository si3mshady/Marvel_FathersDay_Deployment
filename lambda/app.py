import requests
import hashlib
import time
import json
import os 

PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')


def genMD5Hash():
    
    try:
        publicKey = PUBLIC_KEY 
        privateKey = PRIVATE_KEY 
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
            return str(characterAttributes.get('picture'))
           
        
        except Exception as e:
            print(e)

       
    else:
        print(res.status_code)
        print(res.content)

def lambda_handler(event,context):        

    data = event.get('body')           
    character = json.loads(data) #data is a string conver to 
    character = character.get('character')  #ternary operator with tuples     
    comicData = fetchCharacterAttributes(character)
    return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"},
      "body": json.dumps(comicData)}

    
    

    
#Elliott Arnold 
#Docker, Deployment, CICD Practice 
#Query Marvel API to receive an image of desired character 
#Fathers Day 
#6-20-21



