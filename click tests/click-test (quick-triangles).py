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

X = int(1000)
Y = int(700)
screen = pygame.display.set_mode((X,Y))
# DOTS ARE CONFIRMED TO BE OKAY
dict_162 = {"id":162,"dots":[(495,175)]}
dict_163 = {"id":163,"dots":[(420,250)]}
dict_164 = {"id":164,"dots":[(570,250)]}
dict_165 = {"id":165,"dots":[(495,325)]}
arr_centers = [dict_162,dict_163,dict_164,dict_165]
game_map = pygame.image.load('quick-triangles (dark).png')
screen.blit(game_map,(0,0))

for cnt1 in range(0, len(arr_centers), 1):
    for cnt2 in range(0, len(arr_centers[cnt1]["dots"]), 1):
        gfxdraw.pixel(screen, arr_centers[cnt1]["dots"][cnt2][0],arr_centers[cnt1]["dots"][cnt2][1], (255,0,0))

#mouse = pygame.mouse.get_pos()
#for x in range(0, 500, 1):
    #for y in range(0, 500, 1):
        #id_selected = shortest_distance((x, y), arr_centers)
        #id_selected = int(id_selected + 162)
        #if (id_selected == int(162)):
            #color = (0,255,0)
            #gfxdraw.pixel(screen,x,y, color)
        #elif (id_selected == int(163)):
            #color = (0,0,255)
            #gfxdraw.pixel(screen,x,y, color)
        #elif (id_selected == int(164)):
            #color = (255,255,0)
            #gfxdraw.pixel(screen,x,y, color)
        #elif (id_selected == int(165)):
            #color = (255,0,0)
            #gfxdraw.pixel(screen,x,y, color)
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