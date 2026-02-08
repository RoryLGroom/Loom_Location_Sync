from pymongo import MongoClient
import requests
import config
#for testing location api
import random

uri = config.Test_uri
client = MongoClient(uri)

try:
    #get database names
    listOfDatabases= client.list_database_names()
    #cycle through databases
    
    for database in listOfDatabases:
        #print name of each database in given collection
        names = client[database].list_collection_names()
        print(database, names)
    client.close
    """
    collection = database.get_collection("Test1")

    # add 100 new documents for testing
    doc = []

    for i in range(2,101):
        doc.append({"DeviceID": 1391935, "Packet": i})

    result = collection.insert_many(doc)
    query = { "DeviceID": 1391935}
    print(result)
    result1 = collection.update_many(query, {"$set": {"LocationData": "Oregon"}})

    client.close


        

    
    # Query for a movie that has the title 'Back to the Future'
    query = { "DeviceID": 1391935}
    packet_1 = Mux_Multiplex.find_one(query)
    print(packet_1)
    packet_1_update= Mux_Multiplex.update_one(query, {"$set": {"LocationData": "Oregon"}})
    print(packet_1_update)

    client.close()

    #hologram_response = requests.get("https://dashboard.hologram.io/api/1/devices/1391935")
    #print(hologram_response.json())
"""
except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
