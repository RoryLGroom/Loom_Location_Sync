from pymongo import MongoClient
import requests
import config
import base64
from datetime import date
#for testing location api

uri = config.test_mongo_uri
client = MongoClient(uri)


try:
    #Hologram

    #encode credentials using base64
    encoded_credentials = base64.b64encode(config.credentials.encode('utf-8')).decode('utf-8')
    #create header with hologram creds
    headers = {
    'Authorization': f'Basic {encoded_credentials}'
    }
    response = requests.get(config.hologram_url_location, headers= headers)
    data = response.json()
    all_devices = data["data"]

    # get rest of paginated data. Stores data we want to use in variable all_devices
    while(data["continues"]):
        new_request = requests.get(f'https://dashboard.hologram.io{data["links"]["next"]}', headers= headers)
        data = new_request.json()
        # adds data to list we want to publish to mongo
        all_devices.extend(data["data"])

    # filters list to only include devices with valid locations. When hologram sends out packets without location info, 
    #long and lat will be empty strings
    clean_devices = {}
    for device in all_devices:
        if device["latitude"] and device["longitude"]:
            device["Last Updated"] = date.today().isoformat()
            clean_devices[device["deviceid"]] = device

    # prints number of devices with actual location data. Right now, its about half. 
    #however, subsequent calls might return legitimate information. 
    print(clean_devices)
    #print("Retrieved ", len(clean_devices), " devices with locations from Hologram")



    
    db = client.get_database("Device_Test")
    collection = db.get_collection("Device_Test")
    #check to see if data has been updated and update existing mongoDb records, print number updated to terminal, 
    # and names of updated loctions
    number_updated = 0
    # collection.find({}) returns a cursor to a set of documents matching query, 
    # if argument is empty bracket, will return all documents
    for device in collection.find({}):
        device_id = device["deviceid"]

        if device_id in clean_devices:
            clean_device = clean_devices[device_id]
            
            if clean_device["latitude"] != device["latitude"] or clean_device["longitude"] != device["longitude"]:
                query = {"deviceid": device_id}
                update_operation = {
                    "$set": {"latitude": clean_device["latitude"], "longitude": clean_device["longitude"],
                    "Last Updated": clean_device["Last Updated"]}
                    }
                collection.update_one(query, update_operation)
                number_updated += 1

        else:
            collection.insert_one()

    if number_updated == 0:
        print("Locations are up to date")
    elif number_updated == 1:
        print("Updated ", number_updated, " device location")
    else:
        print("Updated ", number_updated, " device locations")


    


except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
