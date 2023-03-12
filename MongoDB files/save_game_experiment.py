from territory_class import Territory
from player_class import Player
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0-udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

sv = cluster["pyrisk_sv"]
collection = sv["saved_games"]

# WHAT DETAILS DO WE NEED TO SAVE?
# back_mode
# arr_players
# arr_territories

def data_to_dictionary (data_dict, code, back_mode, arr_players, arr_territories):
    back_mode = int(back_mode)
    data_dict.update({"_id":code})
    data_dict.update({0:[]})
    data_dict[0].append(str(back_mode))
    data_dict[str(0)] = data_dict.pop(0)
    for cnt in range(0, len(arr_players), 1):
        data_dict.update({cnt+1:[]})
        data_dict[cnt+1].append(str(arr_players[cnt].id_num))
        data_dict[cnt+1].append(str(arr_players[cnt].color))
        data_dict[cnt+1].append(str(arr_players[cnt].name))
        data_dict[cnt+1].append(str(arr_players[cnt].typed))
        data_dict[cnt+1].append(str(arr_players[cnt].cnt_init))
        data_dict[cnt+1].append(str(arr_players[cnt].trr_and_frc))
        data_dict[cnt+1].append(str(arr_players[cnt].allies))
        data_dict[str(cnt+1)] = data_dict.pop(cnt+1)
    for cnt in range(0, len(arr_territories), 1):
        data_dict.update({cnt+len(arr_players)+1:[]})
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].id_num))
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].name))
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].pos))
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].blob_names))
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].real_blobs))
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].borders))
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].bonus_group))
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].controller))
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].force_no))
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].dots))
        data_dict[cnt+len(arr_players)+1].append(str(arr_territories[cnt].screen))
        data_dict[str(cnt+len(arr_players)+1)] = data_dict.pop(cnt+len(arr_players)+1)
    data_dict.update({len(data_dict)+1:[]})
    data_dict[len(data_dict)].append(len(arr_players))
    data_dict[len(data_dict)].append(len(arr_territories))
    #data_dict[len(data_dict)-1].append(len(arr_players))
    #data_dict[len(data_dict)-1].append(len(arr_territories))
    data_dict[str(len(data_dict)-1)] = data_dict.pop(len(data_dict))


back_mode = int(0)

Alaska = Territory(0,"Alaska",[50,50],["R","G","B"], 0, [1,2,3],0,0,34,[11,22,33],0,0)
NorthWestTerritory = Territory(1,"Peru",[100,100],["R","G","B"], 0, [1,2,3],0,0,34,[11,22,33],0,0)
Alberta = Territory(2,"Alberta",[200,200],["R","G","B"], 0, [1,2,3],0,0,34,[11,22,33],0,0)
Ontario = Territory(3,"Ontario",[400,400],["R","G","B"], 0, [1,2,3],0,0,34,[11,22,33],0,0)
Quebec = Territory(4,"Quebec",[400,400],["R","G","B"], 0, [1,2,3],0,0,34,[11,22,33],0,0)
WesternUnitedStates = Territory(5,"Western-United-States",[400,400],["R","G","B"], 0, [1,2,3],0,0,34,[11,22,33],0,0)
EasternUnitedStates = Territory(6,"Eastern-United-States",[400,400],["R","G","B"], 0, [1,2,3],0,0,34,[11,22,33],0,0)
Greenland = Territory(7,"Greenland",[400,400],["R","G","B"], 0, [1,2,3],0,0,34,[11,22,33],0,0)
Mexico = Territory(8,"Mexico",[400,400],["R","G","B"], 0, [1,2,3],0,0,34,[11,22,33],0,0)

player1 = Player(0, (39,134,39), "Aviv", 1, 0, {"1":50, "2":100}, [])
player2 = Player(1, (20,30,50), "Lester", 1, 0, {"3":150, "4":200}, [])
player3 = Player(2, (100,100,100), "Yunker", 1, 0, {"5":250, "6":300}, [])

arr_territories = [Alaska, NorthWestTerritory, Alberta, Ontario, WesternUnitedStates, EasternUnitedStates, Greenland, Mexico]
arr_players = [player1, player2, player3]

print(arr_players)

data_dict = {}
code = 11223344556
data_to_dictionary(data_dict, code, back_mode, arr_players, arr_territories)
#list_to_dict_territories (dict_territories, arr_territories, code)
#list_to_dict_players (dict_players, arr_players, code)
#print(data_dict)
collection.insert_one(data_dict)
