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

X = int(1227)
Y = int(628)
screen = pygame.display.set_mode((X,Y))

dict_0 = {"id":0,"dots":[(110, 112),(108, 102),(95, 91),(135, 59),(107, 56),(64, 64),(46, 73),(32, 87),(30, 103),(62, 92)]}
dict_1 = {"id":1,"dots":[(105, 91),(142, 62),(183, 59),(224, 68),(275, 67),(288, 55),(308, 63),(268, 81),(246, 92),(224, 91),(215, 91)]}
dict_2 = {"id":2,"dots":[(116, 140),(108, 122),(113, 98),(214, 97),(189, 139),(115, 102),(113, 114)]}
dict_3 = {"id":3,"dots":[(196, 139),(222, 98),(242, 98),(256, 113),(268, 118),(270, 133),(264, 152),(273, 159),(251, 152),(225, 144),(218, 140),(225, 142)]}
dict_4 = {"id":4,"dots":[(278, 135),(287, 121),(304, 103),(318, 89),(327, 97),(345, 102),(359, 124),(337, 133),(309, 137),(301, 149),(285, 156),(269, 149)]}
dict_5 = {"id":5,"dots":[(143, 216),(96, 213),(84, 188),(115, 146),(194, 145),(185, 194),(151, 195),(132, 217)]}
dict_6 = {"id":6,"dots":[(159, 241),(149, 226),(141, 228),(139, 221),(148, 221),(155, 200),(192, 199),(200, 145),(219, 148),(222, 157),(232, 154),(225, 179),(243, 160),(244, 169),(244, 179),(261, 171),(276, 164),(290, 162),(305, 154),(283, 171),(256, 198),(228, 240),(196, 226)]}
dict_7 = {"id":7,"dots":[(414, 90),(384, 29),(454, 20),(516, 18),(495, 54),(472, 57),(442, 67)]}
dict_8 = {"id":8,"dots":[(104, 250),(96, 218),(114, 224),(125, 224),(131, 221),(142, 234),(148, 231),(158, 247),(232, 326),(196, 270),(127, 272),(183, 299)]}
dict_9 = {"id":9,"dots":[(228, 356),(236, 329),(248, 316),(260, 310),(292, 321),(316, 337),(337, 344),(333, 352),(308, 354),(305, 340),(294, 343),(286, 343),(286, 352),(281, 357),(271, 353),(264, 360),(263, 378),(252, 371),(242, 362),(229, 356)]}
dict_10 = {"id":10,"dots":[(226, 361),(241, 367),(256, 376),(248, 390),(248, 402),(261, 411),(280, 411),(301, 427),(315, 443),(317, 459),(333, 477),(323, 481),(311, 469),(297, 460),(280, 461),(268, 442),(246, 429)]}
dict_11 = {"id":11,"dots":[(269, 447),(282, 469),(299, 465),(308, 476),(318, 480),(320, 490),(335, 484),(333, 504),(343, 515),(330, 531),(274, 484),(326, 498),(329, 491)]}
dict_12 = {"id":12,"dots":[(347, 510),(331, 496),(341, 480),(339, 473),(329, 465),(324, 459),(322, 446),(310, 433),(304, 423),(289, 417),(282, 404),(268, 410),(262, 405),(252, 397),(266, 382),(267, 364),(268, 356),(285, 361),(288, 347),(302, 344),(306, 360),(333, 357),(340, 351),(295, 349),(291, 355),(274, 357),(259, 386),(340, 504),(337, 491)]}
dict_13 = {"id":13,"dots":[(508, 77)]}
dict_14 = {"id":14,"dots":[(609, 110),(598, 95),(587, 99),(617, 66),(659, 84),(651, 57),(640, 90)]}
dict_15 = {"id":15,"dots":[(534, 123),(558, 130)]}
dict_16 = {"id":16,"dots":[(535, 196),(526, 192),(530, 169),(554, 170),(550, 146),(564, 143),(569, 137),(578, 143),(584, 145),(579, 153),(583, 159),(583, 164)]}
dict_17 = {"id":17,"dots":[(575, 135),(591, 126),(593, 110),(607, 123),(622, 120),(636, 119),(639, 146),(624, 151),(619, 140),(599, 146),(592, 148),(588, 139)]}
dict_18 = {"id":18,"dots":[(620, 180),(589, 161),(587, 151),(600, 152),(614, 145),(613, 145),(618, 154),(630, 159),(643, 151),(658, 149),(664, 161),(661, 170),(655, 175),(645, 194),(636, 181),(593, 153),(630, 152)]}
dict_19 = {"id":19,"dots":[(687, 158),(677, 149),(667, 157),(660, 144),(645, 144),(651, 134),(639, 109),(645, 101),(661, 92),(667, 86),(657, 59),(760, 68),(747, 80),(756, 103),(766, 122),(773, 131),(743, 127),(736, 152),(727, 141),(742, 180),(719, 170),(703, 160),(705, 146)]}
dict_20 = {"id":20,"dots":[(599, 350),(617, 351),(613, 331),(645, 312),(650, 289),(650, 276),(621, 262),(594, 251),(592, 228),(599, 214),(537, 205),(595, 197),(571, 202),(490, 305),(636, 269)]}
dict_21 = {"id":21,"dots":[(603, 218),(598, 227),(599, 249),(616, 255),(651, 270),(656, 260),(694, 260),(697, 258),(691, 229),(669, 226),(643, 219),(637, 262)]}
dict_22 = {"id":22,"dots":[(700, 263),(660, 266),(657, 275),(652, 296),(653, 308),(663, 326),(672, 340),(702, 349),(687, 372),(689, 400),(697, 410),(694, 427),(700, 434),(716, 411),(713, 388),(732, 360),(762, 315),(736, 318),(713, 292)]}
dict_23 = {"id":23,"dots":[(601, 357),(623, 354),(618, 334),(649, 318),(671, 347),(694, 349),(685, 364),(677, 378),(677, 397),(670, 406),(670, 412),(675, 420),(664, 414),(650, 410),(641, 393),(631, 398),(624, 389),(608, 387),(623, 343),(612, 358)]}
dict_24 = {"id":24,"dots":[(611, 394),(622, 393),(631, 405),(640, 398),(647, 416),(666, 420),(681, 423),(679, 403),(689, 421),(696, 439),(689, 432),(701, 421),(719, 416),(652, 467),(659, 419),(671, 424),(676, 411),(689, 413)]}
dict_25 = {"id":25,"dots":[(742, 448)]}
dict_26 = {"id":26,"dots":[(697, 227),(672, 182),(719, 180),(741, 189),(772, 196),(794, 203),(802, 246),(720, 266),(738, 300),(728, 278),(768, 288),(795, 216)]}
dict_27 = {"id":27,"dots":[(810, 245),(800, 206),(814, 197),(832, 193),(845, 197),(868, 208),(867, 223),(888, 231),(903, 236),(919, 239),(937, 235),(943, 237),(933, 262),(869, 273),(806, 224)]}
dict_28 = {"id":28,"dots":[(950, 241),(948, 243),(936, 268),(966, 324),(980, 347),(983, 352),(977, 341),(950, 254),(956, 260),(967, 269),(976, 265),(976, 266),(986, 262),(990, 266),(985, 278),(1002, 310)]}
dict_29 = {"id":29,"dots":[(846, 186),(860, 181),(864, 163),(869, 154),(877, 146),(888, 151),(900, 165),(909, 165),(960, 197),(959, 197),(967, 194),(974, 196),(1003, 176),(1012, 183),(1008, 191),(1027, 196),(1035, 223),(995, 262),(986, 255),(985, 255),(967, 262),(956, 251),(953, 235),(937, 229),(926, 235),(915, 234),(910, 234),(896, 230),(888, 223),(876, 221),(873, 211),(870, 202),(861, 200)]}
dict_30 = {"id":30,"dots":[(757, 167),(770, 187),(800, 197),(811, 189),(823, 192),(840, 191),(843, 179),(860, 169),(855, 161),(861, 156),(827, 123),(805, 119),(782, 124),(779, 129),(780, 137),(765, 136),(746, 135),(734, 141),(741, 148)]}
dict_31 = {"id":31,"dots":[(775, 123),(766, 116),(760, 107),(758, 96),(753, 83),(764, 62),(780, 60),(773, 52),(797, 54),(803, 61),(812, 63),(822, 73),(835, 81),(842, 94),(860, 104),(864, 125),(867, 146),(854, 138),(834, 120),(821, 119),(807, 112),(788, 115)]}
dict_32 = {"id":32,"dots":[(803, 48),(819, 40),(849, 33),(876, 36),(872, 46),(883, 46),(890, 50),(886, 61),(898, 73),(904, 79),(909, 89),(913, 98),(906, 100),(896, 103),(897, 119),(888, 126),(879, 128),(876, 140),(865, 134),(873, 127),(860, 112),(870, 109),(859, 94),(849, 92),(842, 85),(839, 77),(827, 71),(816, 59),(808, 57)]}
dict_33 = {"id":33,"dots":[(912, 76),(904, 72),(892, 58),(898, 51),(891, 45),(890, 45),(904, 47),(916, 49),(1049, 60),(1051, 65),(1046, 67),(1044, 71),(1036, 74),(1030, 77),(1030, 81),(1020, 84),(1019, 94),(1006, 100),(1009, 108),(973, 106),(955, 94),(939, 95),(933, 95),(947, 90),(924, 84)]}
dict_34 = {"id":34,"dots":[(884, 131),(895, 126),(903, 118),(902, 106),(912, 102),(914, 92),(910, 82),(926, 93),(936, 101),(949, 97),(958, 100),(968, 109),(981, 111),(1009, 117),(1018, 117),(1018, 124),(1030, 126),(1026, 135),(1030, 139),(1015, 130),(994, 120),(983, 127),(985, 136),(974, 137),(963, 138),(951, 136),(937, 134),(917, 127),(911, 130),(911, 136),(895, 131)]}
dict_35 = {"id":35,"dots":[(1053, 164),(1059, 158),(1058, 151),(1054, 144),(1043, 146),(1040, 141),(1040, 142),(1032, 134),(1036, 122),(1022, 120),(1023, 113),(1017, 112),(1012, 103),(1025, 97),(1025, 88),(1038, 87),(1035, 79),(1051, 70),(1061, 70),(1056, 62)]}
dict_36 = {"id":36,"dots":[(884, 143),(894, 137),(911, 141),(917, 133),(933, 140),(943, 139),(960, 145),(974, 142),(988, 143),(992, 133),(991, 127),(1001, 126),(1016, 139),(1032, 148),(1035, 149),(1051, 149),(1045, 153),(1052, 155),(1047, 162),(1050, 170),(1050, 179),(1046, 186),(1058, 201),(1052, 193),(1030, 182),(1024, 176),(1017, 178),(1005, 168),(991, 177),(974, 189),(959, 190),(944, 182),(932, 175),(909, 158),(901, 159)]}
dict_37 = {"id":37,"dots":[(1075, 215),(1101, 197),(1095, 167)]}
dict_38 = {"id":38,"dots":[(956, 343),(971, 358),(990, 380),(1002, 394),(1019, 398),(1059, 407),(1073, 404),(1060, 370),(1016, 373),(1012, 362),(1042, 339),(1044, 356)]}
dict_39 = {"id":39,"dots":[(1087, 361),(1108, 370),(1111, 377),(1121, 380),(1134, 397),(1142, 402),(1174, 411)]}
dict_40 = {"id":40,"dots":[(1084, 434),(1071, 478),(1119, 486),(1104, 528),(1048, 486)]}
dict_41 = {"id":41,"dots":[(1089, 435),(1095, 425),(1114, 423),(1131, 448),(1145, 421),(1154, 436),(1140, 483),(1115, 556),(1109, 533),(1126, 483),(1076, 477)]}
game_map = pygame.image.load('countries (dark).png')
screen.blit(game_map,(0,0))

arr_centers = [dict_0,dict_1,dict_2,dict_3,dict_4,dict_5,dict_6,dict_7,dict_8,dict_9,dict_10,dict_11,dict_12,dict_13,dict_14,dict_15,dict_16,dict_17,dict_18,dict_19,dict_20,dict_21,dict_22,dict_23,dict_24,dict_25,dict_26,dict_27,dict_28,dict_29,dict_30,dict_31,dict_32,dict_33,dict_34,dict_35,dict_36,dict_37,dict_38,dict_39,dict_40,dict_41]

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