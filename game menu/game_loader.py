import pygame # importing the PyGame module 
from territory_class import Territory # import the Territory class
from player_class import Player # import the Player class
import pymongo # import the PyMongo module
from pymongo import MongoClient # import the Client-method
#from game_menu import load_game_map
#from game_menu import load_gui_text_levels

# this is the cluster - as exists in the MongoDB atlas.
cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"] # the variable is the entire database - as exists in the MongoDB atlas.
sv = cluster["pyrisk_sv"] # the variable is the entire database - as exists in the MongoDB atlas.
save_doc = sv["saved_games"] # the variable is the entire database - as exists in the MongoDB atlas.
res_doc = db["pyrisk_resolutions"] # the document that holds the resolutions of the game-maps

def load_arr_players (arr_players, DATA): # load the list of player-objects
    cell = str(len(DATA)-2) # get the specific place from which we can locate the player-data
    #print("the important cell is: " + str(DATA[cell])) # debug print
    #print("the next cell is: " + str(DATA[cell][0]+1)) # debug print
    #print("The 'cell' is: " + str(cell)) # debug print
    for cnt in range(1, int((DATA[cell][0])+1), 1): # looping over the data of the players
        arr_players.append(Player(0,0,0,0,0,0,0)) # append a new player-object
        arr_players[cnt-1].id_num = int(DATA[str(cnt)][0]) # assign the ID-number.
        arr_players[cnt-1].color = (DATA[str(cnt)][1]) # assign the color.
        arr_players[cnt-1].name = str(DATA[str(cnt)][2]) # assign the name.
        arr_players[cnt-1].typed = int(DATA[str(cnt)][3]) # assign the player-type.
        arr_players[cnt-1].cnt_init = int(DATA[str(cnt)][4]) # assign the initial count of forces.
        arr_players[cnt-1].trr_and_frc = (DATA[str(cnt)][5]) # assign the dictionary of "territory and force"
        arr_players[cnt-1].allies = (DATA[str(cnt)][6]) # assign the list of allies.
    #for cnt in range(0, len(arr_players), 1): # loop over the list of player-objects.
    #    print("AS FOR PLAYER NO." + str(cnt) + ":") # debug print
    #    print("ID NUMBER is: " + str(arr_players[cnt].id_num)) # debug print
    #    print("COLOR is: " + str(arr_players[cnt].color)) # debug print
    #    print("NAME is: " + str(arr_players[cnt].name)) # debug print
    #    print("TYPED is: " + str(arr_players[cnt].typed)) # debug print
    #    print("CNT_INIT is: " + str(arr_players[cnt].cnt_init)) # debug print
    #    print("TRR_AND_FRC is: " + str(arr_players[cnt].trr_and_frc)) # debug print
    #    print("ALLIES is: " + str(arr_players[cnt].allies)) # debug print
    #    print("------") # debug print
        


