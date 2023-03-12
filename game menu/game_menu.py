# MODULES OF THE GAME:
import pygame
import pymongo
import time # exclusively for time.sleep function
import timeit # to calculate duration of loading time.
from pygame.event import * # import all the functions in 'pygame.event'.

# SUB-MODULES OF THE GAME:
from pymongo import MongoClient # this game is a client of the database

# CLASSES OF THE GAME:
from button_class import Button # the button class.
from territory_class import Territory # the territory class.
from player_class import Player # the player class.
from textbox_class import textBox # import the "textBox" class.
from guiText_class import gui_text # import the "gui_text" class.

# FUNCTIONS OF THE GAME:
from game_functions import * # import all the game functions
from game_loader import * # import all functions of game-load.
from game_saver import * # import all functions of game-save.

# this is the cluster - as exists in the MongoDB atlas.
cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"] # the variable is the entire database - as exists in the MongoDB atlas.
sv = cluster["pyrisk_sv"] # the variable is the entire database - as exists in the MongoDB atlas.

res_doc = db["pyrisk_resolutions"] # the document of resolutions (unique resolutions for each map of 8 maps)
total_doc = db["pyrisk_total_territories"] # the range of id-numbers of all territories that reside in a specific map (8 maps = 8 different options)
blob_links_doc = db["pyrisk_blob_links"] # "blobs" are the single-colored PNG that fill the void of the territories in the game-map, used to signifiy which territories belong to which player.
bonus_doc = db["pyrisk_bonus"] # when a player controlls all territories within a specified group - that player will receive a bonus number of forces to deploy for each of their playable turns.
borders_doc = db["pyrisk_borders"] # a player can only launch an attack from a territory to another territory if the ATTACKED territory has similar borders with the owned territory (from which the attack is launched).
dots_doc = db["pyrisk_dots"] # "dots" refer to the main system of the game to determine which territory has been selected for whatever in-game purpose (whether: reinforce, attack, move, etc').
force_doc = db["pyrisk_force_text"] # refers to the position in which the NUMBER of forces is displayed over the colored blob.
position_doc = db["pyrisk_positions"] # refers to positions in which the "blobs" will be 'printed' onto the game-map. The position is of (x,y) parameters.
general_doc = db["pyrisk_general"] # refers to a document that contains all data about all territories (CURRENTLY NOT IN USE).

save_doc = sv["saved_games"] # refers to the document that contains data of all saved games.

def load_game_map (map_select, back_mode): # this function loads the game maps.
    back_mode = int(back_mode) # 'back-mode' is the color of the background (0=DARK / 1=LIGHT)
    map_select = int(map_select) # the selected game-map (1/2/3/4/5/6/7/8)
    if (back_mode == int(1)): #1=light, the 'light' version of the game maps.
        if (map_select == int(1)): # if the selected-map is valued 1, then...
            game_map = pygame.image.load('countries (light).png') # load the light version of 'countries' map
        elif (map_select == int(2)): # if the selected-map is valued 2, then...
            game_map = pygame.image.load('hexagons (light).png') # load the light version of 'hexagons' map
        elif (map_select == int(3)): # if the selected-map is valued 3, then...
            game_map = pygame.image.load('pyramid (light).png') # load the light version of 'pyramid' map
        elif (map_select == int(4)): # if the selected-map is valued 4, then...
            game_map = pygame.image.load('quick-triangles (light).png') # load the light version of 'quick-triangles' map
        elif (map_select == int(5)): # if the selected-map is valued 5, then...
            game_map = pygame.image.load('serious-triangles (light).png') # load the light version of 'serious-triangles' map
        elif (map_select == int(6)): # if the selected-map is valued 6, then...
            game_map = pygame.image.load('squares (light).png') # load the light version of 'squares' map
        elif (map_select == int(7)): # if the selected-map is valued 7, then...
            game_map = pygame.image.load('stadium (light).png') # load the light version of 'stadium' map
        elif (map_select == int(8)): # if the selected-map is valued 8, then...
            game_map = pygame.image.load('keyboard (light).png') # load the light version of 'keyboard' map
    else: # 0=dark, the 'dark' version of the game maps.
        if (map_select == int(1)): # if the selected-map is valued 1, then...
            game_map = pygame.image.load('countries (dark).png') # load the dark version of 'countries' map
        elif (map_select == int(2)): # if the selected-map is valued 1, then...
            game_map = pygame.image.load('hexagons (dark).png') # load the dark version of 'hexagons' map
        elif (map_select == int(3)): # if the selected-map is valued 1, then...
            game_map = pygame.image.load('pyramid (dark).png') # load the dark version of 'pyramid' map
        elif (map_select == int(4)): # if the selected-map is valued 1, then...
            game_map = pygame.image.load('quick-triangles (dark).png') # load the dark version of 'quick-triangles' map
        elif (map_select == int(5)): # if the selected-map is valued 1, then...
            game_map = pygame.image.load('serious-triangles (dark).png') # load the dark version of 'serious-triangles' map
        elif (map_select == int(6)): # if the selected-map is valued 1, then...
            game_map = pygame.image.load('squares (dark).png') # load the dark version of 'squares' map
        elif (map_select == int(7)): # if the selected-map is valued 1, then...
            game_map = pygame.image.load('stadium (dark).png') # load the dark version of 'stadium' map
        elif (map_select == int(8)): # if the selected-map is valued 1, then...
            game_map = pygame.image.load('keyboard (dark).png') # load the dark version of 'keyboard' map
    return game_map # return the loaded map

def clean_screen(back_mode): # this function 'clears' the game-window.
    back_mode = int(back_mode) # 'back-mode' is the color of the background (0=DARK / 1=LIGHT)
    try: # acknowledging the fact that this may not work.
        if (back_mode == int(0)): #0=DARK
            screen.fill((0,0,0)) # fill it with 'pure' black
        else: # 1=LIGHT
            screen.fill((255,255,255)) # fill it with 'pure' white
    except: # irrelevant
        pass # 'placebo'

def load_menus (back_mode): # this function loads the PNG files of the menus (each menu = 1 PNG file).
    back_mode = int(back_mode) # 'back-mode' is the color of the background (0=DARK / 1=LIGHT)
    if (back_mode == int(0)): #0=DARK
        # will load all the 'dark-versions' of the menus.
        menu0 = pygame.image.load('menu0dark.png') # load the 'light' version of menu-0 into the variable
        menu2 = pygame.image.load('menu2dark.png') # load the 'light' version of menu-2 into the variable
        menu3 = pygame.image.load('menu3dark.png') # load the 'light' version of menu-3 into the variable
        menu4 = pygame.image.load('menu4dark.png') # load the 'light' version of menu-4 into the variable
        menu5 = pygame.image.load('menu5dark.png') # load the 'light' version of menu-5 into the variable
        menu6 = pygame.image.load('menu6dark.png') # load the 'light' version of menu-6 into the variable
    else: #1=LIGHT
        # will load all the 'light-versions' of the menus.
        menu0 = pygame.image.load('menu0light.png') # load the 'light' version of menu-0 into the variable
        menu2 = pygame.image.load('menu2light.png') # load the 'light' version of menu-2 into the variable
        menu3 = pygame.image.load('menu3light.png') # load the 'light' version of menu-3 into the variable
        menu4 = pygame.image.load('menu4light.png') # load the 'light' version of menu-4 into the variable
        menu5 = pygame.image.load('menu5light.png') # load the 'light' version of menu-5 into the variable
        menu6 = pygame.image.load('menu6light.png') # load the 'light' version of menu-6 into the variable
    return menu0, menu2, menu3, menu4, menu5, menu6

def get_resolutions (res_arr, selected_map): # this function gets the resolution-data from the database - in accordance to the selected map.
    selected_map = int(selected_map) # stablize the variable to be an integer (not a float!)
    arr_res = res_doc.find_one({"_id":(selected_map-1)}) #  assign the results from the database to the variable
    arr_res = arr_res["res"] # assign the actual-resolutions of the results from the database to the variable.

#def load_gui_text_levels (arr_levels, selected_map):
#    selected_map = int(selected_map)
#    LEVELS = res_doc.find_one({"_id":(selected_map-1)}) # locate the matching "object" according to the map number.
#    arr_levels[0].append(LEVELS["level_1"][0])
#    arr_levels[0].append(LEVELS["level_1"][1])
#    arr_levels[1].append(LEVELS["level_2"][0])
#    arr_levels[1].append(LEVELS["level_2"][1])
#    arr_levels[2].append(LEVELS["level_3"][0])
#    arr_levels[2].append(LEVELS["level_3"][1])
#    arr_levels[3].append(LEVELS["level_4"][0])
#    arr_levels[3].append(LEVELS["level_4"][1])
#    arr_levels[4].append(LEVELS["level_5"][0])
#    arr_levels[4].append(LEVELS["level_5"][1])
#    arr_levels[5].append(LEVELS["level_6"][0])
#    arr_levels[5].append(LEVELS["level_6"][1])
#    arr_levels[6].append(LEVELS["level_7"][0])
#    arr_levels[6].append(LEVELS["level_7"][1])
#    arr_levels[7].append(LEVELS["level_8"][0])
#    arr_levels[7].append(LEVELS["level_8"][1])
#    arr_levels[8].append(LEVELS["level_9"][0])
#    arr_levels[8].append(LEVELS["level_9"][1])
#    arr_levels[9].append(LEVELS["level_10"][0])
#    arr_levels[9].append(LEVELS["level_10"][1])
#    arr_levels[10].append(LEVELS["level_11"][0])
#    arr_levels[10].append(LEVELS["level_11"][1])
#    arr_levels[11].append(LEVELS["level_12"][0])
#    arr_levels[11].append(LEVELS["level_12"][1])
#    arr_levels[12].append(LEVELS["level_13"][0])
#    arr_levels[12].append(LEVELS["level_13"][1])
#    arr_levels[13].append(LEVELS["level_14"][0])
#    arr_levels[13].append(LEVELS["level_14"][1])
#    print("arr_levels is: " + str(arr_levels))
#    print("the level-1 LEVELS are: " + str(LEVELS["level_1"]))


