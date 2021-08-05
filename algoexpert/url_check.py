from pymongo import MongoClient
mongo_uri = "mongodb://localhost:27017/"
client = MongoClient(mongo_uri)
print(client.list_database_names())


