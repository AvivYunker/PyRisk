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

X = int(1200)
Y = int(600)
screen = pygame.display.set_mode((X,Y))
dict_234 = {"id":234,"dots":[(356, 192),(299, 133),(417, 85),(416, 166)]}
dict_235 = {"id":235,"dots":[(426, 85),(508, 84),(507, 167),(425, 166)]}
dict_236 = {"id":236,"dots":[(516, 84),(597, 85),(596, 167),(515, 168)]}
dict_237 = {"id":237,"dots":[(605, 84),(687, 84),(687, 167),(605, 167)]}
dict_238 = {"id":238,"dots":[(695, 84),(778, 84),(777, 167),(695, 167)]}
dict_239 = {"id":239,"dots":[(785, 84),(786, 167),(843, 192),(902, 135)]}
dict_240 = {"id":240,"dots":[(246, 255),(294, 142),(351, 197),(325, 256)]}
dict_241 = {"id":241,"dots":[(335, 256),(357, 203),(412, 257)]}
dict_242 = {"id":242,"dots":[(362, 197),(418, 176),(417, 251)]}
dict_243 = {"id":243,"dots":[(425, 257),(425, 174),(507, 174),(507, 257)]}
dict_244 = {"id":244,"dots":[(515, 174),(515, 257),(597, 258),(597, 175)]}
dict_245 = {"id":245,"dots":[(606, 175),(686, 175),(686, 256),(605, 257)]}
dict_246 = {"id":246,"dots":[(695, 257),(695, 175),(777, 174),(777, 257)]}
dict_247 = {"id":247,"dots":[(785, 252),(786, 174),(839, 198)]}
dict_248 = {"id":248,"dots":[(790, 257),(844, 203),(865, 257)]}
dict_249 = {"id":249,"dots":[(872, 257),(848, 197),(907, 139),(955, 257)]}
dict_250 = {"id":250,"dots":[(292, 384),(244, 264),(326, 266),(352, 324)]}
dict_251 = {"id":251,"dots":[(357, 319),(335, 265),(413, 264)]}
dict_252 = {"id":252,"dots":[(361, 325),(417, 267),(417, 347)]}
dict_253 = {"id":253,"dots":[(425, 347),(425, 264),(506, 263),(507, 348)]}
dict_254 = {"id":254,"dots":[(515, 347),(515, 264),(597, 264),(597, 347)]}
dict_255 = {"id":255,"dots":[(606, 346),(606, 265),(687, 264),(687, 348)]}
dict_256 = {"id":256,"dots":[(696, 347),(695, 264),(777, 264),(777, 347)]}
dict_257 = {"id":257,"dots":[(785, 347),(784, 268),(839, 323)]}
dict_258 = {"id":258,"dots":[(788, 264),(865, 265),(843, 318)]}
dict_259 = {"id":259,"dots":[(848, 324),(873, 265),(956, 265),(907, 383)]}
dict_260 = {"id":260,"dots":[(298, 389),(356, 329),(417, 353),(416, 439)]}
dict_261 = {"id":261,"dots":[(426, 438),(425, 355),(507, 355),(507, 437)]}
dict_262 = {"id":262,"dots":[(516, 355),(596, 355),(596, 438),(515, 437)]}
dict_263 = {"id":263,"dots":[(606, 355),(687, 354),(687, 438),(605, 438)]}
dict_264 = {"id":264,"dots":[(695, 354),(777, 354),(777, 438),(695, 438)]}
dict_265 = {"id":265,"dots":[(785, 354),(844, 328),(903, 387),(785, 437)]}

arr_centers = [dict_234,dict_235,dict_236,dict_237,dict_238,dict_239,dict_240,dict_241,dict_242,dict_243,dict_244,dict_245,dict_246,dict_247,dict_248,dict_249,dict_250,dict_251,dict_252,dict_253,dict_254,dict_255,dict_256,dict_257,dict_258,dict_259,dict_260,dict_261,dict_262,dict_263,dict_264,dict_265]

game_map = pygame.image.load('stadium (dark).png')
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
