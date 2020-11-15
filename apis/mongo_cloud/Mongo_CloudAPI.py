import json
import pymongo
from pymongo import MongoClient
from getmac import get_mac_address as gma
from flask_blueprints.example_bp import get_analysis

client = MongoClient("mongodb+srv://admin:mongodb9143@cluster0.femb8.mongodb.net/group5db?retryWrites=true&w=majority")
db = client['group5db']
analysis = get_analysis()


# def insert_log():
#     collection = db[gma()]
#     # with open('C:/Users/Taylor/Desktop/ActiveWindowListener/mongo/mongo_server_log1.json') as file:
#     #     file_data = json.load(file)

#     if isinstance(analysis, list):
#         collection.insert_many(analysis)
#         print("Successfully inserted log as many files")
#     else:
#         collection.insert_one(analysis)
#         print("Successfully inserted log as single file")

def create_collection():
    collection = gma()
    collection_list = db.list_collection_names()
    if collection in collection_list:
        print("Collection {} already exists!".format(collection))
    else:
        db.create_collection(collection)
        print("Collection: {} was created successfully!".format(collection))

# insert_log()
client.close()