# COLORS: (those that are relevant in the game) (NOT IN USE)
# IN-GAME player colors:
# GREEN = (34,139,34)
# BLUE = (0,95,190)
# YELLOW = (251,219,3)
# RED = (251,28,46)
# ORANGE = (255,102,0)
# PURPLE = (66,12,76)
# GREY = (110,110,110)
# BLACK = (0,0,0)

def load_menu_0(back_mode, menu, arr_players, arr_territories, resolutions, totals, gui_text_levels, assignType, game_map, enSave): # LOAD CODE MENU - the menu in which the saved game is loaded from the database.
    code = str("") # the code starts as an empty string.
    screen.blit(menu0, (0,0)) # stick the PNG file of the 'load-screen' menu.
    pygame.display.update() # refresh the pygame window.
    back_button = Button(3, "BACK", back_mode, (50,570,200,100), 5, 1, 0, screen) # initiate the 'back' button
    submit_button = Button(1, "SUBMIT", back_mode, (900,230,160,80), 5, 1, 0, screen) # initiate the 'submit' button
    game_code = textBox((340,260,400,50), 11, back_mode, 1, 5, screen,340, code) # define the textbox of the saved-game password
    game_code.initiate_text_box() # initiate the game_code button.
    while (menu == int(0)): # as long as the menu-screen is 0 - the 'saved-game-loading' menu, then...
        for event in pygame.event.get(): # get pygame events.
            mouse = pygame.mouse.get_pos() # get (x,y) positions of the mouse.
            menu = back_button.button_functional(menu) # make the 'back' button functional (according to a local function in the 'button-class').
            code = submit_button.button_functional(code) # make the 'submit' button functional (according to a local function in the 'button-class').
            game_code.on_hover_text_box() # determine if the text-box is being hovered on by the mouse.
            submit_button.value = game_code.strr # assign the game-code string to the string-value of the submit-button object.
            if (len(code) == int(5)): # if the entered code is of length 11, then...
                game_map = load_saved_game(code, back_mode, game_map, arr_players, arr_territories, totals, resolutions, gui_text_levels) # send all critical parameters to the 'load_saved_game' function.
                game_map = load_game_map(game_map, back_mode) # will load the number of the game-map
                resolutions = [game_map.get_rect().size[0],game_map.get_rect().size[1]] # will load the resolutions of the saved game.
                assignType = int(1) # will determine that the assignType is 1, which means "AUTO ASSIGN".
                menu = int(7) # after menu-0 (load-menu) - get to menu-7 (actual-game)
                enSave = int(1) # will determine that enSave is 1, which means to "ENABLE SAVE".
                #code = "abc"
                break # break - leave the "while" loop.
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()
                exit(0)
    #print("IN LOAD MENU - the 'assignType' is: " + str(assignType))
    #print("the length of arr_territories is: " + str(len(arr_territories)))
    #print("the resolutions is: " + str(resolutions))
    return menu, assignType, game_map, resolutions, enSave # return the value of the menu.



def load_menu_1 (back_mode, menu): # LOGO MENU - the menu of the game-logo + decide over the color-mode of the game
    #back_mode = int(-1)
    if (back_mode == int(1)): #1=LIGHT
        menu1 = pygame.image.load('menu1light.png') # load the "light" version of the 1st game-menu.
    else: #0=DARK
        menu1 = pygame.image.load('menu1dark.png') # load the "dark" version of the 1st game-menu.
    screen.blit(menu1, (0,0)) # stick the PNG file of the 'logo-screen' menu.
    light_button = Button(3, "LIGHT", back_mode,(200,250,300,200),5, 1, 0, screen) # define the "light-button"
    dark_button = Button(3, "DARK", back_mode,(600,250,300,200), 5, 0, 0, screen) # define the "dark-button"
    proceed_button = Button(3, "PROCEED", back_mode,(350,570,400,100),5, 2, 0, screen) # define the "proceed" button
    load_button = Button(1, "LOAD GAME", back_mode, (850,570,200,100), 5, 0, 0, screen) # define the "load-game" button
    #pygame.display.update()
    #back_mode = int(-1)
    while (menu == int(1)): # as long as the menu-screen is 1 - the 'saved-game-loading' menu, then...
        for event in pygame.event.get():  # get pygame events.
            mouse = pygame.mouse.get_pos() # get (x,y) positions of the mouse.
            back_mode = light_button.button_functional(back_mode) # make "light" button functional.
            back_mode = dark_button.button_functional(back_mode) # make "dark" button functional.
            menu = load_button.button_functional(menu) # make "load button" functional.
            if (back_mode != int(-1)): # back-mode must be either "light" / "dark" in order to procede.
                menu = proceed_button.button_functional(menu) # make "proceed" button functional.
                menu = load_button.button_functional(menu) # make "load" button functional.
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()
                exit(0)
    return menu, back_mode # return menu-number AND type of backmode (0=DARK / 1=LIGHT)

def load_menu_2 (back_mode, menu, selected_map): # PLYAER-MENU - select the game-map (select only 1 out of 8)
    selected_map = int(-1) # currently - there is no selected map (selected map can by numbers 1-8)
    screen.blit(menu2, (0,0)) # apply menu-PNG onto the PyGame window.
    arr_mini_maps = [0]*8 # define the array of mini-maps, each map having a single cell.
    if (back_mode == int(0)): # 0=DARK
        arr_mini_maps = ["map1dark.png","map2dark.png","map3dark.png","map4dark.png","map5dark.png","map6dark.png","map7dark.png","map8dark.png"] # define all names of maps
    else:
        arr_mini_maps = ["map1light.png","map2light.png","map3light.png","map4light.png","map5light.png","map6light.png","map7light.png","map8light.png"] # define all names of maps
    map1_button = Button(3, "", back_mode, (20, 175,240,175), 5, 1, arr_mini_maps[0], screen) # initiate the "countries-map" button
    map2_button = Button(3, "", back_mode, (290,175,240,175), 5, 2, arr_mini_maps[1], screen) # initiate the "hexagons-map" button
    map3_button = Button(3, "", back_mode, (560,175,240,175), 5, 3, arr_mini_maps[2], screen) # initiate the "pyramid-map" button
    map4_button = Button(3, "", back_mode, (830,175,240,175), 5, 4, arr_mini_maps[3], screen) # initiate the "quick-triangles-map" button
    map5_button = Button(3, "", back_mode, (20,365,240,175), 5, 5, arr_mini_maps[4], screen) # initiate the "serious-triangles-map" button
    map6_button = Button(3, "", back_mode, (290,365,240,175), 5, 6, arr_mini_maps[5], screen) # initiate the "squares-map" button
    map7_button = Button(3, "", back_mode, (560,365,240,175), 5, 7, arr_mini_maps[6], screen) # initiate the "stadium-map" button
    map8_button = Button(3, "", back_mode, (830,365,240,175), 5, 8, arr_mini_maps[7], screen) # initiate the "keyboard-map" button
    proceed_button = Button(3, "PROCEED", back_mode, (350,570,400,100), 5, 3, 0, screen) # initiate the "proceed" button.
    back_button = Button(3, "BACK", back_mode, (50,570,200,100), 5, 1, 0, screen) # initiate the "back" button.
    pygame.display.update() # refresh the pygame-window.
    while (menu == int(2)): # while the current menu is "map-select", then:
        for event in pygame.event.get(): # get the pygame event.
            mouse = pygame.mouse.get_pos() # get the position (x,y) coordinates of the mouse.
            selected_map = map1_button.button_functional(selected_map) # initiate functionality of "countries-map" button.
            selected_map = map2_button.button_functional(selected_map) # initiate functionality of "hexagons-map" button.
            selected_map = map3_button.button_functional(selected_map) # initiate functionality of "pyramid-map" button.
            selected_map = map4_button.button_functional(selected_map) # initiate functionality of "quick-triangles-map" button.
            selected_map = map5_button.button_functional(selected_map) # initiate functionality of "serious-triangles-map" button.
            selected_map = map6_button.button_functional(selected_map) # initiate functionality of "squares-map" button.
            selected_map = map7_button.button_functional(selected_map) # initiate functionality of "stadium-map" button.
            selected_map = map8_button.button_functional(selected_map) # initiate functionality of "keyboard-map" button.
            menu = back_button.button_functional(menu) # initiate functionality of "back" button.
            if (selected_map != int(-1)): # if "game-map" has been selected.
                menu = proceed_button.button_functional(menu) # initiate functionality of "proceed" button.
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()
                exit(0)
    #print("THE SELECTED MAP IS: " + str(selected_map))
    return menu, selected_map # return both menu-number and number of selected game-map.

