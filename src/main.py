from pymongo import MongoClient
import config

# Connect to MongoDB
client = MongoClient(config.loom_mongo_uri)
db = client['Biosphere']
collection = db['BiosphereDendrometer_10']

# Pull a document
document = collection.find_one({"Packet.Number": 1})

print(document)