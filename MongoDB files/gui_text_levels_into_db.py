import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0-udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_gui_text_levels"]

# res_0 = {"_id":0,"name":"Countries-Resoluition","res":(1227,628)}

group_1 = {"_id":0,"name":"group_one","valid_ids":[0],"level_0":[535,640],"level_1":[200,680],"level_2":[270,720],"level_3":[560,710]}
group_2 = {"_id":1,"name":"group_two","valid_ids":[1],}

# (1227, 828)
# group1 - countries            # -692 / -188
gt0 = gui_text("ATTACK", 40, 0, [535,640,1,40], screen) # level 0
gt1 = gui_text("012345, select attacking territory!", 20, 0, [200,680,1,20], screen) # level 1
gt2 = gui_text("012345, select territory to attack!", 20, 0, [700,680,1,20], screen) # level 1
gt3 = gui_text("ATTACKER: Alaska", 20, 0, [270,720,1,20], screen) # level 2
gt4 = gui_text("ATTACKED: Alberta", 20, 0, [770,720,1,20], screen) # level 2
one_valued_dice(560,710,(34,139,34)) # level 3
one_valued_dice(650,710,(34,139,34)) # level 3

# (1200,700)
# group2 - hexagons             # -692 / -188
gt0 = gui_text("ATTACK", 40, 0, [508,512,1,40], screen)
gt1 = gui_text("012345, select attacking territory!", 20, 0, [173,552,1,20], screen)
gt2 = gui_text("012345, select territory to attack!", 20, 0, [673,552,1,20], screen)
gt3 = gui_text("ATTACKER: Alaska", 20, 0, [243,592,1,20], screen)
gt4 = gui_text("ATTACKED: Alberta", 20, 0, [743,592,1,20], screen)
one_valued_dice(533,582,(34,139,34))
one_valued_dice(623,582,(34,139,34))

# (1000,800)
# group3 - pyramid              # 
gt0 = gui_text("ATTACK", 40, 0, [308,612,1,40], screen)
gt1 = gui_text("012345, select attacking territory!", 20, 0, [85,645,1,20], screen)
gt2 = gui_text("012345, select territory to attack!", 20, 0, [585,645,1,20], screen)
gt3 = gui_text("ATTACKER: Alaska", 20, 0, [155,685,1,20], screen)
gt4 = gui_text("ATTACKED: Alberta", 20, 0, [655,685,1,20], screen)
one_valued_dice(445,675,(34,139,34))
one_valued_dice(535,675,(34,139,34))

# group4 - keyboard
gt0 = gui_text("ATTACK", 40, 0, [560,425,1,40], screen)
gt1 = gui_text("012345, select attacking territory!", 20, 0, [225,465,1,20], screen)
gt2 = gui_text("012345, select territory to attack!", 20, 0, [725,465,1,20], screen)
gt3 = gui_text("ATTACKER: Alaska", 20, 0, [295,505,1,20], screen)
gt4 = gui_text("ATTACKED: Alberta", 20, 0, [795,505,1,20], screen)
one_valued_dice(585,495,(34,139,34))
one_valued_dice(675,495,(34,139,34))