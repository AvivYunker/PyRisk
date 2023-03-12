import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0-udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]

blob_names_doc = db["pyrisk_blob_links"]
bonus_doc = db["pyrisk_bonus"]
borders_doc = db["pyrisk_borders"]
dots_doc = db["pyrisk_dots"]
pos_doc = db["pyrisk_positions"]
force_doc = db["pyrisk_force_text"]

def insert_to_txt (strr):
    strr = str(strr)
    file = open("general_database", "w")
    file.write(strr)
    file.close()

# List of territory features:

# ordered list:
# 1. dictionary definition
# 2. id_number (0-370)
# 3. borders
# 4. bonus group
# 6. force-text
# 7. positions
# 8. blob-links

# 5. dots

entire_string = ["alaska","north_west_territory","alberta","ontario","quebec","western_united_states","eastern_united_states","greenland","mexico","venezuela","peru","argentina","brazil","iceland","scandinavia","great_britain","western_europe","northern_europe","southern_europe","ukraine","north_africa","egypt","sudan","congo","south_africa","madagascar","middle_east","india","siam","china","central_asia","ural","siberia","yakutsk","irkutsk","kamtchatka","mongolia","japan","indonesia","papau_new_guinea","western_australia","eastern_australia","hex0","hex1","hex2","hex3","hex4","hex5","hex6","hex7","hex8","hex9","hex10","hex11","hex12","hex13","hex14","hex15","hex16","hex17","hex18","hex19","hex20","hex21","hex22","hex23","hex24","hex25","hex26","hex27","hex28","hex29","hex30","hex31","hex32","hex33","hex34","hex35","hex36","hex37","hex38","hex39","hex40","hex41","hex42","hex43","hex44","hex45","hex46","hex47","hex48","hex49","hex50","hex51","hex52","hex53","hex54","hex55","pyr0","pyr1","pyr2","pyr3","pyr4","pyr5","pyr6","pyr7","pyr8","pyr9","pyr10","pyr11","pyr12","pyr13","pyr14","pyr15","pyr16","pyr17","pyr18","pyr19","pyr20","pyr21","pyr22","pyr23","pyr24","pyr25","pyr26","pyr27","pyr28","pyr29","pyr30","pyr31","pyr32","pyr33","pyr34","pyr35","pyr36","pyr37","pyr38","pyr39","pyr40","pyr41","pyr42","pyr43","pyr44","pyr45","pyr46","pyr47","pyr48","pyr49","pyr50","pyr51","pyr52","pyr53","pyr54","pyr55","pyr56","pyr57","pyr58","pyr59","pyr60","pyr61","pyr62","pyr63","qck0","qck1","qck2","qck3","srs0","srs1","srs2","srs3","srs4","srs5","srs6","srs7","srs8","srs9","srs10","srs11","srs12","srs13","srs14","srs15","srs16","srs17","srs18","srs19","srs20","srs21","srs22","srs23","srs24","srs25","srs26","srs27","srs28","srs29","srs30","srs31","sqr0","sqr1","sqr2","sqr3","sqr4","sqr5","sqr6","sqr7","sqr8","sqr9","sqr10","sqr11","sqr12","sqr13","sqr14","sqr15","sqr16","sqr17","sqr18","sqr19","sqr20","sqr21","sqr22","sqr23","sqr24","sqr25","sqr26","sqr27","sqr28","sqr29","sqr30","sqr31","sqr32","sqr33","sqr34","sqr35","stad0","stad1","stad2","stad3","stad4","stad5","stad6","stad7","stad8","stad9","stad10","stad11","stad12","stad13","stad14","stad15","stad16","stad17","stad18","stad19","stad20","stad21","stad22","stad23","stad24","stad25","stad26","stad27","stad28","stad29","stad30","stad31","kybrd0","kybrd1","kybrd2","kybrd3","kybrd4","kybrd5","kybrd6","kybrd7","kybrd8","kybrd9","kybrd10","kybrd11","kybrd12","kybrd13","kybrd14","kybrd15","kybrd16","kybrd17","kybrd18","kybrd19","kybrd20","kybrd21","kybrd22","kybrd23","kybrd24","kybrd25","kybrd26","kybrd27","kybrd28","kybrd29","kybrd30","kybrd31","kybrd32","kybrd33","kybrd34","kybrd35","kybrd36","kybrd37","kybrd38","kybrd39","kybrd40","kybrd41","kybrd42","kybrd43","kybrd44","kybrd45","kybrd46","kybrd47","kybrd48","kybrd49","kybrd50","kybrd51","kybrd52","kybrd53","kybrd54","kybrd55","kybrd56","kybrd57","kybrd58","kybrd59","kybrd60","kybrd61","kybrd62","kybrd63","kybrd64","kybrd65","kybrd66","kybrd67","kybrd68","kybrd69","kybrd70","kybrd71","kybrd72","kybrd73","kybrd74","kybrd75","kybrd76","kybrd77","kybrd78","kybrd79","kybrd80","kybrd81","kybrd82","kybrd83","kybrd84","kybrd85","kybrd86","kybrd87","kybrd88","kybrd89","kybrd90","kybrd91","kybrd92","kybrd93","kybrd94","kybrd95","kybrd96","kybrd97","kybrd98","kybrd99","kybrd100","kybrd101","kybrd102","kybrd103","kybrd104"]

# alaska_force_text = {"_id":0,"name":"alaska","force_text":(70,60)}

strr = str("")


for cnt in range(0, 371, 1):
    NAME = borders_doc.find_one({"_id":(cnt)})
    BORDERS = borders_doc.find_one({"_id":(cnt)})
    BONUS = bonus_doc.find_one({"territories":(cnt)})
    FORCE = force_doc.find_one({"_id":(cnt)})
    POSITION = pos_doc.find_one({"_id":(cnt)})
    BLOB_NAMES = blob_names_doc.find_one({"valid_ids":(cnt)})
    DOTS = dots_doc.find_one({"_id":(cnt)})
    strr += (str(entire_string[cnt]) + '_general = {"_id":' + str(cnt) + ',"name":"' + str(NAME["name"]) + '","borders":' + str(BORDERS["borders"]) + ',"bonus_group":{"' + str(BONUS["bonus"]) + '":' + str(BONUS["territories"]) + '},"force_text":' + str(FORCE["force_text"]) + ',"blob_positions":' + str(POSITION["position"]) + ',"blob_names":' + str(BLOB_NAMES["strings"]) + ',"dots":' + str(DOTS["dots"]) + "}\n")
    print(str(cnt))
print("-----")
for cnt in range(0, 371, 1):
    strr += ("collection.insert_one(" + str(entire_string[cnt]) + '_general)\n')
    print(str(cnt))
insert_to_txt(strr)
print("\nDONE!\n")