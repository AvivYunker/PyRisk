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
# DOTS ARE CONFIRMED TO BE OKAY
dict_42 = {"id":42,"dots":[(72,98)]}
dict_43 = {"id":43,"dots":[(151,145)]}
dict_44 = {"id":44,"dots":[(231,98)]}
dict_45 = {"id":45,"dots":[(310,145)]}
dict_46 = {"id":46,"dots":[(390,98)]}
dict_47 = {"id":47,"dots":[(469,145)]}
dict_48 = {"id":48,"dots":[(549,98)]}
dict_49 = {"id":49,"dots":[(628,145)]}
dict_50 = {"id":50,"dots":[(708,98)]}
dict_51 = {"id":51,"dots":[(787,145)]}
dict_52 = {"id":52,"dots":[(867,98)]}
dict_53 = {"id":53,"dots":[(946,145)]}
dict_54 = {"id":54,"dots":[(1026,98)]}
dict_55 = {"id":55,"dots":[(1105,145)]}
dict_56 = {"id":56,"dots":[(72,193)]}
dict_57 = {"id":57,"dots":[(151,240)]}
dict_58 = {"id":58,"dots":[(231,193)]}
dict_59 = {"id":59,"dots":[(310,240)]}
dict_60 = {"id":60,"dots":[(390,193)]}
dict_61 = {"id":61,"dots":[(469,240)]}
dict_62 = {"id":62,"dots":[(549,193)]}
dict_63 = {"id":63,"dots":[(628,240)]}
dict_64 = {"id":64,"dots":[(708,193)]}
dict_65 = {"id":65,"dots":[(787,240)]}
dict_66 = {"id":66,"dots":[(867,193)]}
dict_67 = {"id":67,"dots":[(946,240)]}
dict_68 = {"id":68,"dots":[(1026,193)]}
dict_69 = {"id":69,"dots":[(1105,240)]}
dict_70 = {"id":70,"dots":[(72,288)]}
dict_71 = {"id":71,"dots":[(151,336)]}
dict_72 = {"id":72,"dots":[(231,288)]}
dict_73 = {"id":73,"dots":[(310,336)]}
dict_74 = {"id":74,"dots":[(390,288)]}
dict_75 = {"id":75,"dots":[(469,336)]}
dict_76 = {"id":76,"dots":[(549,288)]}
dict_77 = {"id":77,"dots":[(628,336)]}
dict_78 = {"id":78,"dots":[(708,288)]}
dict_79 = {"id":79,"dots":[(787,336)]}
dict_80 = {"id":80,"dots":[(867,288)]}
dict_81 = {"id":81,"dots":[(946,336)]}
dict_82 = {"id":82,"dots":[(1026,288)]}
dict_83 = {"id":83,"dots":[(1105,336)]}
dict_84 = {"id":84,"dots":[(72,383)]}
dict_85 = {"id":85,"dots":[(151,431)]}
dict_86 = {"id":86,"dots":[(231,383)]}
dict_87 = {"id":87,"dots":[(310,431)]}
dict_88 = {"id":88,"dots":[(390,383)]}
dict_89 = {"id":89,"dots":[(469,431)]}
dict_90 = {"id":90,"dots":[(549,383)]}
dict_91 = {"id":91,"dots":[(628,431)]}
dict_92 = {"id":92,"dots":[(708,383)]}
dict_93 = {"id":93,"dots":[(787,431)]}
dict_94 = {"id":94,"dots":[(867,383)]}
dict_95 = {"id":95,"dots":[(946,431)]}
dict_96 = {"id":96,"dots":[(1026,383)]}
dict_97 = {"id":97,"dots":[(1105,431)]}

arr_centers = [dict_42,dict_43,dict_44,dict_45,dict_46,dict_47,dict_48,dict_49,dict_50,dict_51,dict_52,dict_53,dict_54,dict_55,dict_56,dict_57,dict_58,dict_59,dict_60,dict_61,dict_62,dict_63,dict_64,dict_65,dict_66,dict_67,dict_68,dict_69,dict_70,dict_71,dict_72,dict_73,dict_74,dict_75,dict_76,dict_77,dict_78,dict_79,dict_80,dict_81,dict_82,dict_83,dict_84,dict_85,dict_86,dict_87,dict_88,dict_89,dict_90,dict_91,dict_92,dict_93,dict_94,dict_95,dict_96,dict_97]

game_map = pygame.image.load('hexagons (dark).png')
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