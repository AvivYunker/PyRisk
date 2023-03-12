import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_total_territories"]

id_ranges_0 = {"_id":0,"name":"Countries-Total","total":(0,41)}
id_ranges_1 = {"_id":1,"name":"Hexagons-Total","total":(42,97)}
id_ranges_2 = {"_id":2,"name":"Pyramids-Total","total":(98,161)}
id_ranges_3 = {"_id":3,"name":"Quick-Triangles-Total","total":(162,165)}
id_ranges_4 = {"_id":4,"name":"Serious-Triangles-Total","total":(166,197)}
id_ranges_5 = {"_id":5,"name":"Squares-Total","total":(198,233)}
id_ranges_6 = {"_id":6,"name":"Stadium-Total","total":(234,265)}
id_ranges_7 = {"_id":7,"name":"Keyboard-Total","total":(266,370)}

collection.insert_one(id_ranges_0)
collection.insert_one(id_ranges_1)
collection.insert_one(id_ranges_2)
collection.insert_one(id_ranges_3)
collection.insert_one(id_ranges_4)
collection.insert_one(id_ranges_5)
collection.insert_one(id_ranges_6)
collection.insert_one(id_ranges_7)