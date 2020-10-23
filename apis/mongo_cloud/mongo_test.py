import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Admin:Pass123word#@cluster0.vh3ty.mongodb.net/WindowListener?retryWrites=true&w=majority")
db = client.test
