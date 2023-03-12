import pygame
pygame.init()
from button_class import Button
from territory_class import Territory
from player_class import Player
import pymongo
from pymongo import MongoClient
import time
import timeit
import random
import math

screen = pygame.display.set_mode((1227,628))
game_map = pygame.image.load("countries (dark).png")
screen.blit(game_map,(0,0))
pygame.display.update()


cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0-udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
res_doc = db["pyrisk_resolutions"]
total_doc = db["pyrisk_total_territories"]
blob_names_doc = db["pyrisk_blob_links"]
bonus_doc = db["pyrisk_bonus"]
borders_doc = db["pyrisk_borders"]
dots_doc = db["pyrisk_dots"]
colors_doc = db["pyrisk_player_colors"]
pos_doc = db["pyrisk_positions"]
general_doc = db["pyrisk_general"]

def fill_arr_assign (arr_assign, arr_territories):
    for cnt in range(0, len(arr_territories), 1):
        if (arr_territories[cnt].controller == int(-1)):
            arr_assign.append(arr_territories[cnt].id_num)
    #for cnt in range(0, len(arr_assign), 1):
        #print(str(arr_assign[cnt]), end=",")

def generate_neutral_count (arr_territories, neut_cnt):
    min_edge = int(len(arr_territories) / 5)
    max_edge = int(len(arr_territories) / 4)
    neut_cnt = random.randrange(min_edge, max_edge)
    return neut_cnt

def auto_assign_one (arr_territories, arr_assign, team_cnt, flag):
    team_cnt = int(team_cnt)
    while (team_cnt > 0):
        rndm = random.randrange(0, len(arr_assign))
        arr_territories[arr_assign[rndm]].controller = int(flag)
        arr_assign.pop(rndm)
        team_cnt = int(team_cnt - 1)

def generate_player_count(arr_territories, arr_players):
    pass

def deter_init_cnt (arr_temp, arr_players):
    temp_list = []
    ttl = len(arr_temp)
    edge_1 = math.ceil(len(arr_temp) / len(arr_players))
    edge_2 = math.floor(len(arr_temp) / len(arr_players))
    #print("ttl is: " + str(ttl))
    while (ttl > 0):
        if (ttl % edge_1 == int(0)):
            temp_list.append(edge_1)
            ttl = int(ttl - edge_1)
            #print("A", end=",")
        else:
            temp_list.append(edge_2)
            ttl = int(ttl - edge_2)
            #print("B", end=",")
    #print("\n---\n")
    #for cnt in range(0, len(arr_player_cnt), 1):
        #print(str(arr_player_cnt[cnt]), end=",")
    #print("*****")
    #print(temp_list)
    #print("ARR_PLAYERS:")
    for cnt in range(0, len(arr_players), 1):
        indx = random.randrange(0, len(temp_list))
        arr_players[cnt].cnt_own = temp_list[indx]
        temp_list.pop(indx)
    #print("RESULTS ARE::::")
    #for cnt in range(0, len(arr_players), 1):
        #print(str(arr_players[cnt].id_num) + " --> " + str(arr_players[cnt].cnt_own))



lwr_id = int(0)
upr_id = int(41)
player_cnt = int(6)

arr_territories = []
arr_players = []
arr_assign = []
neut_cnt = int(0) # number of neutral territories
selected_map = int(1)



# DEFINING THE NATIONS:
for cnt in range(lwr_id, upr_id+1, 1):
    arr_territories.append(Territory(cnt, 0,0,0,0,0,0,0,0,0,screen))
for cnt in range(0, len(arr_territories), 1):
    arr_territories[cnt].init_territory(selected_map)

# DEFINING THE PLAYERS:
for cnt in range(0, player_cnt, 1):
    arr_players.append(Player(cnt, 0,0,0,0,0,0))

fill_arr_assign(arr_assign, arr_territories)
neut_cnt = generate_neutral_count(arr_territories, neut_cnt)
generate_player_count(arr_territories, arr_players)
#print("Neutrals count is: " + str(neut_cnt))


auto_assign_one(arr_territories, arr_assign, neut_cnt, int(6))
deter_init_cnt(arr_assign, arr_players)
for cnt in range(0, len(arr_players), 1):
    auto_assign_one(arr_territories, arr_assign, arr_players[cnt].cnt_own, int(cnt))



#for cnt in range(0, len(arr_players), 1):
    #auto_assign_one(arr_territories, arr_assign)
for cnt in range(0, len(arr_territories), 1):
    print("(" + str(arr_territories[cnt].id_num), end = ",")
    print(str(arr_territories[cnt].name), end = ",")
    print(str(arr_territories[cnt].controller) + ")")

for cnt in range(0, len(arr_territories), 1):
    arr_territories[cnt].stick_blob()


input("DONE!")