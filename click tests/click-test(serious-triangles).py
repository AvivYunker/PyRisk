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

X = int(650)
Y = int(650)
screen = pygame.display.set_mode((X,Y))
# DOTS ARE CONFIRMED TO BE OKAY
dict_166 = {"id":166,"dots":[(133,123)]}
dict_167 = {"id":167,"dots":[(188,68)]}
dict_168 = {"id":168,"dots":[(243,68)]}
dict_169 = {"id":169,"dots":[(298,123)]}
dict_170 = {"id":170,"dots":[(353,123)]}
dict_171 = {"id":171,"dots":[(408,68)]}
dict_172 = {"id":172,"dots":[(463,68)]}
dict_173 = {"id":173,"dots":[(518,123)]}
dict_174 = {"id":174,"dots":[(133,178)]}
dict_175 = {"id":175,"dots":[(188,233)]}
dict_176 = {"id":176,"dots":[(243,233)]}
dict_177 = {"id":177,"dots":[(298,178)]}
dict_178 = {"id":178,"dots":[(353,178)]}
dict_179 = {"id":179,"dots":[(408,233)]}
dict_180 = {"id":180,"dots":[(463,233)]}
dict_181 = {"id":181,"dots":[(518,178)]}
dict_182 = {"id":182,"dots":[(133,343)]}
dict_183 = {"id":183,"dots":[(188,288)]}
dict_184 = {"id":184,"dots":[(243,288)]}
dict_185 = {"id":185,"dots":[(298,343)]}
dict_186 = {"id":186,"dots":[(353,343)]}
dict_187 = {"id":187,"dots":[(408,288)]}
dict_188 = {"id":188,"dots":[(463,288)]}
dict_189 = {"id":189,"dots":[(518,343)]}
dict_190 = {"id":190,"dots":[(133,398)]}
dict_191 = {"id":191,"dots":[(188,453)]}
dict_192 = {"id":192,"dots":[(243,453)]}
dict_193 = {"id":193,"dots":[(298,398)]}
dict_194 = {"id":194,"dots":[(353,398)]}
dict_195 = {"id":195,"dots":[(408,453)]}
dict_196 = {"id":196,"dots":[(463,453)]}
dict_197 = {"id":197,"dots":[(518,398)]}

arr_centers = [dict_166,dict_167,dict_168,dict_169,dict_170,dict_171,dict_172,dict_173,dict_174,dict_175,dict_176,dict_177,dict_178,dict_179,dict_180,dict_181,dict_182,dict_183,dict_184,dict_185,dict_186,dict_187,dict_188,dict_189,dict_190,dict_191,dict_192,dict_193,dict_194,dict_195,dict_196,dict_197]

game_map = pygame.image.load('serious-triangles (dark).png')
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
           print(mouse)
           gfxdraw.pixel(screen, mouse[0], mouse[1], (0,255,0))
           id_selected = shortest_distance((mouse[0], mouse[1]), arr_centers)
           print("id: " + str(id_selected))
           pygame.display.update()