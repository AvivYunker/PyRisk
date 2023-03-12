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
dict_98 = {"id":98,"dots":[(470,100)]}
dict_99 = {"id":99,"dots":[(440,160)]}
dict_100 = {"id":100,"dots":[(470,142)]}
dict_101 = {"id":101,"dots":[(500,160)]}
dict_102 = {"id":102,"dots":[(410,220)]}
dict_103 = {"id":103,"dots":[(440,200)]}
dict_104 = {"id":104,"dots":[(470,220)]}
dict_105 = {"id":105,"dots":[(500,200)]}
dict_106 = {"id":106,"dots":[(530,220)]}
dict_107 = {"id":107,"dots":[(380,280)]}
dict_108 = {"id":108,"dots":[(410,260)]}
dict_109 = {"id":109,"dots":[(440,280)]}
dict_110 = {"id":110,"dots":[(470,260)]}
dict_111 = {"id":111,"dots":[(500,280)]}
dict_112 = {"id":112,"dots":[(530,260)]}
dict_113 = {"id":113,"dots":[(560,280)]}
dict_114 = {"id":114,"dots":[(350,340)]}
dict_115 = {"id":115,"dots":[(380,320)]}
dict_116 = {"id":116,"dots":[(410,340)]}
dict_117 = {"id":117,"dots":[(440,320)]}
dict_118 = {"id":118,"dots":[(470,340)]}
dict_119 = {"id":119,"dots":[(500,320)]}
dict_120 = {"id":120,"dots":[(530,340)]}
dict_121 = {"id":121,"dots":[(560,320)]}
dict_122 = {"id":122,"dots":[(590,340)]}
dict_123 = {"id":123,"dots":[(320,400)]}
dict_124 = {"id":124,"dots":[(350,380)]}
dict_125 = {"id":125,"dots":[(380,400)]}
dict_126 = {"id":126,"dots":[(410,380)]}
dict_127 = {"id":127,"dots":[(440,400)]}
dict_128 = {"id":128,"dots":[(470,380)]}
dict_129 = {"id":129,"dots":[(500,400)]}
dict_130 = {"id":130,"dots":[(530,380)]}
dict_131 = {"id":131,"dots":[(560,400)]}
dict_132 = {"id":132,"dots":[(590,380)]}
dict_133 = {"id":133,"dots":[(620,400)]}
dict_134 = {"id":134,"dots":[(290,460)]}
dict_135 = {"id":135,"dots":[(320,440)]}
dict_136 = {"id":136,"dots":[(350,460)]}
dict_137 = {"id":137,"dots":[(380,440)]}
dict_138 = {"id":138,"dots":[(410,460)]}
dict_139 = {"id":139,"dots":[(440,440)]}
dict_140 = {"id":140,"dots":[(470,460)]}
dict_141 = {"id":141,"dots":[(500,440)]}
dict_142 = {"id":142,"dots":[(530,460)]}
dict_143 = {"id":143,"dots":[(560,440)]}
dict_144 = {"id":144,"dots":[(590,460)]}
dict_145 = {"id":145,"dots":[(620,440)]}
dict_146 = {"id":146,"dots":[(650,460)]}
dict_147 = {"id":147,"dots":[(260,520)]}
dict_148 = {"id":148,"dots":[(290,500)]}
dict_149 = {"id":149,"dots":[(320,520)]}
dict_150 = {"id":150,"dots":[(350,500)]}
dict_151 = {"id":151,"dots":[(380,520)]}
dict_152 = {"id":152,"dots":[(410,500)]}
dict_153 = {"id":153,"dots":[(440,520)]}
dict_154 = {"id":154,"dots":[(470,500)]}
dict_155 = {"id":155,"dots":[(500,520)]}
dict_156 = {"id":156,"dots":[(530,500)]}
dict_157 = {"id":157,"dots":[(560,520)]}
dict_158 = {"id":158,"dots":[(590,500)]}
dict_159 = {"id":159,"dots":[(620,520)]}
dict_160 = {"id":160,"dots":[(650,500)]}
dict_161 = {"id":161,"dots":[(680,520)]}

arr_centers = [dict_98,dict_99,dict_100,dict_101,dict_102,dict_103,dict_104,dict_105,dict_106,dict_107,dict_108,dict_109,dict_110,dict_111,dict_112,dict_113,dict_114,dict_115,dict_116,dict_117,dict_118,dict_119,dict_120,dict_121,dict_122,dict_123,dict_124,dict_125,dict_126,dict_127,dict_128,dict_129,dict_130,dict_131,dict_132,dict_133,dict_134,dict_135,dict_136,dict_137,dict_138,dict_139,dict_140,dict_141,dict_142,dict_143,dict_144,dict_145,dict_146,dict_147,dict_148,dict_149,dict_150,dict_151,dict_152,dict_153,dict_154,dict_155,dict_156,dict_157,dict_158,dict_159,dict_160,dict_161]

game_map = pygame.image.load('pyramid (dark).png')
screen.blit(game_map,(0,0))

for cnt1 in range(0, len(arr_centers), 1):
    for cnt2 in range(0, len(arr_centers[cnt1]["dots"]), 1):
        gfxdraw.pixel(screen, arr_centers[cnt1]["dots"][cnt2][0],arr_centers[cnt1]["dots"][cnt2][1], (255,0,0))


pygame.display.update()
print(str(len(arr_centers)) + "//")
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