import pymongo # import the PyMongo module
import random # import the random module
from pymongo import MongoClient # import the Client-method

# this is the cluster - as exists in the MongoDB atlas.
cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

sv = cluster["pyrisk_sv"] # the variable is the entire database - as exists in the MongoDB atlas.
save_doc = sv["saved_games"] # the variable is the entire database - as exists in the MongoDB atlas.

def data_to_dictionary (data_dict, code, back_mode, arr_players, arr_territories): # function that concentrates the existing game-data 
    back_mode = int(back_mode) # stabilize the 'back_mode' variable into an integer.
    data_dict.update({"_id":str(code)}) # insert the 'back_mode' variable value into the main dictionary.
    data_dict.update({"0":[]}) # insert a new list
    data_dict["0"].append(str(back_mode)) # add the value of 'back_mode' to the dictionary.
    #data_dict[str(0)] = data_dict.pop(0) # irrelevant
    for cnt in range(0, len(arr_players), 1): # loop over the list of players
        data_dict.update({str(cnt+1):[]}) # insert a new dictionary.
        data_dict[str(cnt+1)].append(arr_players[cnt].id_num) # insert "id_num" into the list of the dictionary.
        data_dict[str(cnt+1)].append(arr_players[cnt].color) # insert "color" into the list of the dictionary.
        data_dict[str(cnt+1)].append(arr_players[cnt].name) # insert "name" into the list of the dictionary.
        data_dict[str(cnt+1)].append(arr_players[cnt].typed) # insert "player-type" into the list of the dictionary.
        data_dict[str(cnt+1)].append(arr_players[cnt].cnt_init) # insert "initial-count" into the list of the dictionary.
        data_dict[str(cnt+1)].append(arr_players[cnt].trr_and_frc) # insert the "territory and force" dictionary to the list of the dictionary
        data_dict[str(cnt+1)].append(arr_players[cnt].allies) # insert the allies-list to the list of the dictionary.
        #data_dict[str(cnt+1)] = data_dict.pop(cnt+1) # irrelevant
    for cnt in range(0, len(arr_territories), 1): # loop over the list of territories
        data_dict.update({str(cnt+len(arr_players)+1):[]}) # insert a new dictionary.
        data_dict[str(cnt+len(arr_players)+1)].append(arr_territories[cnt].id_num) # insert "id_num" into the list of the dictionary
        data_dict[str(cnt+len(arr_players)+1)].append(arr_territories[cnt].name) # insert "name" into the list of the dictionary.
        data_dict[str(cnt+len(arr_players)+1)].append(arr_territories[cnt].pos) # insert "position" into the list of the dictionary.
        data_dict[str(cnt+len(arr_players)+1)].append(arr_territories[cnt].blob_names) # insert "blob_names"-list into the list of the dictionary.
        data_dict[str(cnt+len(arr_players)+1)].append(arr_territories[cnt].borders) # insert "borders"-list into the list of the dictionary.
        data_dict[str(cnt+len(arr_players)+1)].append(arr_territories[cnt].bonus_group) # insert "bonus-group"-list into the list of the dictionary.
        data_dict[str(cnt+len(arr_players)+1)].append(arr_territories[cnt].controller) # insert "controller" into the list of the dictionary.
        data_dict[str(cnt+len(arr_players)+1)].append(arr_territories[cnt].force_no) # insert "force-no"-list into the list of the dictionary.
        data_dict[str(cnt+len(arr_players)+1)].append(arr_territories[cnt].dots) # insert "dots"-list into the list of the dictionary.
        data_dict[str(cnt+len(arr_players)+1)].append(arr_territories[cnt].text_force_point) # insert "text-force-point"-list into the list of the dictionary.
        #data_dict[str(cnt+len(arr_players)+1)] = data_dict.pop(cnt+len(arr_players)+1) # irrelevant
    data_dict.update({str(len(data_dict)-1):[]})
    #print("-----") # debug print
    #print(data_dict) # debug print
    #print("-----") # debug print
    #print("len(arr_players) is: " + str(len(arr_players))) # debug print
    #print("str(len(data_dict)-1) is: " + str(str(len(data_dict)-1))) # debug print
    #print("The place is: " + str(len(data_dict))) # debug print
    data_dict[str(len(data_dict)-2)].append(int(len(arr_players))) # inser the length of the list of player-objects.
    data_dict[str(len(data_dict)-2)].append(int(len(arr_territories))) # insert the length of the list of territory-objects.
    #print(data_dict) # debug print
    #data_dict[len(data_dict)-1].append(len(arr_players)) # irrelevant
    #data_dict[len(data_dict)-1].append(len(arr_territories)) # irrelevant
    #data_dict[str(len(data_dict)-1)] = data_dict.pop(len(data_dict)) # irrelevant


def generate_save_code(): # function to generate a code
    code = random.randrange(10000, 100000) # a 5-digit code
    temp = save_doc.find_one({"_id":(code)}) # add the 'code' as an ID number of the data (chunk-of-text)
    while (temp is not None): # if the code has already been used - and already exists in the data-base, then we need to generate a new code
        code = random.randrange(10000, 100000) # a 5-digit code (generating a new code)
        temp = save_doc.find_one({"_id":(code)}) # attempting to locate a data (chunk-of-text) in the database.
    return code # return the generated code to the function-call
    
def save_game (back_mode, arr_players, arr_territories): # the general function to save the game (that's being called from the 'main' program)
    code = generate_save_code() # function to generate a random code to associate with the data in the data-base
    data_dict = {} # the dictionary which will contain the data of the current saved game
    data_to_dictionary(data_dict, code, back_mode, arr_players, arr_territories) # function to insert current data of the game into the dictionary
    #print("THE DATA DICT IS:............................") # debug print
    #for cnt in data_dict: # looping over the contents of the dictionary
    #    print(type(cnt)) # debug print
    #print("-----------") # debug print
    #print(data_dict) # debug print
    #print("-----------") # debug print
    save_doc.insert_one(data_dict) # insert the dictionary into the document of the data-base
    #print("finished") # debug print
    return code # return the generated-code to the function-call.
