import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_player_colors"]

color_0 = {"_id":0,"name":"Green","rdb_data":(34,139,34)}
color_1 = {"_id":1,"name":"Blue","rgb_data":(0,95,190)}
color_2 = {"_id":2,"name":"Yellow","rgb_data":(251,219,3)}
color_3 = {"_id":3,"name":"Red","rgb_data":(251,28,46)}
color_4 = {"_id":4,"name":"Orange","rgb_data":(255,102,0)}
color_5 = {"_id":5,"name":"Purple","rgb_data":(66,12,76)}

collection.insert_one(color_0)
collection.insert_one(color_1)
collection.insert_one(color_2)
collection.insert_one(color_3)
collection.insert_one(color_4)
collection.insert_one(color_5)