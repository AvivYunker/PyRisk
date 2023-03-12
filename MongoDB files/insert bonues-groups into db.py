import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_bonus"]

bonus_0 = {"_id":0,"name":"North-America","territories":(0,1,2,3,4,5,6,7,8),"bonus":5}
bonus_1 = {"_id":1,"name":"South-America","territories":(9,10,11,12),"bonus":2}
bonus_2 = {"_id":2,"name":"Europe","territories":(13,14,15,16,17,18,19),"bonus":5}
bonus_3 = {"_id":3,"name":"Africa","territories":(20,21,22,23,24,25),"bonus":3}
bonus_4 = {"_id":4,"name":"Asia","territories":(26,27,28,29,30,31,32,33,34,35,36,37),"bonus":7}
bonus_5 = {"_id":5,"name":"Australia","territories":(38,39,40,41),"bonus":2}
bonus_6 = {"_id":6,"name":"North-West-Hexagons","territories":(42,43,44,45,46,47,48,56,57,58,59,60,61,62),"bonus":4}
bonus_7 = {"_id":7,"name":"North-East-Hexagons","territories":(49,50,51,52,53,54,55,63,64,65,66,67,68,69),"bonus":4}
bonus_8 = {"_id":8,"name":"South-West-Hexagons","territories":(70,71,72,73,74,75,76,84,85,86,87,88,89,90),"bonus":4}
bonus_9 = {"_id":9,"name":"South-East-Hexagons","territories":(77,78,79,80,81,82,83,91,92,93,94,95,96,97),"bonus":4}
bonus_10 = {"_id":10,"name":"North-Pyramid","territories":(98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113),"bonus":4}
bonus_11 = {"_id":11,"name":"West-Pyramid","territories":(114,123,124,125,134,135,136,137,138,147,148,149,150,151,152,153),"bonus":4}
bonus_12 = {"_id":12,"name":"Central-Pyramid","territories":(115,116,117,118,119,120,121,126,127,128,129,130,139,140,141,154),"bonus":4}
bonus_13 = {"_id":13,"name":"East-Pyramid","territories":(122,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161),"bonus":4}
bonus_14 = {"_id":14,"name":"West-Quick","territories":(162,163),"bonus":8}
bonus_15 = {"_id":15,"name":"East-Quick","territories":(164,165),"bonus":8}
bonus_16 = {"_id":16,"name":"North-West-Serious","territories":(166,167,168,169,174,175,176,177),"bonus":3}
bonus_17 = {"_id":17,"name":"North-East-Serious","territories":(170,171,172,173,178,179,180,181),"bonus":3}
bonus_18 = {"_id":18,"name":"South-West-Serious","territories":(182,183,184,185,190,191,192,193),"bonus":3}
bonus_19 = {"_id":19,"name":"South-East-Serious","territories":(186,187,188,189,194,195,196,197),"bonus":3} # finished till here
bonus_20 = {"_id":20,"name":"North-West-Squares","territories":(198,199,200,204,205,206,210,211,212),"bonus":4}
bonus_21 = {"_id":21,"name":"North-East-Squares","territories":(201,202,203,207,208,209,213,214,215),"bonus":4}
bonus_22 = {"_id":22,"name":"South-West-Squares","territories":(216,217,218,222,223,224,228,229,230),"bonus":4}
bonus_23 = {"_id":23,"name":"South-East-Squares","territories":(219,220,221,225,226,227,231,232,233),"bonus":4}
bonus_24 = {"_id":24,"name":"Extreme-North-West-Stadium","territories":(234,240,241,242),"bonus":4}
bonus_25 = {"_id":25,"name":"Central-North-West-Stadium","territories":(235,236,243,244),"bonus":4}
bonus_26 = {"_id":26,"name":"Central-North-East-Stadium","territories":(237,238,245,246),"bonus":4}
bonus_27 = {"_id":27,"name":"Extreme-North-East-Stadium","territories":(239,247,248,249),"bonus":4}
bonus_28 = {"_id":28,"name":"Extreme-South-East-Stadium","territories":(250,251,252,260),"bonus":4}
bonus_29 = {"_id":29,"name":"Central-South-West-Stadium","territories":(253,254,261,262),"bonus":4}
bonus_30 = {"_id":30,"name":"Central-South-East-Stadium","territories":(255,256,263,264),"bonus":4}
bonus_31 = {"_id":31,"name":"Extreme-South-East-Stadium","territories":(257,258,259,265),"bonus":4}
bonus_32 = {"_id":32,"name":"Escape-Key-Keyboard","territories":(266),"bonus":1}
bonus_33 = {"_id":33,"name":"F1-F4-Keyboard","territories":(267,268,269,270),"bonus":3}
bonus_34 = {"_id":34,"name":"F5-F8-Keyboard","territories":(271,272,273,274),"bonus":3}
bonus_35 = {"_id":35,"name":"F9-F12-Keyboard","territories":(275,276,277,278),"bonus":3}
bonus_36 = {"_id":36,"name":"Print-Scroll-Pause-Keyboard","territories":(279,280,281),"bonus":2}
bonus_37 = {"_id":37,"name":"Central-Keyboard","territories":(282,283,284,285,286,287,288,289,290,291,292,293,294,295,303,304,305,306,307,308,309,310,311,312,313,314,315,316,324,325,326,327,328,329,330,331,332,333,334,335,336,340,341,342,343,344,345,346,347,348,349,350,351,352,358,359,360,361,362,363,364,365),"bonus":25}
bonus_38 = {"_id":38,"name":"Insert-Home-Delete-End-Keyboard","territories":(296,297,298,317,318,319),"bonus":7}
bonus_39 = {"_id":39,"name":"Numpad-Keyboard","territories":(299,300,301,302,320,321,322,323,337,338,339,354,355,357,356,369,370),"bonus":15}
bonus_40 = {"_id":40,"name":"ArrowKeys-Keyboard","territories":(353,366,367,368),"bonus":5}

collection.insert_one(bonus_0)
collection.insert_one(bonus_1)
collection.insert_one(bonus_2)
collection.insert_one(bonus_3)
collection.insert_one(bonus_4)
collection.insert_one(bonus_5)
collection.insert_one(bonus_6)
collection.insert_one(bonus_7)
collection.insert_one(bonus_8)
collection.insert_one(bonus_9)
collection.insert_one(bonus_10)
collection.insert_one(bonus_11)
collection.insert_one(bonus_12)
collection.insert_one(bonus_13)
collection.insert_one(bonus_14)
collection.insert_one(bonus_15)
collection.insert_one(bonus_16)
collection.insert_one(bonus_17)
collection.insert_one(bonus_18)
collection.insert_one(bonus_19)
collection.insert_one(bonus_20)
collection.insert_one(bonus_21)
collection.insert_one(bonus_22)
collection.insert_one(bonus_23)
collection.insert_one(bonus_24)
collection.insert_one(bonus_25)
collection.insert_one(bonus_26)
collection.insert_one(bonus_27)
collection.insert_one(bonus_28)
collection.insert_one(bonus_29)
collection.insert_one(bonus_30)
collection.insert_one(bonus_31)
collection.insert_one(bonus_32)
collection.insert_one(bonus_33)
collection.insert_one(bonus_34)
collection.insert_one(bonus_35)
collection.insert_one(bonus_36)
collection.insert_one(bonus_37)
collection.insert_one(bonus_38)
collection.insert_one(bonus_39)
collection.insert_one(bonus_40)