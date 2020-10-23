import json
import pymongo
from pymongo import MongoClient
from getmac import get_mac_address as gma

client = MongoClient("mongodb+srv://admin:mongodb9143@cluster0.femb8.mongodb.net/group5db?retryWrites=true&w=majority")
db = client['group5db']

def insert_log():
    collection = db[gma()]
    with open('C:/Users/Taylor/Desktop/ActiveWindowListener/mongo/mongo_server_log.json') as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        collection.insert_many(file_data)
        print("Successfully inserted log as many files")
    else:
        collection.insert_one(file_data)
        print("Successfully inserted log as single file")

def create_collection():
    collection = gma()
    collection_list = db.list_collection_names()
    if collection in collection_list:
        print("Collection {} already exists!".format(collection))
    else:
        db.create_collection(collection)
        print("Collection: {} was created successfully!".format(collection))


client.close()
