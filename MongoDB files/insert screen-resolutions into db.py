import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_resolutions"]

res_0 = {"_id":0,"name":"Countries-Resoluition","res":(1227,828),"level_1":[535,635],"level_2":[475,680],"level_3":[10,710],"level_4":[546,710],"level_5":[850,710],"level_6":[10,740],"level_7":[550,740],"level_8":[640,740],"level_9":[850,740],"level_10":[400,773], "level_11":[543,773], "level_12":[685,773], "level_13":[1080,773], "level_14":[1080,637]}
res_1 = {"_id":1,"name":"Hexagons-Resolution","res":(1200,700),"level_1":[508,512],"level_2":[459,557],"level_3":[10,587],"level_4":[521,587],"level_5":[825,587],"level_6":[10,617],"level_7":[525,617],"level_8":[615,617],"level_9":[825,617],"level_10":[375,645], "level_11":[518,645], "level_12":[660,645], "level_13":[1053,645], "level_14":[1053,509]}
res_2 = {"_id":2,"name":"Pyramids-Resolution","res":(1000,800),"level_1":[430,602],"level_2":[363,647],"level_3":[5,677],"level_4":[446,677],"level_5":[660,677],"level_6":[5,707],"level_7":[450,707],"level_8":[540,707],"level_9":[660,707],"level_10":[300,745], "level_11":[443,745], "level_12":[585,745], "level_13":[853,745], "level_14":[853,609]}
res_3 = {"_id":3,"name":"Quick-Triangles-resolution","res":(1000,700),"level_1":[430,505],"level_2":[363,547],"level_3":[10,577],"level_4":[451,577],"level_5":[660,577],"level_6":[10,607],"level_7":[455,607],"level_8":[545,607],"level_9":[660,607],"level_10":[305,645], "level_11":[448,645], "level_12":[590,645], "level_13":[853,645], "level_14":[853,509]}
res_4 = {"_id":4,"name":"Serious-Triangles-Resolution","res":(1000,700),"level_1":[430,505],"level_2":[363,547],"level_3":[10,577],"level_4":[451,577],"level_5":[660,577],"level_6":[15,607],"level_7":[455,607],"level_8":[545,607],"level_9":[660,607],"level_10":[305,645], "level_11":[448,645], "level_12":[590,645], "level_13":[853,645], "level_14":[853,509]}
res_5 = {"_id":5,"name":"Squares-Resolution","res":(1000,920),"level_1":[430,725],"level_2":[363,767],"level_3":[10,797],"level_4":[451,797],"level_5":[660,797],"level_6":[10,827],"level_7":[455,827],"level_8":[545,827],"level_9":[660,827],"level_10":[305,865], "level_11":[448,865], "level_12":[590,865], "level_13":[853,865], "level_14":[853,729]}
res_6 = {"_id":6,"name":"Stadium-Resolution","res":(1000,700),"level_1":[430,505],"level_2":[363,547],"level_3":[10,577],"level_4":[451,577],"level_5":[660,577],"level_6":[10,607],"level_7":[455,607],"level_8":[545,607],"level_9":[660,607],"level_10":[305,645], "level_11":[448,645], "level_12":[590,645], "level_13":[853,645], "level_14":[853,509]}
res_7 = {"_id":7,"name":"Keyboard-Resolution","res":(1300,620),"level_1":[560,425],"level_2":[508,470],"level_3":[10,500],"level_4":[576,500],"level_5":[960,500],"level_6":[10,535],"level_7":[580,535],"level_8":[670,535],"level_9":[960,535],"level_10":[430,565], "level_11":[573,565], "level_12":[715,565], "level_13":[1153,565], "level_14":[1153,429]}

# keyboard
#level 13 - skip_attack_button = Button(1, "SKIP", back_mode, (1153,565,140,50), 5, 6, 0, screen) # initiate the "skip" button.
#level 10 - auto_attack_button = Button(1, "AUTO", back_mode, (430,565,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#level 11 - skip_attack_button = Button(1, "SKIP", back_mode, (573,565,140,50), 5, 6, 0, screen) # initiate the "skip" button.
#level 12 - manual_attack_button = Button(1, "MANUAL", back_mode, (715,565,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#level 14 - save_button = Button(1, "SAVE", back_mode, (1153,429,140,50), 5, 6, 0, screen) # initiate the "skip" button.


collection.insert_one(res_0)
collection.insert_one(res_1)
collection.insert_one(res_2)
collection.insert_one(res_3)
collection.insert_one(res_4)
collection.insert_one(res_5)
collection.insert_one(res_6)
collection.insert_one(res_7)