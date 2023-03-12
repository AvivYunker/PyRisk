import pygame
pygame.init()
from pygame import gfxdraw

def distance_two_dots(dot1, dot2):
    part1 = pow(dot2[1]-dot1[1], 2) # y2 - y1
    part2 = pow(dot2[0]-dot1[0], 2) # x2 - x1
    res = pow(part1 + part2, 0.5)
    return res

def shortest_distance(my_dot, arr_dot):
    selected = int(0)
    dist = 10000
    for cnt1 in range(0, len(arr_dot), 1):
        for cnt2 in range(0, len(arr_dot[cnt1]["dots"]), 1):
            #print(arr_dot[cnt1]["dots"][cnt2][0])
            #print(arr_dot[cnt1]["dots"][cnt2][1])
            #print(my_dot[0])
            #print(my_dot[1])
            temp = distance_two_dots((my_dot[0],my_dot[1]),(arr_dot[cnt1]["dots"][cnt2][0],arr_dot[cnt1]["dots"][cnt2][1]))
        if (temp < dist):
            dist = int(temp)
            selected = (arr_dot[cnt1]["id"])
            #print("ID IS: " + str(selected))
    return selected

X = int(800)
Y = int(800)
screen = pygame.display.set_mode((X,Y))
# DOTS ARE CONFIRMED TO BE OKAY
dict_198 = {"id":198,"dots":[(150,150)]}
dict_199 = {"id":199,"dots":[(250,150)]}
dict_200 = {"id":200,"dots":[(350,150)]}
dict_201 = {"id":201,"dots":[(450,150)]}
dict_202 = {"id":202,"dots":[(550,150)]}
dict_203 = {"id":203,"dots":[(650,150)]}
dict_204 = {"id":204,"dots":[(150,250)]}
dict_205 = {"id":205,"dots":[(250,250)]}
dict_206 = {"id":206,"dots":[(350,250)]}
dict_207 = {"id":207,"dots":[(450,250)]}
dict_208 = {"id":208,"dots":[(550,250)]}
dict_209 = {"id":209,"dots":[(650,250)]}
dict_210 = {"id":210,"dots":[(150,350)]}
dict_211 = {"id":211,"dots":[(250,350)]}
dict_212 = {"id":212,"dots":[(350,350)]}
dict_213 = {"id":213,"dots":[(450,350)]}
dict_214 = {"id":214,"dots":[(550,350)]}
dict_215 = {"id":215,"dots":[(650,350)]}
dict_216 = {"id":216,"dots":[(150,450)]}
dict_217 = {"id":217,"dots":[(250,450)]}
dict_218 = {"id":218,"dots":[(350,450)]}
dict_219 = {"id":219,"dots":[(450,450)]}
dict_220 = {"id":220,"dots":[(550,450)]}
dict_221 = {"id":221,"dots":[(650,450)]}
dict_222 = {"id":222,"dots":[(150,550)]}
dict_223 = {"id":223,"dots":[(250,550)]}
dict_224 = {"id":224,"dots":[(350,550)]}
dict_225 = {"id":225,"dots":[(450,550)]}
dict_226 = {"id":226,"dots":[(550,550)]}
dict_227 = {"id":227,"dots":[(650,550)]}
dict_228 = {"id":228,"dots":[(150,650)]}
dict_229 = {"id":229,"dots":[(250,650)]}
dict_230 = {"id":230,"dots":[(350,650)]}
dict_231 = {"id":231,"dots":[(450,650)]}
dict_232 = {"id":232,"dots":[(550,650)]}
dict_233 = {"id":233,"dots":[(650,650)]}

arr_centers = [dict_198,dict_199,dict_200,dict_201,dict_202,dict_203,dict_204,dict_205,dict_206,dict_207,dict_208,dict_209,dict_210,dict_211,dict_212,dict_213,dict_214,dict_215,dict_216,dict_217,dict_218,dict_219,dict_220,dict_221,dict_222,dict_223,dict_224,dict_225,dict_226,dict_227,dict_228,dict_229,dict_230,dict_231,dict_232,dict_233]

game_map = pygame.image.load('squares (dark).png')
screen.blit(game_map,(0,0))

for cnt1 in range(0, len(arr_centers), 1):
    for cnt2 in range(0, len(arr_centers[cnt1]["dots"]), 1):
        gfxdraw.pixel(screen, arr_centers[cnt1]["dots"][cnt2][0],arr_centers[cnt1]["dots"][cnt2][1], (255,0,0))

pygame.display.update()
print(len(arr_centers))
while (True):
   for event in pygame.event.get():
       mouse = pygame.mouse.get_pos()
       click = pygame.mouse.get_pressed()
       if (click[0] == int(1)):
           #print(mouse)
           gfxdraw.pixel(screen, mouse[0], mouse[1], (0,255,0))
           id_selected = shortest_distance((mouse[0], mouse[1]), arr_centers)
           print("id: " + str(id_selected))
           pygame.display.update()