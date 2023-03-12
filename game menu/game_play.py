import pygame
#pygame.init()
import pymongo
import random
from territory_class import Territory
from player_class import Player
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:631029@cluster0-udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
pos_doc = db["pyrisk_positions"]
border_doc = db["pyrisk_borders"]
png_name_doc = db["pyrisk_blob_links"]
bonus_doc = db["pyrisk_bonus"]
dots_doc = db["pyrisk_dots"]
totals_doc = db["pyrisk_total_territories"]

def create_territories (arr_territories, edges):
    for cnt in range(0, len(edges), 1):
        arr_territories.append(Territory(edges[cnt],0,0,0,0,0,0,0,0,0))
        arr_territories[cnt].get_position()
        arr_territories[cnt].get_name()
        arr_territories[cnt].get_borders()
        arr_territories[cnt].get_png_names()
        arr_territories[cnt].get_bonus_group()
        arr_territories[cnt].get_dots()
        arr_territories[cnt].zero_forces()
        arr_territories[cnt].load_blobs()


def create_players (arr_players, player_cnt, edges):
    #Aviv = Player(0,0,0,0,0,0)
    print("asdoa")
    #print(len(player_cnt)) # 0 --> NOT GOOD
    for cnt in range(0, player_cnt, 1):
        arr_players.append(Player(cnt, 0,0,0,0,0,0))
        arr_players[cnt].get_color()
        arr_players[cnt].init_cnt_own(edges, player_cnt)
        #print(str(arr_players[cnt].cnt_own))



def auto_assign_territories (arr_territories, edges, player_cnt):
    arr_temp = []
    for cnt in range(0, len(edges), 1):
        arr_temp.append(edges[cnt])
    for cnt in range(0, len(arr_temp), 1):
        print(str(arr_temp[cnt]), end=",")
    amnt = int(len(arr_territories) / player_cnt) # amout
    #print("The amount is: " + str(amnt))
    for cnt1 in range(0, len(arr_territories), 1):
        for cnt2 in range(0, amnt, 1):
            rndm = random.randrange(0, len(arr_temp))
            while (arr_temp[rndm] == int(-1)):
                rndm = random.randrange(0, len(arr_temp))
            #arr_territories[cnt].controller.append(arr_temp[rndm])
            arr_temp[rndm] = int(-1)
    for cnt in range(0, len(arr_territories), 1):
        print(arr_territories[cnt].controller)
            # 7/2/2020 - I AM HERE



player_cnt = 2 # player count --> there will be 2 players
map_select = 4 # map selection --> quick-triangles.

#res_tup = resolutions.find_one({"_id":(map_select-1)})
X = int(500)
Y = int(500)
screen = pygame.display.set_mode((X,Y))
screen.fill((255,0,0))

game_map = pygame.image.load('quick-triangles (dark).png')
screen.blit(game_map,(0,0))
pygame.display.update()

edges = [] # 162,163,164,165

total_edges = totals_doc.find_one({"_id":(map_select-1)})
total_edges = total_edges["total"]
edges = total_edges

arr_territories = []
arr_players = []

create_territories(arr_territories, edges)
create_players(arr_players, player_cnt, edges)

#auto_assign_territories (arr_territories, edges, player_cnt)
print("ALIVE")


#for cnt in range(0, len(arr_territories), 1):
    #print(arr_territories[cnt)


#for cnt in range(0, len(edges), 1):
    #name = borders_doc.find_one({"_id":(edges[cnt])})
    #name = name["name"]
    #name = Territory(cnt,0,0,0,0,0,0,0,0,0)







# initial screen
# menu1 = pygame.image.load('menu1.png')

