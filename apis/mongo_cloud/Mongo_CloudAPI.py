import json
import pymongo
from pymongo import MongoClient
from getmac import get_mac_address as gma

client = MongoClient("mongodb+srv://Admin:Pass123word#@cluster0.vh3ty.mongodb.net/WindowListener?retryWrites=true&w=majority")
db = client['WindowListener']

def insert_log():
    collection = db['json']

    with open('C:/Users/Taylor/Desktop/ActiveWindowListener/mongo/mongo_server_log.json') as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        collection.insert_many(file_data)
        print("IF statement")
    else:
        collection.insert_one(file_data)
        print("else statement")

def create_collection():
    collection_list = db.list_collection_names()
    collection = gma()
    if collection in collection_list:
        print("Collection {} already exists!".format(collection))
    else:
        db.create_collection(collection)
        print("Collection: {} was created successfully!".format(collection))


create_collection()   
client.close()