def load_menu_3 (back_mode, menu, player_select, selected_map, enSave): # selection of number of players / humans / computers.
    player_select = [-1,-1,-8] # 1st cell is human-no, 2nd cell is computer-no, 3rd cell is total-players. 
    screen.blit(menu3, (0,0)) # load the menu of the player-select menu.
    pygame.display.update() # update the pygame window.
    lv0_gt = gui_text("", 40, 0, (800,70, 1, 40), screen) # this is the header: "FORTIFY" / "ATTACK" / "MOVE"
    lv1_gt = gui_text("", 40, 0, (800,100, 1, 40), screen) # this is the header: "FORTIFY" / "ATTACK" / "MOVE"
    lv2_gt = gui_text("", 40, 0, (800,130, 1, 40), screen) # this is the header: "FORTIFY" / "ATTACK" / "MOVE"

    two_players = Button(3, "2", back_mode, (115,115,130,80), 5, 2, 0, screen) # initiate the "2-players" button.
    three_players = Button(3, "3", back_mode, (298,115,130,80), 5, 3, 0, screen) # initiate the "3-players" button.
    four_players = Button(3, "4", back_mode, (482,115,130,80), 5, 4, 0, screen) # initiate the "4-players" button.
    five_players = Button(3, "5", back_mode, (665,115,130,80), 5, 5, 0, screen) # initiate the "5-players" button.
    six_players = Button(3, "6", back_mode, (848,115,130,80), 5, 6, 0, screen) # initiate the "6-players" button.
    
    zero_human = Button(3, "0", back_mode, (415,315,70,50), 5, 0, 0, screen) # initiate the "0-human" button.
    one_human = Button(3, "1", back_mode, (515,315,70,50), 5, 1, 0, screen) # initiate the "1-human" button.
    two_human = Button(3, "2", back_mode, (615,315,70,50), 5, 2, 0, screen) # initiate the "2-human" button.
    three_human = Button(3, "3", back_mode, (715,315,70,50), 5, 3, 0, screen) # initiate the "3-human" button.
    four_human = Button(3, "4", back_mode, (815,315,70,50), 5, 4, 0, screen) # initiate the "4-human" button.
    five_human = Button(3, "5", back_mode, (915,315,70,50), 5, 5, 0, screen) # initiate the "5-human" button.
    six_human = Button(3, "6", back_mode, (1015,315,70,50), 5, 6, 0, screen) # initiate the "6-human" button.
    
    zero_comp = Button(3, "0", back_mode, (415,398,70,50), 5, 0, 0, screen) # initiate the "0-computer" button.
    one_comp = Button(3, "1", back_mode, (515,398,70,50), 5, 1, 0, screen) # initiate the "1-computer" button.
    two_comp = Button(3, "2", back_mode, (615,398,70,50), 5, 2, 0, screen) # initiate the "2-computer" button.
    three_comp = Button(3, "3", back_mode, (715,398,70,50), 5, 3, 0, screen) # initiate the "3-computer" button.
    four_comp = Button(3, "4", back_mode, (815,398,70,50), 5, 4, 0, screen) # initiate the "4-computer" button.
    five_comp = Button(3, "5", back_mode, (915,398,70,50), 5, 5, 0, screen) # initiate the "5-computer" button.
    six_comp = Button(3, "6", back_mode, (1015,398,70,50), 5, 6, 0, screen) # initiate the "6-computer" button.
    
    if (selected_map == int(4)):
            five_players.draw_button_cross() # place an 'X' over the "five-players" button.
            six_players.draw_button_cross() # place an 'X' over the "six-players" button.
            five_human.draw_button_cross() # place an 'X' over the "five-human" button.
            six_human.draw_button_cross() # place an 'X' over the "six-human" button.
            five_comp.draw_button_cross() # place an 'X' over the "five-computer" button.
            six_comp.draw_button_cross() # place an 'X' over the "six-computer" button.
    yes_save = Button(3, "YES", back_mode, (745,480,130,80), 5, 1, 0, screen) # initiate the "yes-save" button
    no_save = Button(3, "NO", back_mode, (950,480,130,80), 5, 0, 0, screen) # initiate the "no-save" button
    proceed_button = Button(3, "PROCEED", back_mode, (350,570,400,100), 5, 4, 0, screen) # initiate the "proceed" button.
    back_button = Button(3, "BACK", back_mode, (50,570,200,100), 5, 2, 0, screen) # initiate the "back" button.
    pygame.display.update() # refresh the pygame window.
    while (menu == int(3)): # which the manu is at "player-number + passcode selection" menu, then:
        for event in pygame.event.get(): # get the pygame event
            mouse = pygame.mouse.get_pos() # get the mouse position (x,y) coordinates.
            player_select[2] = two_players.button_functional(player_select[2]) # initiate functionality of "2-players" button.
            player_select[2] = three_players.button_functional(player_select[2]) # initiate functionality of "3-players" button.
            player_select[2] = four_players.button_functional(player_select[2]) # initiate functionality of "4-players" button.
            if (selected_map != int(4)): # if the selected-map is all but "quick-triangles" (only 4 territories), then...
                player_select[2] = five_players.button_functional(player_select[2]) # initiate functionality of "5-players" button.
                player_select[2] = six_players.button_functional(player_select[2]) # initiate functionality of "6-players" button.
            player_select[0] = zero_human.button_functional(player_select[0]) # initiate functionality of "0-humans" button.
            player_select[0] = one_human.button_functional(player_select[0]) # initiate functionality of "1-humans" button.
            player_select[0] = two_human.button_functional(player_select[0]) # initiate functionality of "2-humans" button.
            player_select[0] = three_human.button_functional(player_select[0]) # initiate functionality of "3-humans" button.
            player_select[0] = four_human.button_functional(player_select[0]) # initiate functionality of "4-humans" button.
            if (selected_map != int(4)): # if the selected-map is all but "quick-triangles" (only 4 territories), then... ######
                player_select[0] = five_human.button_functional(player_select[0]) # initiate functionality of "5-humans" button.
                player_select[0] = six_human.button_functional(player_select[0]) # initiate functionality of "6-humans" button.
            player_select[1] = zero_comp.button_functional(player_select[1]) # initiate functionality of "0-computers" button.
            player_select[1] = one_comp.button_functional(player_select[1]) # initiate functionality of "1-computers" button.
            player_select[1] = two_comp.button_functional(player_select[1]) # initiate functionality of "2-computers" button.
            player_select[1] = three_comp.button_functional(player_select[1]) # initiate functionality of "3-computers" button.
            player_select[1] = four_comp.button_functional(player_select[1]) # initiate functionality of "4-computers" button.
            if (selected_map != int(4)):  # if the selected-map is all but "quick-triangles" (only 4 territories), then... ######
                player_select[1] = five_comp.button_functional(player_select[1]) # initiate functinality of "5-computers" button.
                player_select[1] = six_comp.button_functional(player_select[1]) # initiate functionality of "6-computers" button.
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()
                exit(0)
            enSave = yes_save.button_functional(enSave) # initiate functionality of "yes-save" button.
            enSave = no_save.button_functional(enSave) # initiate functionality of "no-save" button.
            menu = back_button.button_functional(menu) # initiate functionality of "back" button.


            if ((player_select[0] + player_select[1] == player_select[2]) and (enSave != -1)): # only if no-humans + no-computer = no-players, then:
                menu = proceed_button.button_functional(menu) # initiate functionality of "proceed" button.
    return menu, player_select, enSave # return value of "menu".

