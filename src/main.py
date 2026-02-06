from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Insert a document
collection.insert_one({'name': 'Example', 'type': 'Test'})

# Query a document
document = collection.find_one({'name': 'Example'})
print(document)