def load_arr_territories (arr_territories, DATA): # load the list of territory-objects
    cell = str(len(DATA)-2) # get the specific place from which we can locate the territory-data
    #print("lower edge is: " + str(int(DATA[cell][0])+1)) # ERROR!!!
    #print("upper edge is: " + str(int(DATA[cell][0])+int(DATA[cell][1])+1))
    for cnt in range(int(DATA[cell][0])+1, int(DATA[cell][0])+int(DATA[cell][1])+1, 1): # loop over the data where there's data regarding the territories
        arr_territories.append(Territory(0,0,0,0,0,0,0,0,0,0,0,0)) # append a territory-object to the list
        arr_territories[len(arr_territories)-1].id_num = int(DATA[str(cnt)][0]) # id_num
        arr_territories[len(arr_territories)-1].name = str(DATA[str(cnt)][1]) # name
        arr_territories[len(arr_territories)-1].pos = (DATA[str(cnt)][2]) # pos
        arr_territories[len(arr_territories)-1].blob_names = (DATA[str(cnt)][3]) # blob_names
        #arr_territories[len(arr_territories)-1].real_blobs = None
        arr_territories[len(arr_territories)-1].borders = (DATA[str(cnt)][4]) # borders
        arr_territories[len(arr_territories)-1].bonus_group = (DATA[str(cnt)][5]) # bonus_group
        arr_territories[len(arr_territories)-1].controller = int(DATA[str(cnt)][6]) # controller
        arr_territories[len(arr_territories)-1].force_no = (DATA[str(cnt)][7]) # force-no
        arr_territories[len(arr_territories)-1].dots = (DATA[str(cnt)][8]) # dots
        arr_territories[len(arr_territories)-1].text_force_point = (DATA[str(cnt)][9]) # numer-point
        #arr_territories[len(arr_territories)-1].screen = (0) # screen
    #for cnt in range(0, len(arr_territories), 1): # loop over the list of territories
        #print("AS FOR TERRITORY NO." + str(cnt) + ":") # debug print
        #print("ID NUMBER is: " + str(arr_territories[cnt].id_num)) # debug print
        #print("NAME is: " + str(arr_territories[cnt].name)) # debug print
        #print("POS is: " + str(arr_territories[cnt].pos)) # debug print
        #print("BLOB_NAMES is: " + str(arr_territories[cnt].blob_names)) # debug print
        #print("REAL_BLOBS is: " + str(arr_territories[cnt].real_blobs)) # debug print
        #print("BORDERS is: " + str(arr_territories[cnt].borders)) # debug print
        #print("BONUS_GROUP is: " + str(arr_territories[cnt].bonus_group)) # debug print
        #print("CONTROLLER is: " + str(arr_territories[cnt].controller)) # debug print
        #print("FORCE_NO is: " + str(arr_territories[cnt].force_no)) # debug print
        #print("DOTS is: " + str(arr_territories[cnt].dots)) # debug print
        #print("NUMBER_POINT is: " + str(arr_territories[cnt].text_force_point)) # debug print
        #print("SCREEN is: " + str(arr_territories[cnt].screen)) # debug print
        #print("------") # debug print

def load_map_number (DATA, back_mode, gui_text_levels): # function to load the map-number of the game
    cell = str(len(DATA)-2) # get the specific place from which we can locate the territory-data
    id_num = str(DATA[str(DATA[cell][0]+1)][0]) # get the ID-number if the map
    if (id_num == '0'): # if the ID number of the first territory in the map is 0, then...
        #game_map = load_game_map(1, back_mode)
        game_map = int(1) # 'countries' game-map
        load_gui_text_levels (gui_text_levels, 1) # load the gui-text positons of the 'countries' map
    elif (id_num == '42'): # if the ID number of the first territory in the map is 42, then...
        #game_map = load_game_map(2, back_mode)
        game_map = int(2) # 'hexagons' game-map
        load_gui_text_levels (gui_text_levels, 2) # load the gui-text positons of the 'hexagons' map
    elif (id_num == '98'): # if the ID number of the first territory in the map is 98, then...
        #game_map = load_game_map(3, back_mode)
        game_map = int(3) # 'pyramids' game-map
        load_gui_text_levels (gui_text_levels, 3) # load the gui-text positons of the 'pyramid' map
    elif (id_num == '162'): # if the ID number of the first territory in the map is 162, then...
        #game_map = load_game_map(4, back_mode)
        game_map = int(4) # 'quick-triangles' game-map
        load_gui_text_levels (gui_text_levels, 4) # load the gui-text positons of the 'quick-triangles' map
    elif (id_num == '166'): # if the ID number of the first territory in the map is 166, then...
        #game_map = load_game_map(5, back_mode)
        game_map = int(5) # 'serious-triangles' game-map
        load_gui_text_levels (gui_text_levels, 5) # load the gui-text positons of the 'serious-triangles' map
    elif (id_num == '198'): # if the ID number of the first territory in the map is 198, then...
        #game_map = load_game_map(6, back_mode)
        game_map = int(6) # 'squares' game-map
        load_gui_text_levels (gui_text_levels, 6) # load the gui-text positons of the 'squares' map
    elif (id_num == '234'): # if the ID number of the first territory in the map is 234, then...
        #game_map = load_game_map(7, back_mode)
        game_map = int(7) # 'stadium' game-map
        load_gui_text_levels (gui_text_levels, 7) # load the gui-text positons of the 'stadium' map
    elif (id_num == '266'): # if the ID number of the first territory in the map is 266, then...
        #game_map = load_game_map(8, back_mode)
        game_map = int(8) # 'keyboard' game-map
        load_gui_text_levels (gui_text_levels, 8) # load the gui-text positons of the 'keyboard' map
    return game_map