def load_menu_4 (back_mode, menu, player_select, arr_colors, arr_names): # selection of colors and names of each of the players
    screen.blit(menu4, (0,0)) # load the menu of the color/name selection of the players.
    arr_colors = [-1]*player_select[2] # all colors are -1, which is a neutral number, and will change as the selection takes place.
    #print("length of arr_colors is: " + str(len(arr_colors))) # debug print
    #color_display = [(34,139,34),(0,95,190),(251,219,3),(251,28,46),(255,102,0),(66,12,76)] # not used
    pygame.display.update() # refresh the pygame window.0
    proceed_button = Button(3, "PROCEED", back_mode, (350,570,400,100), 5, 5, 0, screen) # initiate the 'proceed' button
    back_button = Button(3, "BACK", back_mode, (50,570,200,100), 5, 3, 0, screen) # initiate the 'back' button

    initiate_arr_names(arr_names, player_select) # initiate the array of names-of-players.

    if (player_select[2] >= int(2)): # if we have 2 players or more, then (for now) produce 2 rows of colors.
        # FIRST ROW OF COLORS.
        # def __init__ (self, arr_dem, length, color, font, thick, screen, level, strr):
        #game_code = textBox((340,260,400,50), 11, back_mode, 1, 5, screen,340, code)
        name_text_box_1 = textBox((60,100,240,60), 7, back_mode, 1, 5, screen, 60, arr_names[0]) # define text-box for the name of 1st player.
        name_text_box_1.initiate_text_box() # initiate text-box for the name of 1st player.
        name_text_box_1.reset_string() # reset the string-name of 1st player.
        colored_button_1_1 = Button(3, "", back_mode, (360,100,100,60), 5, 0, "green-button.png", screen) # green-button for 1st player.
        colored_button_1_2 = Button(3, "", back_mode, (480,100,100,60), 5, 1, "blue-button.png", screen) # blue-button for 1st player.
        colored_button_1_3 = Button(3, "", back_mode, (600,100,100,60), 5, 2, "yellow-button.png", screen) # yellow-button for 1st player. 
        colored_button_1_4 = Button(3, "", back_mode, (720,100,100,60), 5, 3, "red-button.png", screen) # red-button for 1st player.
        colored_button_1_5 = Button(3, "", back_mode, (840,100,100,60), 5, 4, "orange-button.png", screen) # orange-button for 1st player.
        colored_button_1_6 = Button(3, "", back_mode, (960,100,100,60), 5, 5, "purple-button.png", screen) # purple-button for 1st player.

        # SECOND ROW OF COLORS.
        name_text_box_2 = textBox((60,180,240,60), 7, back_mode, 1, 5, screen, 60, arr_names[1]) # define text-box for the name of 2nd player.
        name_text_box_2.initiate_text_box() # initiate text-box for the name of 1st player.
        name_text_box_2.reset_string() # reset the string-name of 1st player.
        colored_button_2_1 = Button(3, "", back_mode, (360,180,100,60), 5, 0, "green-button.png", screen) # green-button for 2nd player.
        colored_button_2_2 = Button(3, "", back_mode, (480,180,100,60), 5, 1, "blue-button.png", screen) # blue-button for 2nd player.
        colored_button_2_3 = Button(3, "", back_mode, (600,180,100,60), 5, 2, "yellow-button.png", screen) # yellow-button for 2nd player.
        colored_button_2_4 = Button(3, "", back_mode, (720,180,100,60), 5, 3, "red-button.png", screen) # red-button for 2nd player.
        colored_button_2_5 = Button(3, "", back_mode, (840,180,100,60), 5, 4, "orange-button.png", screen) # orange-button for 2nd player.
        colored_button_2_6 = Button(3, "", back_mode, (960,180,100,60), 5, 5, "purple-button.png", screen) # purple-button for 2nd player.

    if (player_select[2] >= int(3)): # if we have 3 players or more, then (for now) produce 1 more row of colors.
        # THIRD ROW OF COLORS.
        name_text_box_3 = textBox((60,260,240,60), 7, back_mode, 1, 5, screen, 60, arr_names[2]) # define text-box for the name of 3rd player.
        name_text_box_3.initiate_text_box() # initiate text-box for the name of 3rd player.
        name_text_box_3.reset_string() # reset the string-name of 3rd player.
        colored_button_3_1 = Button(3, "", back_mode, (360,260,100,60), 5, 0, "green-button.png", screen) # green-button for 3rd player.
        colored_button_3_2 = Button(3, "", back_mode, (480,260,100,60), 5, 1, "blue-button.png", screen) # blue-button for 3rd player.
        colored_button_3_3 = Button(3, "", back_mode, (600,260,100,60), 5, 2, "yellow-button.png", screen) # yellow-button for 3rd player.
        colored_button_3_4 = Button(3, "", back_mode, (720,260,100,60), 5, 3, "red-button.png", screen) # red-button for 3rd player.
        colored_button_3_5 = Button(3, "", back_mode, (840,260,100,60), 5, 4, "orange-button.png", screen) # orange-button for 3rd player.
        colored_button_3_6 = Button(3, "", back_mode, (960,260,100,60), 5, 5, "purple-button.png", screen) # purple-button for 3rd player.

    if (player_select[2] >= int(4)): # if we have 4 players or more, then (for now) produce 1 more row of colors.
        # FOURTH ROW OF COLORS.
        name_text_box_4 = textBox((60,340,240,60), 7, back_mode, 1, 5, screen, 60, arr_names[3]) # define text-box for the name of 4th player.
        name_text_box_4.initiate_text_box() # initiate text-box for the name of 4th player.
        name_text_box_4.reset_string() # reset the string-name of 4th player.
        colored_button_4_1 = Button(3, "", back_mode, (360,340,100,60), 5, 0, "green-button.png", screen) # green-button for 4th player. 
        colored_button_4_2 = Button(3, "", back_mode, (480,340,100,60), 5, 1, "blue-button.png", screen) # blue-button for 4th player.
        colored_button_4_3 = Button(3, "", back_mode, (600,340,100,60), 5, 2, "yellow-button.png", screen) # yellow-button for 4th player.
        colored_button_4_4 = Button(3, "", back_mode, (720,340,100,60), 5, 3, "red-button.png", screen) # red-button for 4th player.
        colored_button_4_5 = Button(3, "", back_mode, (840,340,100,60), 5, 4, "orange-button.png", screen) # orange-button for 4th player.
        colored_button_4_6 = Button(3, "", back_mode, (960,340,100,60), 5, 5, "purple-button.png", screen) # purple-button for 4th player.

    if (player_select[2] >= int(5)): # if we have 5 players or more, then (for now) produce 1 more row of colors.
        # FIFTH ROW OF COLORS.
        name_text_box_5 = textBox((60,420,240,60), 7, back_mode, 1, 5, screen, 60, arr_names[4]) # define text-box for the name of 5th player.
        name_text_box_5.initiate_text_box() # initiate text-box for the name of 5th player.
        name_text_box_5.reset_string() # reset the string-name of 5th player.
        colored_button_5_1 = Button(3, "", back_mode, (360,420,100,60), 5, 0, "green-button.png", screen) # green-button for 5th player.
        colored_button_5_2 = Button(3, "", back_mode, (480,420,100,60), 5, 1, "blue-button.png", screen) # blue-button for 5th player.
        colored_button_5_3 = Button(3, "", back_mode, (600,420,100,60), 5, 2, "yellow-button.png", screen) # yellow-button for 5th player.
        colored_button_5_4 = Button(3, "", back_mode, (720,420,100,60), 5, 3, "red-button.png", screen) # red-button for 5th player.
        colored_button_5_5 = Button(3, "", back_mode, (840,420,100,60), 5, 4, "orange-button.png", screen) # orange-button for 5th player.
        colored_button_5_6 = Button(3, "", back_mode, (960,420,100,60), 5, 5, "purple-button.png", screen) # purple-button for 5th player.

    if (player_select[2] >= int(6)): # if we have 6 players or more, then (for now) produce 1 more row of colors.
        # SIXTH ROW OF COLORS.
        name_text_box_6 = textBox((60,500,240,60), 7, back_mode, 1, 5, screen, 60, arr_names[5]) # define text-box for the name of 6th player.
        name_text_box_6.initiate_text_box() # initiate text-box for the name of 6th player.
        name_text_box_6.reset_string() # reset the string-gname of the 6th palyer.
        colored_button_6_1 = Button(3, "", back_mode, (360,500,100,60), 5, 0, "green-button.png", screen) # green-button for 6th player.
        colored_button_6_2 = Button(3, "", back_mode, (480,500,100,60), 5, 1, "blue-button.png", screen) # blue-button for 6th player.
        colored_button_6_3 = Button(3, "", back_mode, (600,500,100,60), 5, 2, "yellow-button.png", screen) # yellow-button for 6th player.
        colored_button_6_4 = Button(3, "", back_mode, (720,500,100,60), 5, 3, "red-button.png", screen) # red-button for 6th player.
        colored_button_6_5 = Button(3, "", back_mode, (840,500,100,60), 5, 4, "orange-button.png", screen) # orange-button for 6th player.
        colored_button_6_6 = Button(3, "", back_mode, (960,500,100,60), 5, 5, "purple-button.png", screen) # purple-button for 6th player.

    while (menu == int(4)): # while we're at the color/name selection menu.
        for event in pygame.event.get(): # get the pygame event
            mouse = pygame.mouse.get_pos() # get the mouse position (x,y) coordinates.
            #print("PLAYER SELECT IS: " + str(player_select)) # debug print
            menu = back_button.button_functional(menu) # make 'back' button functional.
            if (player_select[2] >= int(2)): # if we have 2 or more players, make all 12 color buttons functional.
                name_text_box_1.on_hover_text_box() # check button-hover over text-box of 1st-player.
                arr_names[0] = name_text_box_1.strr # assign value of class-string to 1st cell of array-of-names.
                #print("arr_names[0] is: " + str(arr_names[0])) # debug print
                name_text_box_2.on_hover_text_box() # check button-hover over text-box of 2nd-player.
                arr_names[1] = name_text_box_2.strr # assign value of class-string to 2nd cell of array-of-names.
                #print("arr_names[1] is: " + str(arr_names[1])) # debug print
                arr_colors[0] = colored_button_1_1.button_functional(arr_colors[0]) # initiate functionality of "1st-green-button"
                arr_colors[0] = colored_button_1_2.button_functional(arr_colors[0]) # initiate functionality of "1st-blue-button"
                arr_colors[0] = colored_button_1_3.button_functional(arr_colors[0]) # initiate functionality of "1st-yellow-button"
                arr_colors[0] = colored_button_1_4.button_functional(arr_colors[0]) # initiate functionality of "1st-red-button"
                arr_colors[0] = colored_button_1_5.button_functional(arr_colors[0]) # initiate functionality of "1st-orange-button"
                arr_colors[0] = colored_button_1_6.button_functional(arr_colors[0]) # initiate functionality of "1st-purple-button"
                arr_colors[1] = colored_button_2_1.button_functional(arr_colors[1]) # initiate functionality of "2nd-green-button"
                arr_colors[1] = colored_button_2_2.button_functional(arr_colors[1]) # initiate functionality of "2nd-blue-button"
                arr_colors[1] = colored_button_2_3.button_functional(arr_colors[1]) # initiate functionality of "2nd-yellow-button"
                arr_colors[1] = colored_button_2_4.button_functional(arr_colors[1]) # initiate functionality of "2nd-red-button"
                arr_colors[1] = colored_button_2_5.button_functional(arr_colors[1]) # initiate functionality of "2nd-orange-button"
                arr_colors[1] = colored_button_2_6.button_functional(arr_colors[1]) # initiate functionality of "2nd-purple-button"
            if (player_select[2] >= int(3)): # if we have 3 or more players, make additional 6 color buttons functional.
                name_text_box_3.on_hover_text_box() # check button-hover over text-box of 3rd-player.
                arr_names[2] = name_text_box_3.strr # assign value of class-string to 3rd cell of array-of-names.
                #print("arr_names[1] is: " + str(arr_names[1]))
                arr_colors[2] = colored_button_3_1.button_functional(arr_colors[2]) # initiate functionality of "3rd-green-button"
                arr_colors[2] = colored_button_3_2.button_functional(arr_colors[2]) # initiate functionality of "3rd-blue-button"
                arr_colors[2] = colored_button_3_3.button_functional(arr_colors[2]) # initiate functionality of "3rd-yellow-button"
                arr_colors[2] = colored_button_3_4.button_functional(arr_colors[2]) # initiate functionality of "3rd-red-button"
                arr_colors[2] = colored_button_3_5.button_functional(arr_colors[2]) # initiate functionality of "3rd-orange-button"
                arr_colors[2] = colored_button_3_6.button_functional(arr_colors[2]) # initiate functionality of "3rd-purple-button"
            if (player_select[2] >= int(4)): # if we have 4 or more players, make additional 6 color buttons functional.
                name_text_box_4.on_hover_text_box() # check button-hover over text-box of 4th-player.
                arr_names[3] = name_text_box_4.strr # assign value of class-string to 4rd cell of array-of-names.
                #print("arr_names[1] is: " + str(arr_names[1]))
                arr_colors[3] = colored_button_4_1.button_functional(arr_colors[3]) # initiate functionality of "4th-green-button"
                arr_colors[3] = colored_button_4_2.button_functional(arr_colors[3]) # initiate functionality of "4th-blue-button"
                arr_colors[3] = colored_button_4_3.button_functional(arr_colors[3]) # initiate functionality of "4th-yellow-button"
                arr_colors[3] = colored_button_4_4.button_functional(arr_colors[3]) # initiate functionality of "4th-red-button"
                arr_colors[3] = colored_button_4_5.button_functional(arr_colors[3]) # initiate functionality of "4th-orange-button"
                arr_colors[3] = colored_button_4_6.button_functional(arr_colors[3]) # initiate functionality of "4th-purple-button"
            if (player_select[2] >= int(5)): # if we have 5 or more players, make additional 6 color buttons functional.
                name_text_box_5.on_hover_text_box() # check button-hover over text-box of 5th-player.
                arr_names[4] = name_text_box_5.strr # assign value of class-string to 5th cell of array-of-names.
                #print("arr_names[1] is: " + str(arr_names[1]))
                arr_colors[4] = colored_button_5_1.button_functional(arr_colors[4]) # initiate functionality of "5th-green-button"
                arr_colors[4] = colored_button_5_2.button_functional(arr_colors[4]) # initiate functionality of "5th-blue-button"
                arr_colors[4] = colored_button_5_3.button_functional(arr_colors[4]) # initiate functionality of "5th-yellow-button"
                arr_colors[4] = colored_button_5_4.button_functional(arr_colors[4]) # initiate functionality of "5th-red-button"
                arr_colors[4] = colored_button_5_5.button_functional(arr_colors[4]) # initiate functionality of "5th-orange-button"
                arr_colors[4] = colored_button_5_6.button_functional(arr_colors[4]) # initiate functionality of "5th-purple-button"
            if (player_select[2] >= int(6)): # if we have 6 or more players, make additional 6 color buttons functional.
                name_text_box_6.on_hover_text_box() # check button-hover over text-box of 6nd-player.
                arr_names[5] = name_text_box_6.strr # assign value of class-string to 6th cell of array-of-names.
                #print("arr_names[1] is: " + str(arr_names[1]))
                arr_colors[5] = colored_button_6_1.button_functional(arr_colors[5]) # initiate functionality of "6th-green-button"
                arr_colors[5] = colored_button_6_2.button_functional(arr_colors[5]) # initiate functionality of "6th-blue-button"
                arr_colors[5] = colored_button_6_3.button_functional(arr_colors[5]) # initiate functionality of "6th-yellow-button"
                arr_colors[5] = colored_button_6_4.button_functional(arr_colors[5]) # initiate functionality of "6th-red-button"
                arr_colors[5] = colored_button_6_5.button_functional(arr_colors[5]) # initiate functionality of "6th-orange-button"
                arr_colors[5] = colored_button_6_6.button_functional(arr_colors[5]) # initiate functionality of "6th-purple-button"
            if (check_player_color(arr_colors) == int(1)): # if each player has their own distinct color, then...
                menu = proceed_button.button_functional(menu) # menu receives new value (of new menu) from the 'proceed' button.
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()
                exit(0)
    for cnt in range(0, len(arr_names), 1): # loop over the list of names of all players
        if (len(arr_names[cnt]) == int(0)): # if the length of the name-string is 0 (if there's no string at all), then...
            arr_names[cnt] = "player" + str(cnt+1) # assign auto-name ('Player#') if there wasn't a previous string.
    #print("The arr_names is: " + str(arr_names))
    return menu, arr_colors # return value of menu, and array of colors.

