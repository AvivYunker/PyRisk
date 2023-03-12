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

cluster = MongoClient("mongodb+srv://PyRiskUser:6310294455@cluster0-udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

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

def distance_two_dots(dot1, dot2):
    part1 = pow(dot2[1]-dot1[1], 2) # y2 - y1
    part2 = pow(dot2[0]-dot1[0], 2) # x2 - x1
    res = pow(part1 + part2, 0.5)
    return res


                #print(arr_territories[0].dots)
                #print(arr_territories[0].dots[0])
                #print(arr_territories[0].dots[0][0])
def shortest_distance(my_dot, arr_territories):
    selected = int(0)
    dist = 10000
    for cnt1 in range(0, len(arr_territories), 1):
        for cnt2 in range(0, len(arr_territories[cnt1].dots), 1):
            temp = distance_two_dots((my_dot[0],my_dot[1]),(arr_territories[cnt1].dots[cnt2][0],arr_territories[cnt1].dots[cnt2][1]))
            if (temp < dist):
                dist = int(temp)
                selected = (arr_territories[cnt1].id_num)
                #print("ID IS: " + str(selected))
    return selected

def all_taken (arr_territories):
    for cnt in range(0, len(arr_territories), 1):
        if (arr_territories[cnt].controller == int(-1)):
            return 0
    return 1

screen = pygame.display.set_mode((1227,628))
game_map = pygame.image.load("stadium (dark).png")
screen.blit(game_map,(0,0))
pygame.display.update()

lwr_id = int(234)
upr_id = int(265)
selected_map = int(1)

arr_territories = []
for cnt in range(lwr_id, upr_id+1, 1):
    arr_territories.append(Territory(cnt, 0,0,0,0,0,0,0,0,0,0,screen))
for cnt in range(0, len(arr_territories), 1):
    arr_territories[cnt].init_territory(selected_map)

print('ready')
x = all_taken(arr_territories)
z = int(0)
while (x == int(0)):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        color = screen.get_at(mouse)
        click = pygame.mouse.get_pressed()
        if (click[0] == int(1) and color[0] == int(0) and color[1] == int(0) and color[2] == int(1)):
                id_selected = shortest_distance((mouse[0],mouse[1]),arr_territories)
                color = screen.get_at(mouse)
                arr_territories[id_selected-lwr_id].controller = int(z)
                z += 1
                if (z == int(7)):
                    z = int(0)
                arr_territories[id_selected-lwr_id].stick_blob()
                x = all_taken(arr_territories)
        pygame.display.update()



