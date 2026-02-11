from pymongo import MongoClient
import requests
import config
import base64
#for testing location api

uri = config.loom_mongo_uri
client = MongoClient(uri)


try:
    #Hologram - Fetch 
    #retrieve lists of deviceswith one API call
    hologram_url = "https://dashboard.hologram.io/api/1/devices/?orgid=30237"
    #encode credentials using base64
    encoded_credentials = base64.b64encode(config.credentials.encode('utf-8')).decode('utf-8')
    #create header with hologram creds
    headers = {
    'Authorization': f'Basic {encoded_credentials}'
    }
    response = requests.get(hologram_url, headers= headers)

    print(response.text)

    #Mongo
    #check devices with matching ID, if location doesnt exist, update
    query = { "DeviceID": {"$exists": True}, "Location": {"$exists": False}}
    """

    listOfDatabases= client.list_database_names()
    for database in listOfDatabases:
        curr_database = client.get_database(database)
       
    collection = database.get_collection("Test1")

    client.close
"""
except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