def check_player_color (arr): # this function checks of the color-selection is distinct for each player.
    for cnt in range(0, len(arr), 1): # scan through the entire 'color-list'.
        if ((arr[cnt] == int(-1)) or arr.count(arr[cnt]) != int(1)): # if the color is NOT distinct, then...
            return 0 # return 0, because the colors are NOT distinct, therefore - need to reselect.
    return 1 # finally - we've scanned through the whole list - and colors are distinct - so now we can move on.

def load_menu_5 (back_mode, menu, player_select, allies, assignType, neutrals, arr_names, arr_colors, selected_map): # selection of allies / assign-type / neutral-zones.
    screen.blit(menu5, (0,0)) # apply the menu-screen of the 5th menu.
    pygame.display.update() # update the pygame window.
    temp1 = int(-1) # 'allies-group' variable
    temp2 = int(-1) # 'selected-player' variable
    reset = int(0) # '0' means that the 'reset' button is not yet selected
    if (back_mode == int(0)): # if background is dark, then...
        color = (0,0,0) # BLACK
    else: # otherwise, assign the opposite number
        color = (255,255,255) # WHITE
    #print("The arr_colors is: " + str(arr_colors)) # debug print
    allies1 = Button(1, "ALLIES-1", back_mode, (280,95,140,50), 5, 1, 0, screen) # initiate the "allies-1-group" button.
    allies2 = Button(1, "ALLIES-2", back_mode, (475,95,140,50), 5, 2, 0, screen) # initiate the "allies-2-group" button.
    allies3 = Button(1, "ALLIES-3", back_mode, (670,95,140,50), 5, 3, 0, screen) # initiate the "allies-3-group" button.
    reset_button = Button(1, "RESET", back_mode, (50,95,140,50), 5, 1, 0, screen) # initiate the "reset" button.
    lv7_gt = gui_text("", 100, 0, (800, 100, 1, 20), screen) # text of "left-click to release".
    lv0_gt = gui_text("", 100, 0, (520, 160, 1, 20), screen) # this is the text of the selected allies-group-number
    lv0_gt.init_gui_text(back_mode) # initializing the text-of-selected-allies text-object (gui_text) of player no 1, with specified color
    if (player_select[2] == int(2)): # if there are a total of 2 players, then...
        player1_button = Button(1, arr_names[0], back_mode, (375,265,140,50), 5, 0, 0, screen) # initiate the 1st-player button
        player2_button = Button(1, arr_names[1], back_mode, (575,265,140,50), 5, 1, 0, screen) # initiate the 2nd-player button
        lv1_gt = gui_text("", 45, 0, (435, 320, 1, 20), screen) # this is the 1st triangle for the 1st player
        lv2_gt = gui_text("", 45, 0, (635, 320, 1, 20), screen) # this is the 2nd triangle for the 2nd player
        lv1_gt.init_gui_text(back_mode) # initializing the 1st text-object (gui_text) of player no 1, with specified color
        lv2_gt.init_gui_text(back_mode) # initializing the 2nd text-object (gui_text) of player no 2, with specified color
        arr_allies_players = [426,626] # the button-positions, if there are 2 buttons.
    elif (player_select[2] == int(3)): # if the number-of-players are 3, then...
        player1_button = Button(1, arr_names[0], back_mode, (280,265,140,50), 5, 0, 0, screen) # initiate the 1st-player button
        player2_button = Button(1, arr_names[1], back_mode, (475,265,140,50), 5, 1, 0, screen) # initiate the 2nd-player button
        player3_button = Button(1, arr_names[2], back_mode, (670,265,140,50), 5, 2, 0, screen) # initiate the 3rd-player button
        lv1_gt = gui_text("", 45, 0, (340, 320, 1, 20), screen) # this is the 1st triangle for the 1st player
        lv2_gt = gui_text("", 45, 0, (535, 320, 1, 20), screen) # this is the 2nd triangle for the 2nd player
        lv3_gt = gui_text("", 45, 0, (730, 320, 1, 20), screen) # this is the 3rd triangle for the 3rd player
        lv1_gt.init_gui_text(back_mode) # initializing the 1st text-object (gui_text) of player no 1, with specified color
        lv2_gt.init_gui_text(back_mode) # initializing the 2nd text-object (gui_text) of player no 2, with specified color
        lv3_gt.init_gui_text(back_mode) # initializing the 3rd text-object (gui_text) of player no 3, with specified color
        arr_allies_players = [331,526,721] # the button-positions, if there are 3 buttons.
    elif (player_select[2] == int(4)): # if the number-of-players are 4, then...
        player1_button = Button(1, arr_names[0], back_mode, (175,265,140,50), 5, 0, 0, screen) # initiate the 1st-player button
        player2_button = Button(1, arr_names[1], back_mode, (375,265,140,50), 5, 1, 0, screen) # initiate the 2nd-player button
        player3_button = Button(1, arr_names[2], back_mode, (575,265,140,50), 5, 2, 0, screen) # initiate the 3rd-player button
        player4_button = Button(1, arr_names[3], back_mode, (775,265,140,50), 5, 3, 0, screen) # initiate the 4th-player button
        lv1_gt = gui_text("", 45, 0, (235, 320, 1, 20), screen) # this is the 1st triangle for the 1st player
        lv2_gt = gui_text("", 45, 0, (435, 320, 1, 20), screen) # this is the 2nd triangle for the 2nd player
        lv3_gt = gui_text("", 45, 0, (635, 320, 1, 20), screen) # this is the 3rd triangle for the 3rd player
        lv4_gt = gui_text("", 45, 0, (835, 320, 1, 20), screen) # this is the 4th triangle for the 4th player
        lv1_gt.init_gui_text(back_mode) # initializing the 1st text-object (gui_text) of player no 1, with specified color
        lv2_gt.init_gui_text(back_mode) # initializing the 2nd text-object (gui_text) of player no 2, with specified color
        lv3_gt.init_gui_text(back_mode) # initializing the 3rd text-object (gui_text) of player no 3, with specified color
        lv4_gt.init_gui_text(back_mode) # initializing the 4th text-object (gui_text) of player no 4, with specified color
        arr_allies_players = [226,426,626,826] # the button-positions, if there are 4 buttons.
    elif (player_select[2] == int(5)): # if the number-of-players are 5, then...
        player1_button = Button(1, arr_names[0], back_mode, (85,265,140,50), 5, 0, 0, screen) # initiate the 1st-player button
        player2_button = Button(1, arr_names[1], back_mode, (280,265,140,50), 5, 1, 0, screen) # initiate the 2nd-player button
        player3_button = Button(1, arr_names[2], back_mode, (475,265,140,50), 5, 2, 0, screen) # initiate the 3rd-player button
        player4_button = Button(1, arr_names[3], back_mode, (670,265,140,50), 5, 3, 0, screen) # initiate the 4th-player button
        player5_button = Button(1, arr_names[4], back_mode, (865,265,140,50), 5, 4, 0, screen) # initiate the 5th-player button
        lv1_gt = gui_text("", 45, 0, (145, 320, 1, 20), screen) # this is the 1st triangle for the 1st player
        lv2_gt = gui_text("", 45, 0, (340, 320, 1, 20), screen) # this is the 2nd triangle for the 2nd player
        lv3_gt = gui_text("", 45, 0, (535, 320, 1, 20), screen) # this is the 3rd triangle for the 3rd player
        lv4_gt = gui_text("", 45, 0, (730, 320, 1, 20), screen) # this is the 4th triangle for the 4th player
        lv5_gt = gui_text("", 45, 0, (925, 320, 1, 20), screen) # this is the 5th triangle for the 5th player
        lv1_gt.init_gui_text(back_mode) # initializing the 1st text-object (gui_text) of player no 1, with specified color
        lv2_gt.init_gui_text(back_mode) # initializing the 2nd text-object (gui_text) of player no 2, with specified color
        lv3_gt.init_gui_text(back_mode) # initializing the 3rd text-object (gui_text) of player no 3, with specified color
        lv4_gt.init_gui_text(back_mode) # initializing the 4th text-object (gui_text) of player no 4, with specified color
        lv5_gt.init_gui_text(back_mode) # initializing the 5th text-object (gui_text) of player no 5, with specified color
        arr_allies_players = [136,331,526,721,916] # the button-positions, if there are 5 buttons.
    elif (player_select[2] == int(6)): # if the number-of-players are 6, then...
        player1_button = Button(1, arr_names[0], back_mode, (75,265,140,50), 5, 0, 0, screen) # initiate the 1st-player button
        player2_button = Button(1, arr_names[1], back_mode, (237,265,140,50), 5, 1, 0, screen) # initiate the 2nd-player button
        player3_button = Button(1, arr_names[2], back_mode, (399,265,140,50), 5, 2, 0, screen) # initiate the 3rd-player button
        player4_button = Button(1, arr_names[3], back_mode, (561,265,140,50), 5, 3, 0, screen) # initiate the 4th-player button
        player5_button = Button(1, arr_names[4], back_mode, (723,265,140,50), 5, 4, 0, screen) # initiate the 5th-player button
        player6_button = Button(1, arr_names[5], back_mode, (885,265,140,50), 5, 5, 0, screen) # initiate the 6th-player button
        lv1_gt = gui_text("", 45, 0, (135, 320, 1, 20), screen) # this is the 1st triangle for the 1st player
        lv2_gt = gui_text("", 45, 0, (297, 320, 1, 20), screen) # this is the 2nd triangle for the 2nd player
        lv3_gt = gui_text("", 45, 0, (459, 320, 1, 20), screen) # this is the 3rd triangle for the 3rd player
        lv4_gt = gui_text("", 45, 0, (621, 320, 1, 20), screen) # this is the 4th triangle for the 4th player
        lv5_gt = gui_text("", 45, 0, (783, 320, 1, 20), screen) # this is the 5th triangle for the 5th player
        lv6_gt = gui_text("", 45, 0, (945, 320, 1, 20), screen) # this is the 6th triangle for the 6th player
        lv1_gt.init_gui_text(back_mode) # initializing the 1st text-object (gui_text) of player no 1, with specified color
        lv2_gt.init_gui_text(back_mode) # initializing the 2nd text-object (gui_text) of player no 2, with specified color
        lv3_gt.init_gui_text(back_mode) # initializing the 3rd text-object (gui_text) of player no 3, with specified color
        lv4_gt.init_gui_text(back_mode) # initializing the 4th text-object (gui_text) of player no 4, with specified color
        lv5_gt.init_gui_text(back_mode) # initializing the 5th text-object (gui_text) of player no 5, with specified color
        lv6_gt.init_gui_text(back_mode) # initializing the 6th text-object (gui_text) of player no 6, with specified color
        arr_allies_players = [126,288,450,612,774,936] # the button-positions, if there are 6 buttons.
    play_button = Button(3, "PLAY", back_mode, (350,570,400,100), 5, 6, 0, screen) # initiate the "play" button.
    back_button = Button(3, "BACK", back_mode, (50,570,200,100), 5, 4, 0, screen) # initiate the "back" button.
    auto_button = Button(2, "AUTO", back_mode, (20,410,200,100), 5, 1, 0, screen) # initiate "AUTO" button (assignment type).
    manual_button = Button(2, "MANUAL", back_mode, (250,410,200,100), 5, 0, 0, screen) # initiate "MANUAL" button (assignment type).
    yes_neutral = Button(3, "YES", back_mode, (640,410,200,100), 5, 1, 0, screen) # initiate "YES" button (neutral zones).
    no_neutral = Button(3, "NO", back_mode, (870,410,200,100), 5, 0, 0, screen) # initiate "NO" button (neutral zones).
    if (player_select[2] == int(2)): # if the number-of-players is 2, then...
        allies3.draw_button_cross() # draw a cross - 'X' over the button (to visually display that this button is deactivated).
    if ((selected_map == 4) and (player_select[2] == 3)): # if both number-of-players is 4, and selected map is 'quick-triangles' (only 4 territories), then...
        no_neutral.draw_button_cross() # draw a cross - 'X' over the button (to visually display that this button is deactivated).
    elif ((selected_map == 4) and (player_select[2] == 4)): # if both number-of-players is 4, and selected map is 'quick-triangles' (only 4 territories), then...
        yes_neutral.draw_button_cross() # draw a cross - 'X' over the button (to visually display that this button is deactivated).
    while (menu == int(5)): # while we're in the 5th menu (allies / assignment-type / neutral-zones)
        for event in pygame.event.get(): # get the pygame event.
            mouse = pygame.mouse.get_pos() # get the position of the mouse.
            click = pygame.mouse.get_pressed() # get the boolean value for mouse-click.
            menu = back_button.button_functional(menu) # initiate functionality of "back" button.
            assignType = auto_button.button_functional(assignType) # initiate functionality of "AUTO" button. (for assign-type).
            assignType = manual_button.button_functional(assignType) # initiate functionality of "MANUAL" button (for assign-type).
            if (not ((selected_map == 4) and (player_select[2] == 3))): # if NOT (number-of-players is 3 AND the selected map is 'quick-triangles' (only 4 territories)) then...
                neutrals = no_neutral.button_functional(neutrals) # initiate functionality of "NO" button (for neutral zones).
            if (not ((selected_map == 4) and (player_select[2] == 4))): # if NOT (number-of-players is 4 AND the selected map is 'quick-triangles' (only 4 territories)) then...
                neutrals = yes_neutral.button_functional(neutrals) # initiate functionality of "YES" button (for neutral zones).
            reset = reset_button.button_functional(reset) # initiate functionality of the 'reset' button
            temp1 = allies1.button_functional(temp1) # initiate functionality of the 'allies-group-3' button
            temp1 = allies2.button_functional(temp1) # initiate functionality of the 'allies-group-2' button
            #print("temp1 is: " + str(temp1)) # debug print
            #print("temp2 is: " + str(temp2)) # debug print
            if (reset == int(1)): # if the reset button has been activated, then...
                pygame.draw.rect(screen, color, (495,155,100,100), 0) # draw a wide rectangle to conceal all numbers that have been applied in the 'allies-group'.
                pygame.draw.rect(screen, color, (10,320,1080,40), 0) # draw a wide rectangle to conceal all numbers that have been applied in the 'player-rectangles'.
                reset_allies(allies, back_mode) # function to reset all the allies-group AND clear the selection (like right-click with the mouse)
                reset = int(0) # return the 'reset' button to be 0 (which means: diactivated)
                temp1 = int(-1) # the 'allies-group' has not been selected yet
                temp2 = int(-1) # the 'player-rectangle' has not been selected yet
            temp2 = player1_button.button_functional(temp2)
            temp2 = player2_button.button_functional(temp2)
            if (player_select[2] != int(2)):
                temp1 = allies3.button_functional(temp1)
            if (player_select[2] >= int(3)):
                temp2 = player3_button.button_functional(temp2)
            if (player_select[2] >= int(4)):
                temp2 = player4_button.button_functional(temp2)
            if (player_select[2] >= int(5)):
                temp2 = player5_button.button_functional(temp2)
            if (player_select[2] == int(6)):
                temp2 = player6_button.button_functional(temp2)
            if (temp1 >= 1): # 
                pygame.draw.rect(screen, color, (495,155,100,100), 0) # draw a rectangle - in order to conceal the previous number
                lv0_gt.change_text(str(temp1)) # change the text-value of the text-object (gui_text)
                lv0_gt.insert_gui_text(back_mode) # apply the text-object (gui_text) onto the PyGame window with the specified color.
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()
                exit(0)
            #if ((temp1 >= 1) or (temp2 >= 0)):
                #lv7_gt.change_text(str("left-click to release"))
                #lv7_gt.insert_gui_text(back_mode)
                #print("left-click to release")
                #lv7_gt.insert_gui_text(back_mode)
            if ((temp1 >= 1) and (temp2 >= 0)): # if BOTH allies-group AND player are selected (which means that NONE OF THEM are neutral), then...
                #print("temp1 is: " + str(temp1)) # debug print
                #print("temp2 is: " + str(temp2)) # debug print
                add_to_allies(allies, temp2, temp1) # function to add a player to the currently-selected allies-group
                #print(allies) # debug print
                ######
                if (temp2 == int(0)): # if the 1st player-rectangle has been selected, then...
                    pygame.draw.rect(screen, color, (arr_allies_players[0],320,40,40), 0) # draw a rectangle - in order to conceal the previous number
                    lv1_gt.change_text(str(temp1)) # change the text-value of the text-object (gui_text)
                    lv1_gt.insert_gui_text(back_mode) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                elif (temp2 == int(1)): # if the 2nd player-rectangle has been selected, then...
                    pygame.draw.rect(screen, color, (arr_allies_players[1],320,40,40), 0) # draw a rectangle - in order to conceal the previous number
                    lv2_gt.change_text(str(temp1)) # change the text-value of the text-object (gui_text)
                    lv2_gt.insert_gui_text(back_mode) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                elif (temp2 == int(2)): # if the 3rd player-rectangle has been selected, then...
                    pygame.draw.rect(screen, color, (arr_allies_players[2],320,40,40), 0) # draw a rectangle - in order to conceal the previous number
                    lv3_gt.change_text(str(temp1)) # change the text-value of the text-object (gui_text)
                    lv3_gt.insert_gui_text(back_mode) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                elif (temp2 == int(3)): # if the 4th player-rectangle has been selected, then...
                    pygame.draw.rect(screen, color, (arr_allies_players[3],320,40,40), 0) # draw a rectangle - in order to conceal the previous number
                    lv4_gt.change_text(str(temp1)) # change the text-value of the text-object (gui_text)
                    lv4_gt.insert_gui_text(back_mode) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                elif (temp2 == int(4)): # if the 5th player-rectangle has been selected, then...
                    pygame.draw.rect(screen, color, (arr_allies_players[4],320,40,40), 0) # draw a rectangle - in order to conceal the previous number
                    lv5_gt.change_text(str(temp1)) # change the text-value of the text-object (gui_text)
                    lv5_gt.insert_gui_text(back_mode) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                elif (temp2 == int(5)): # if the 6th player-rectangle has been selected, then...
                    pygame.draw.rect(screen, color, (arr_allies_players[5],320,40,40), 0) # draw a rectangle - in order to conceal the previous number
                    lv6_gt.change_text(str(temp1)) # change the text-value of the text-object (gui_text)
                    lv6_gt.insert_gui_text(back_mode) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                temp2 = int(-1) # neutralize the 'temp2' (selected player)
            if (click[2] == int(1)): # if right-button (mouse) had been clicked (which means: disabling current selection)
                pygame.draw.rect(screen, color, (495,155,100,100), 0) # draw a rectangle - in order to conceal the previous number
                temp1 = int(-1) # neutralize the 'temp1' (selected allies-group)
                temp2 = int(-1) # neutralize the 'temp2' (selected player)
            #print("The 'allies' is: " + str(allies)) # debug print
            if ((neutrals != int(-1)) and (assignType != int(-1))): # if neutrals-option AND assign-type-option have been selected, then...
                menu = play_button.button_functional(menu) # initiate functionality of "play-button".
    return menu, assignType, neutrals # return value of menu, assign-type, and neutrals.

