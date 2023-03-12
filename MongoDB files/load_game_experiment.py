from territory_class import Territory
from player_class import Player
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0-udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

sv = cluster["pyrisk_sv"]
save_doc = sv["saved_games"]

def load_back_mode (DATA):
    return (DATA[str(0)][0])

# ---------------------------------------
def load_arr_players (arr_players, DATA):
    cell = str(len(DATA)-2)
    print("THe thing is: " + str(int(DATA[cell][0])+1))
    for cnt in range(1, int(DATA[cell][0])+1, 1):
        arr_players.append([])
        arr_players[len(arr_players)-1].append(DATA[str(cnt)][0])
        arr_players[len(arr_players)-1].append(DATA[str(cnt)][1])
        arr_players[len(arr_players)-1].append(DATA[str(cnt)][2])
        arr_players[len(arr_players)-1].append(DATA[str(cnt)][3])
        arr_players[len(arr_players)-1].append(DATA[str(cnt)][4])
        arr_players[len(arr_players)-1].append(DATA[str(cnt)][5])
        arr_players[len(arr_players)-1].append(DATA[str(cnt)][6])
# FINALLY GOT THIS WORKING

# ---------------------------------------

def load_arr_territories (arr_territories, DATA):
    cell = str(len(DATA)-2)
    print("lower edge is: " + str(int(DATA[cell][0])+1))
    print("upper edge is: " + str(int(DATA[cell][0])+int(DATA[cell][1])+1))
    for cnt in range(int(DATA[cell][0])+1, int(DATA[cell][0])+int(DATA[cell][1])+1, 1):
        arr_territories.append([])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][0])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][1])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][2])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][3])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][4])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][5])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][6])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][7])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][8])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][9])
        arr_territories[len(arr_territories)-1].append(DATA[str(cnt)][10])
        #print(DATA[str(cnt)])

def load_map_number (DATA):
    cell = str(len(DATA)-2)
    id_num = str(DATA[str(DATA[cell][0]+1)][0])
    if (id_num == '0'):
        return 1
    elif (id_num == '42'):
        return 2
    elif (id_num == '98'):
        return 3
    elif (id_num == '162'):
        return 4
    elif (id_num == '166'):
        return 5
    elif (id_num == '198'):
        return 6
    elif (id_num == '234'):
        return 7
    elif (id_num == '266'):
        return 8

def load_totals (totals, DATA):
    cell = str(len(DATA)-2)
    totals[0] = int((DATA[str(DATA[str(cell)][0]+1)][0]))
    totals[1] = int((DATA[str(DATA[str(cell)][0]+DATA[str(cell)][1])][0]))



DATA = save_doc.find_one({"_id":(11223344556)}) # locate the metching "object" according to the map number.
print(DATA)
print("The type of DATA is: " + str(type(DATA)))
while (DATA is not None):
    pass
    

#cell = str(len(DATA)-2)

selected_map = int(0)
back_mode = int(-1)
arr_players = []
arr_territories = []
totals = [0,0]

load_arr_players(arr_players, DATA)
print(arr_players)
#TOTAL = save_doc.find_one({"_id":(11223344557)}) # locate the metching "object" according to the map number.
#print(TOTAL)