def load_gui_text_levels (arr_levels, selected_map): # function to load the gui-text dimentions 
    selected_map = int(selected_map) # stabilize the 'selected_map' variable-value to an integer.
    LEVELS = res_doc.find_one({"_id":(selected_map-1)}) # locate the matching "object" according to the map number.
    arr_levels[0].append(LEVELS["level_1"][0]) # get the 'x' position of the 1st dimentions
    arr_levels[0].append(LEVELS["level_1"][1]) # get the 'y' position of the 1st dimentions
    arr_levels[1].append(LEVELS["level_2"][0]) # get the 'x' position of the 2nd dimentions
    arr_levels[1].append(LEVELS["level_2"][1]) # get the 'y' position of the 2nd dimentions
    arr_levels[2].append(LEVELS["level_3"][0]) # get the 'x' position of the 3rd dimentions
    arr_levels[2].append(LEVELS["level_3"][1]) # get the 'y' position of the 3rd dimentions
    arr_levels[3].append(LEVELS["level_4"][0]) # get the 'x' position of the 4th dimentions
    arr_levels[3].append(LEVELS["level_4"][1]) # get the 'y' position of the 4th dimentions
    arr_levels[4].append(LEVELS["level_5"][0]) # get the 'x' position of the 5th dimentions
    arr_levels[4].append(LEVELS["level_5"][1]) # get the 'y' position of the 5th dimentions
    arr_levels[5].append(LEVELS["level_6"][0]) # get the 'x' position of the 6th dimentions
    arr_levels[5].append(LEVELS["level_6"][1]) # get the 'y' position of the 6th dimentions
    arr_levels[6].append(LEVELS["level_7"][0]) # get the 'x' position of the 7th dimentions
    arr_levels[6].append(LEVELS["level_7"][1]) # get the 'y' position of the 7th dimentions
    arr_levels[7].append(LEVELS["level_8"][0]) # get the 'x' position of the 8th dimentions
    arr_levels[7].append(LEVELS["level_8"][1]) # get the 'y' position of the 8th dimentions
    arr_levels[8].append(LEVELS["level_9"][0]) # get the 'x' position of the 9th dimentions
    arr_levels[8].append(LEVELS["level_9"][1]) # get the 'y' position of the 9th dimentions
    arr_levels[9].append(LEVELS["level_10"][0]) # get the 'x' position of the 10th dimentions
    arr_levels[9].append(LEVELS["level_10"][1]) # get the 'y' position of the 10th dimentions
    arr_levels[10].append(LEVELS["level_11"][0]) # get the 'x' position of the 11th dimentions
    arr_levels[10].append(LEVELS["level_11"][1]) # get the 'y' position of the 11th dimentions
    arr_levels[11].append(LEVELS["level_12"][0]) # get the 'x' position of the 12th dimentions
    arr_levels[11].append(LEVELS["level_12"][1]) # get the 'y' position of the 12th dimentions
    arr_levels[12].append(LEVELS["level_13"][0]) # get the 'x' position of the 13th dimentions
    arr_levels[12].append(LEVELS["level_13"][1]) # get the 'y' position of the 13th dimentions
    arr_levels[13].append(LEVELS["level_14"][0]) # get the 'x' position of the 14th dimentions
    arr_levels[13].append(LEVELS["level_14"][1]) # get the 'y' position of the 14th dimentions
    #print("arr_levels is: " + str(arr_levels)) # debug print
    #print("the level-1 LEVELS are: " + str(LEVELS["level_1"])) # debug print