def load_menu_6 (back_mode, menu, player_select, allies, assignType, neutrals, arr_territories, arr_players, arr_names, resolutions, selected_map, arr_colors, totals, gui_text_levels): # loading screen menu.
    try: # attempt to execute this code (purposely - it may not work)
        screen.blit(menu6, (0,0)) # display the loaded PNG file of 'menu6' onto the PyGame window.
        pygame.display.update() # refresh the PyGame display - to apply the changes.
    except: # incase that the operation of applying the PNG file had failed then...
        pass # do nothing (place-bo)

    # LOAD GAME-MAP RESOLUTIONS
    #print("selected map is: " + str(selected_map))
    load_resolutions(resolutions, res_doc, selected_map) # this will load the screen resolutions of the selected game-map
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    # LOAD ALL ID-NUMBERS
    load_totals(totals, total_doc, selected_map) # this will load the ID-ranges of the territories, only the territories that are relevant in the game.
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    # INITIALIZE TERRITORIES ARRAY
    load_init_territories(arr_territories, totals, selected_map, screen) # this will load all territory attributes of the relevant territories in the game (those of the matching game-map).
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    # INITIALIZE PLAYERS ARRAY
    init_players_arr(arr_players, arr_colors, arr_names, player_select, allies) # this will load all player attributes, in accordance to the selections of the previous menus.
    #print_arr_players(arr_players)
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    # LOAD GUI-TEXT LEVELS
    load_gui_text_levels(gui_text_levels, selected_map) # load the text-objects that get displayed onto the PyGame window.
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    game_map = load_game_map(selected_map, back_mode) # this will load the game-map (the map number, and the "back-mode" of the map).
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    if (neutrals == int(1)): # 1=ENABLE NEUTRALS
        arr_players.append(Player(6, (110,110,110), "neutral", 0, {}, [], 0)) # if "neutrals" was enabled - then it will create a neutral player (always grey)
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    #print_arr_players(arr_players)
    arr_assign = [] # define the list of available (unclaimed) territories
    fill_arr_assign(arr_territories, arr_assign) # fill the 'arr_assign' list with all ID-numbers of available (unclaimed) territories
    #print_arr_assign(arr_assign) # debug print
    deter_init_cnt(arr_territories, arr_players, neutrals) # determine initial territory-count of each player
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    #print_arr_players(arr_players)
    if (assignType == int(1)): # 1=AUTO
        auto_assign_all(arr_territories, arr_players, arr_assign, totals) # auto assign territories to all players.
    #print_arr_players(arr_players) # debug print
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    #print_arr_players(arr_players)
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    menu = int(7) # moving onto the 7th menu - the game itself.
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    return menu, game_map # returns the value of the menu, and number of the game-map.


