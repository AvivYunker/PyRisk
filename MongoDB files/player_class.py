import pygame
#import pymongo
#from pymongo import MongoClient

#cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0-udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
#db = cluster["pyrisk_db"]
#color_doc = db["pyrisk_player_colors"]


# Player1
# name: Aviv Yunker
# color: Green
# id: 0 (0=green)
# type
# trr_own: [0, 41] Alaska and East-Australia
# allies: [0,2,5] (including me - 0).

# GENERAL
# name: ABCDEFG
# color: green / blue / yellow / red / orange / purple
# type
# trr_own: [0,1,2]
# allies: [0,1,2,3,4,5]

# type 0=comp / 1=human
class Player:
    def __init__(self, id_num, color, name, typed, cnt_init, trr_and_frc, allies):
        self.id_num = id_num
        self.color = color
        self.name = name
        self.typed = typed # 0=COMP / 1=HUMAN
        self.cnt_init = 0
        self.trr_and_frc = {} # territories and force
        self.allies = []
    # get_color
    def assign_rgb (self):
        if (self.id_num == 0):
            self.color = (34,139,34)
        elif (self.id_num == 1):
            self.color = (0,95,190)
        elif (self.id_num == 2):
            self.color = (251,219,3)
        elif (self.id_num == 3):
            self.color = (251,28,46)
        elif (self.id_num == 4):
            self.color = (255,102,0)
        elif (self.id_num == 5):
            self.color = (66,12,76)
        elif (self.id_num == 6):
            self.color = (110,110,110)

    def give_name (self, name):
        self.name = name

    def init_cnt_own (self, edges, player_cnt):
        length = len(edges)
        cnt_own = int(length / player_cnt)
        self.cnt_own = cnt_own

    def reinforce (self, cnt_frc, arr_territories):
        cnt_frc = int(cnt_frc)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        while (cnt_frc > 0):
            if (click[0] == int(1)):
                id_selected = shortest_distance((mouse[0], mouse[1]), arr_centers)
                print(id_selected)

    def attack (self, arr_territories):
        pass

    def defend (self, arr_territories):
        pass

    def move (self, arr_territories):
        pass

    def get_cnt_init (self):
        self.cnt_init = len(self.trr_and_frc)*2 # each territory with an average of 3 forces.
        #print("self.cnt_init IS: " + str(self.cnt_init))



# CHECK THIS OUT (7/7/2020)
# if eastern-australia + western-australia owned,
# if eastern-australia has 15 forces
# if western-australia has 20 forces
# trr_and_frc = {"40":15, "41":20}

    #def reinforce (self):
    #def attack (self):
    #def move (self):


#number_of_players = 3
#arr_players = []
#for cnt in range(0, number_of_players, 1):
#    arr_players.append(Player(cnt,0,0,0,0,0,0))
#    arr_players[cnt].assign_rgb()

#def print_arr_players (arr_players): # DEBUG FUNCITON
#    print("BELOW IS ARR_PLAYERS:") # signify what we'll be looking at below...
#    for cnt in range(0, len(arr_players), 1): # loop over the list of players.
#        print("(", end="") # print a single round-bracket, DO NOT move to the next line.
#        print(str(arr_players[cnt].id_num), end=",") # print the 'ID-number' attribute of the player-object.
#        print(str(arr_players[cnt].color), end=",") # print the 'color' attribute of the player-object.
#        print(str(arr_players[cnt].name), end=",") # print the 'name' attribute of the player-object.
#        print(str(arr_players[cnt].typed), end=",") # print the 'typed' attribute of the player-object (whether computer-0 / human-1).
#        print(str(arr_players[cnt].cnt_init), end=",") # print the 'cnt_init' attribute of the player-object ()
#        print(str(arr_players[cnt].trr_and_frc), end=",") # print the 'territory and force' attribute of the player object ("territory_ID":"no_forces").
#        print(str(arr_players[cnt].allies) + ")") # print the 'allies' attribute of the player-object (the ID-numbers of the allied-players).
#    print("----") # separate from the next thing to be printed.

#print_arr_players(arr_players)

#for cnt in range(0, len(arr_players), 1):
#    if (arr_players[cnt].id_num == 1):
#        arr_players[cnt].trr_and_frc.update({255:5})

#print_arr_players(arr_players)

#for cnt in range(0, len(arr_players), 1):
#    if (arr_players[cnt].id_num == 1):
#        arr_players[cnt].trr_and_frc[255] -= 1

#print_arr_players(arr_players)