#def load_game_map (map_select, back_mode): # this function loads the game maps.
#    back_mode = int(back_mode) # 'back-mode' is the color of the background (0=DARK / 1=LIGHT)
#    map_select = int(map_select) # the selected game-map (1/2/3/4/5/6/7/8)
#    if (back_mode == int(1)): #1=light, the 'light' version of the game maps.
#        if (map_select == int(1)):
#            game_map = pygame.image.load('countries (light).png')
#        elif (map_select == int(2)):
#            game_map = pygame.image.load('hexagons (light).png')
#        elif (map_select == int(3)):
#            game_map = pygame.image.load('pyramid (light).png')
#        elif (map_select == int(4)):
#            game_map = pygame.image.load('quick-triangles (light).png')
#        elif (map_select == int(5)):
#            game_map = pygame.image.load('serious-triangles (light).png')
#        elif (map_select == int(6)):
#            game_map = pygame.image.load('squares (light).png')
#        elif (map_select == int(7)):
#            game_map = pygame.image.load('stadium (light).png')
#        elif (map_select == int(8)):
#            game_map = pygame.image.load('keyboard (light).png')
#    else: # 0=dark, the 'dark' version of the game maps.
#        if (map_select == int(1)):
#            game_map = pygame.image.load('countries (dark).png')
#        elif (map_select == int(2)):
#            game_map = pygame.image.load('hexagons (dark).png')
#        elif (map_select == int(3)):
#            game_map = pygame.image.load('pyramid (dark).png')
#        elif (map_select == int(4)):
#            game_map = pygame.image.load('quick-triangles (dark).png')
#        elif (map_select == int(5)):
#            game_map = pygame.image.load('serious-triangles (dark).png')
#        elif (map_select == int(6)):
#            game_map = pygame.image.load('squares (dark).png')
#        elif (map_select == int(7)):
#            game_map = pygame.image.load('stadium (dark).png')
#        elif (map_select == int(8)):
#            game_map = pygame.image.load('keyboard (dark).png')
#    return game_map

def load_totals_data (totals, DATA): # function to get the ranges of ID number of territories in the map
    cell = str(len(DATA)-2) # get the specific place from which we can locate the territory-data
    #print("lower edge: " + str(int((DATA[str(DATA[str(cell)][0]+1)][0])))) # debug print
    #print("upper edge: " + str(int((DATA[str(DATA[str(cell)][0]+DATA[str(cell)][1])][0])))) # debug print
    #print("Before, totals is: " + str(totals)) # debug print
    totals[0] = (int(DATA[str(DATA[str(cell)][0]+1)][0])) # the ID-number of the first territory of the game-map
    totals[1] = (int(DATA[str(DATA[str(cell)][0]+DATA[str(cell)][1])][0])) # the ID-number of the last territory of the game-map
    #print("After, totals is: " + str(totals)) # debug print

def load_real_blobs (arr_territories): # function to load the 'blobs' (colored-PNG files).
    for cnt in range(0, len(arr_territories), 1): # loop over the list of territories
        arr_territories[cnt].load_blobs() # use the 'load_blobs' method of the territory object.

def get_data (code): # function to get the data (chunk-of-text) from the document of the MongoDB database.
    DATA = save_doc.find_one({"_id":(str(code))}) # locate the chunk-of-text (data) by code
    return DATA # return the chunk-of-text (data) to the function call.

def load_saved_game (code, back_mode, game_map, arr_players, arr_territories, totals, resolutions, gui_text_levels):
    DATA = get_data(code) # function to get the data (chunk-of-text) from the database.
    #print("BELOW IS THE DATA: ") # debug print
    #print("000000") # debug print
    #print(DATA) # debug print
    #print("000000") # debug print
    load_totals_data(totals, DATA) # load the ID-numbers of the first territory and of the last territory
    #print("The totals is: " + str(totals)) # debug print
    load_arr_players(arr_players, DATA) # load the list of player-objects
    game_map = load_map_number(DATA, back_mode, gui_text_levels) # load the map-number of the game
    load_arr_territories(arr_territories, DATA) # load the list of territory-objects
    load_real_blobs(arr_territories) # load the 'blobs' (colored-PNGs) of the territories
    #resolutions = [game_map.get_rect().size[0],game_map.get_rect().size[1]]
    return game_map # return the located game-map.