def load_menu_7 (back_mode, menu, player_select, assignType, arr_territories, arr_players, resolutions, game_map, totals, gui_text_levels, enSave, allies): # game preparation (auto / manual assign) menu
    #print("Have reached menu 7...") # debug print
    save = int(0) # define the 'save' to be 0, means that the save-function wasn't activated yet.
    pygame.display.quit() # closing the old "menu" window.
    #print("in menu-7, the resolutions are: " + str(resolutions))
    screen = pygame.display.set_mode((resolutions[0],resolutions[1])) # setting the resolutions of the new game window.
    pygame.display.set_caption('PyRisk - by Aviv Yunker') # setting the title of the new game window.
    screen.blit(game_map,(0,0)) #  apply the game-map on the pygame window.

    # THIS IS WHERE THE GUI_TEXT OBJECTS WILL RESIDE!!!
    #def __init__ (self, text_string, text_size, default_color, dimen, screen):
    lv1_gt = gui_text("", 40, 0, (gui_text_levels[0][0],gui_text_levels[0][1], 1, 40), screen) # this is the header: "FORTIFY" / "ATTACK" / "MOVE"
    lv2_gt = gui_text("", 20, 0, (gui_text_levels[1][0], gui_text_levels[1][1], 1, 20), screen) # this further details the header of the panel
    lv3_gt = gui_text("", 20, 0, (gui_text_levels[2][0], gui_text_levels[2][1], 1, 20), screen) # this requests to select attacking / source territory
    lv4_gt = gui_text("", 20, 0, (gui_text_levels[3][0], gui_text_levels[3][1], 1, 20), screen) # this details about the remaining number of the current phase
    lv5_gt = gui_text("", 20, 0, (gui_text_levels[4][0], gui_text_levels[4][1], 1, 20), screen) # this requests to select attacked / destination territory
    lv6_gt = gui_text("", 20, 0, (gui_text_levels[5][0], gui_text_levels[5][1], 1, 20), screen) # this details the name of attacking territory
    lv7_gt = gui_text("", 20, 0, (gui_text_levels[6][0], gui_text_levels[6][1], 1, 20), screen) # this is the position of the first dice (attacking dice)
    lv8_gt = gui_text("", 20, 0, (gui_text_levels[7][0], gui_text_levels[7][1], 1, 20), screen) # this is the position of the second dice (defending dice)
    lv9_gt = gui_text("", 20, 0, (gui_text_levels[8][0], gui_text_levels[8][1], 1, 20), screen) # this details the name of defending territory

    lv1_gt.init_gui_text(back_mode) # initializing the 1st text-object (gui_text)
    lv2_gt.init_gui_text(back_mode) # initializing the 2nd text-object (gui_text)
    lv3_gt.init_gui_text(back_mode) # initializing the 3rd text-object (gui_text)
    lv4_gt.init_gui_text(back_mode) # initializing the 4th text-object (gui_text)
    lv5_gt.init_gui_text(back_mode) # initializing the 5th text-object (gui_text)
    lv6_gt.init_gui_text(back_mode) # initializing the 6th text-object (gui_text)
    lv7_gt.init_gui_text(back_mode) # initializing the 7th text-object (gui_text)
    lv8_gt.init_gui_text(back_mode) # initializing the 8th text-object (gui_text)
    lv9_gt.init_gui_text(back_mode) # initializing the 9th text-object (gui_text)

    for cnt in range(0, len(arr_territories), 1): # go over all the territory-object of the territory-list
        arr_territories[cnt].give_screen(screen) # give the 'screen' attributes to all the territories in the game.
    if (assignType == int(1)): # 1=AUTO
        for cnt in range(0, len(arr_territories), 1): # go over all the territory-object of the territory-list
            arr_territories[cnt].stick_blob() # apply the blob (colored PNG) onto the PyGame window.
            arr_territories[cnt].stick_force_no(0) # apply the territory force onto the PyGame window.
    else: #0=MANUAL
        pygame.display.update() # refresh the PyGame window.
        #print("I'm here 3/8/2020") # debug print.
        manual_assign_colors(arr_territories, arr_players, back_mode, screen, totals, gui_text_levels, lv1_gt, lv2_gt, lv4_gt, lv7_gt) # manual assign territories.
        #print("finished manual assign colors! 18/8/2020") # debug print.
        define_init_cnt(arr_players) # define the initial count of territories per player.
        manual_assign_init_forces(arr_territories, arr_players, back_mode, screen, totals, gui_text_levels, lv1_gt, lv2_gt, lv4_gt) # manual assign the initial count of territories per player.
        #print("FINISHED MANUAL ASSIGN") # debug print/
    pygame.display.update() # refresh the PyGame window.
        #print("At menu 8") # debug print.
    #print_arr_players(arr_players) # debug print
    game_over = int(0) # 0 = GAME_CONTINUES / 1 = GAME_OVER.
    while (game_over == int(0)): # while the game continues...
        for cnt in range (0, len(arr_players), 1): # go through the list of all players...
            if (arr_players[cnt].id_num == int(6) or arr_players[cnt].id_num == int(-1)): # if 'neutrals' player OR if the player is disabled, then...
                continue # skip the 'turn-iteration' - so that the player cannot fortify, attack and move forces.
            refresh_panel(resolutions, back_mode, screen) # refresh the 'communication-panel' (buttom panel)
            fortify(back_mode, cnt, arr_players, arr_territories, totals, gui_text_levels,screen, lv1_gt, lv2_gt, lv4_gt, lv7_gt) # allow to fortify.
            refresh_panel(resolutions, back_mode, screen) # refresh the 'communication-panel' (buttom panel)
            attack(cnt, back_mode, arr_players, arr_territories, totals, screen,gui_text_levels, lv1_gt,lv2_gt,lv3_gt,lv4_gt,lv5_gt,lv6_gt,lv7_gt,lv8_gt,lv9_gt) # allow to attack.
            refresh_panel(resolutions, back_mode, screen) # refresh the 'communication-panel' (buttom panel)
            move(cnt, back_mode, arr_players, arr_territories, totals, screen, gui_text_levels, lv1_gt, lv2_gt, lv3_gt, lv4_gt, lv5_gt, lv6_gt, lv7_gt, lv9_gt) # allow to move-forces.
            refresh_panel(resolutions, back_mode, screen) # refresh the 'communication-panel' (buttom panel)
            disable_players(arr_players) # determine which players will be disabled by number of owned territories.
            game_over = check_game_over(arr_players) # check if the game is over
            #print_arr_players(arr_players) # debug print.
            if (game_over == int(1)): # if the game is over / finished, then...
                menu = int(8) # set the "menu" variable to be 8 - to get transferred to the 8th menu
                return menu, back_mode # return the 'menu' and 'back_mode' variables to the calling function
            # FUNCTION THAT WILL DETERMINE IF 'GAME OVER'
            #print("fortify_complete is: " + str(fortify_complete))
            #print("attack_complete is: " + str(attack_complete))
            #print("move_complete is: " + str(move_complete))
        if (enSave == int(1)): # if save-option is enabled    
            save_button = Button(1, "SAVE", back_mode, (gui_text_levels[10][0],gui_text_levels[10][1],140,50), 5, 1, 0, screen) # create a 'save' button
            skip_button = Button(1, "SKIP", back_mode, (gui_text_levels[12][0],gui_text_levels[12][1],140,50), 5, 1, 0, screen) # create a 'skip' button
            save = int(0) # set the 'save' variable to be '0' (not pressed yet)
            skip = int(0) # set the 'skip' variable to be '0' (not pressed yet)
            lv1_gt.change_text("SAVE GAME?") # change the text-value of the text-object (gui_text)
            lv1_gt.insert_gui_text(back_mode) # apply the text-object (gui_text) onto the PyGame window with the specified color.
            while (save == int(0) and skip == int(0)): # if neither the 'save' not 'skip' buttons have been pressed yet, then...
                for event in pygame.event.get(): # get the PyGame event.
                    save = save_button.button_functional(save) # initialize functionality of the 'save' button.
                    skip = skip_button.button_functional(skip) # initialize functionality of the 'skip' button.
                    if (save == int(1)): # if the 'save' button has been pressed, then...
                        code = save_game (back_mode, arr_players, arr_territories) # save the game-progress, and produce a new code.
                        refresh_panel(resolutions, back_mode, screen) # refresh the communication panel from remaining residue.
                        lv1_gt.remove_gui_text() # remove the title gui-object text.
                        cont = int(0) # set the 'cont' variable to be '0' (not pressed yet)
                        cont_button = Button(1, "CONTINUE", back_mode, (gui_text_levels[10][0],gui_text_levels[10][1],170,50), 5, 1, 0, screen) # create a 'continue' button
                        lv1_gt.change_text("GAME SAVED!") # change the text-value of the text-object (gui_text)
                        lv1_gt.insert_gui_text(back_mode) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                        lv2_gt.change_text("code: " + str(code)) # change the text-value of the text-object (gui_text)
                        lv2_gt.insert_gui_text(back_mode) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                        while (cont == int(0)): # while the user hasn't clicked on "continue"-button yet, then...
                            for event in pygame.event.get(): # get the PyGame event
                                cont = cont_button.button_functional(cont) # initialize functionality of the "continue" button.
                    if (event.type == pygame.QUIT):
                        pygame.display.quit()
                        pygame.quit()
                        exit(0)
                    elif (skip == int(1)): # if the user had clicked on "skip", then...
                        refresh_panel(resolutions, back_mode, screen) # refresh the communication panel from remaining residue.
    return menu, back_mode # return the value of the menu


def load_menu_8(arr_players, back_mode): # load the credits-screen
    #print("Have reached menu 7...")
    ext = int(0) # the "exit" variable
    if (back_mode == int(0)): #0=DARK
        menu8 = pygame.image.load('menu8dark.png') # load the 'dark' version of the credits-screen
    else: #1=LIGHT
        menu8 = pygame.image.load('menu8light.png') # load the 'light' version of the credits-screen
    pygame.display.quit() # closing the old "menu" window.
    screen = pygame.display.set_mode((1100,700)) # setting the resolutions of the new game window.
    pygame.display.set_caption('PyRisk - by Aviv Yunker') # setting the title of the new game window.
    screen.blit(menu8,(0,0)) #  apply the game-map on the pygame window.
    position = [500,80,100,250] # the text-position of the player-names
    for cnt in range(0, len(arr_players), 1): # iterate over the list of player-objects
        if (len(arr_players[cnt].trr_and_frc) > 0): # if the player has not been deactivated, then...
            insert_credentials_text (arr_players[cnt].name, position, arr_players[cnt].color, screen) # apply the player-names onto the PyGame window
            position[1] += 70 # move the 'y' position of the text 70 pixels downwards (so that the names don't get written one on top of the other).
    exit_button = Button(3, "EXIT", back_mode, (940,630,140,50), 5, 1, 0, screen) # initiate the "skip" button.
    while (ext == int(0)): # if the exit-button has not been pressed yet, then...
        for event in pygame.event.get(): # get the PyGame event
            mouse = pygame.mouse.get_pos() # get the position of the mouse
            click = pygame.mouse.get_pressed() # get the Boolean value of the mouse-click.
            ext = exit_button.button_functional(ext) # initiate functionality of the exit-button
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()
                exit(0)
    pygame.display.quit() # close the PyGame window.
    menu = 9 # assign '9' value to the menu-variable
    return menu # return the value of the 'menu' variable

# MENUS and their numberings
# menu0 = load
# menu1 = PyRisk logo
# menu2 = select map
# menu3 = select number of players / humans / computers
# menu4 = select color for each player
# menu5 = select allies / assign-type / neutral-zones
# menu6 = loading screen.
# menu7 = actual game.


# VARIABLES
global screen
pygame.display.set_caption('PyRisk - by Aviv Yunker') # defining the title of the game-window.
#screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
screen = pygame.display.set_mode((1100,700)) # setting the resolutions of the game-window.
menu = int(1) # the menu variable - for going through all menus.
global back_mode # back-mode ==> the background (color) mode of the game (0=DARK / 1=LIGHT)
back_mode = int(1) # initiate background-mode to be "light".
selected_map = int(-1) # the selected map is currently "-1" (unselected).
enSave = int(-1) # variable of 'enable save' (0 - disable / 1 - enable)
game_map = int(0) # the game map (the map onto which the game will exist)
player_select = [-1,-1,-8] # [0]=human / [1]=computer / [2]=player
arr_colors = [] # array of colors (each player gets of color of this list - by order).
arr_names = [] # the list of names of the players
allies = [[],[],[]] # array of allies (which players cannot attack each other).
assignType = int(-1) # the type of assignment (0=MANUAL / 1=AUTO).
neutrals = int(-1) # enable or disable neutral forces (0=DISABLE / 1=ENABLE).
resolutions = [0]*2 # The coordinates of the screen (0=X / 1=Y - 2-celled list).
totals = [0]*2 # the territory ID numbers of the current game-map (0=MIN-ID / 1=MAX-ID).
arr_territories = [] # the list of territories.
arr_players = [] # list of players of the game.
arr_assign = [] # contains all id numbers (ex: countries is: 0, 1, 2 ... 41)
gui_text_levels = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]] # need to add another dimentions for "skip" button
#panel_button_levels = [[],[],[],[]]
#bonus_groups = # [{},{},{}] ...
# bonus group example: {4:(0,1,2,3,4,5,6,7,8)} - 4 points bonus for North America.
while (menu <= int(8)): # the while loop in which the next menu-to-load is determined.
    clean_screen(back_mode) # function that cleans the screen.
    #pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
    if (menu == int(0)):# if the 'menu' variable is equal to 1, load "load-game" screen
        menu, assignType, game_map, resolutions, enSave = load_menu_0(back_mode, menu, arr_players, arr_territories, resolutions, totals, gui_text_levels, assignType, game_map, enSave) # load "code-menu".
    if (menu == int(1)): # if the 'menu' variable is equal to 1, load 1st screen
        menu, back_mode = load_menu_1(back_mode, menu) # load "logo-menu".
        menu0, menu2, menu3, menu4, menu5, menu6 = load_menus(back_mode) # load the menus of the game (by background color)
    elif (menu == int(2)): # if the 'menu' variable is equal to 2, load 2nd screen
        menu, selected_map = load_menu_2(back_mode, menu, selected_map) # load the "map-selection" menu.
    elif (menu == int(3)): # if the 'menu' variable is equal to 3, load 3rd screen
        menu, player_select, enSave = load_menu_3(back_mode, menu, player_select, selected_map, enSave) # load the "player-selection" menu.
    elif (menu == int(4)): # if the 'menu' variable is equal to 4, load 4th screen
        menu, arr_colors = load_menu_4(back_mode, menu, player_select, arr_colors, arr_names) # load the "color/name-selection" menu
    elif (menu == int(5)): # if the 'menu' variable is equal to 5, load 5th screen
        menu, assignType, neutrals = load_menu_5(back_mode, menu, player_select, allies, assignType, neutrals, arr_names, arr_colors, selected_map) # load the  "allies / assign-type / neutrals" menu
    elif (menu == int(6)): # if the 'menu' variable is equal to 6, load 6th screen
        menu, game_map = load_menu_6(back_mode, menu, player_select, allies, assignType, neutrals, arr_territories, arr_players, arr_names, resolutions, selected_map, arr_colors, totals, gui_text_levels) # load the "load-screen" menu
    elif (menu == int(7)): # if the 'menu' variable is equal to 7, load 7th screen
        menu, back_mode = load_menu_7(back_mode, menu, player_select, assignType, arr_territories, arr_players, resolutions, game_map, totals, gui_text_levels, enSave, allies) # load the "game-preparation" menu
    elif (menu == int(8)): # if the 'menu' variable is equal to 8, load 8th screen
        menu = load_menu_8(arr_players, back_mode)