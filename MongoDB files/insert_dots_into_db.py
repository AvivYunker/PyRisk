import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_dots"]


alaska_dots = {"_id":0,"name":"alaska","dots":[(110, 112), (108, 102), (95, 91), (135, 59), (107, 56), (64, 64), (46, 73), (32, 87), (30, 103), (62, 92),(116, 74)]}
north_west_territory_dots = {"_id":1,"name":"north-west-territory","dots":[(105, 91), (142, 62), (183, 59), (224, 68), (275, 67), (288, 55), (308, 63), (268, 81), (246, 92), (224, 91), (215, 91),(121, 76)]}
alberta_dots = {"_id":2,"name":"alberta","dots":[(116, 140), (108, 122), (113, 98), (214, 97), (189, 139), (115, 102), (113, 114)]}
ontario_dots = {"_id":3,"name":"ontario","dots":[(196, 139), (222, 98), (242, 98), (256, 113), (268, 118), (270, 133), (264, 152), (273, 159), (251, 152), (225, 144), (218, 140), (225, 142)]}
quebec_dots = {"_id":4,"name":"quebec","dots":[(278, 135), (287, 121), (304, 103), (318, 89), (327, 97), (345, 102), (359, 124), (337, 133), (309, 137), (301, 149), (285, 156), (269, 149)]}
western_united_states_dots = {"_id":5,"name":"western-united-states","dots":[(143, 216), (96, 213), (84, 188), (115, 146), (194, 145), (185, 194), (151, 195), (132, 217)]}
eastern_united_states_dots = {"_id":6,"name":"eastern-united-states","dots":[(159, 241), (149, 226), (141, 228), (139, 221), (148, 221), (155, 200), (192, 199), (200, 145), (219, 148), (222, 157), (232, 154), (225, 179), (243, 160), (244, 169), (244, 179), (261, 171), (276, 164), (290, 162), (305, 154), (283, 171), (256, 198), (228, 240), (196, 226)]}
greenland_dots = {"_id":7,"name":"greenland","dots":[(414, 90), (384, 29), (454, 20), (516, 18), (495, 54), (472, 57), (442, 67)]}
mexico_dots = {"_id":8,"name":"mexico","dots":[(104, 250), (96, 218), (114, 224), (125, 224), (131, 221), (142, 234), (148, 231), (158, 247), (232, 326), (196, 270), (127, 272), (183, 299)]}
venezuela_dots = {"_id":9,"name":"venezuela","dots":[(228, 356), (236, 329), (248, 316), (260, 310), (292, 321), (316, 337), (337, 344), (333, 352), (308, 354), (305, 340), (294, 343), (286, 343), (286, 352), (281, 357), (271, 353), (264, 360), (263, 378), (252, 371), (242, 362), (229, 356),(260, 371),(260, 371),(265, 352),(262, 369)]}
peru_dots = {"_id":10,"name":"peru","dots":[(226, 361), (241, 367), (256, 376), (248, 390), (248, 402), (261, 411), (280, 411), (301, 427), (315, 443), (317, 459), (333, 477), (323, 481), (311, 469), (297, 460), (280, 461), (268, 442), (246, 429),(286, 423),(287, 438),(320, 472),(280, 448),(288, 422)]}
argentina_dots = {"_id":11,"name":"argentina","dots":[(269, 447), (282, 469), (299, 465), (308, 476), (318, 480), (320, 490), (335, 484), (333, 504), (343, 515), (330, 531), (274, 484), (326, 498), (329, 491)]}
brazil_dots = {"_id":12,"name":"brazil","dots":[(347, 510), (331, 496), (341, 480), (339, 473), (329, 465), (324, 459), (322, 446), (310, 433), (304, 423), (289, 417), (282, 404), (268, 410), (262, 405), (252, 397), (266, 382), (267, 364), (268, 356), (285, 361), (288, 347), (302, 344), (306, 360), (333, 357), (340, 351), (295, 349), (291, 355), (274, 357), (259, 386), (340, 504), (337, 491)]}
iceland_dots = {"_id":13,"name":"iceland","dots":[(508, 77)]}
scandinavia_dots = {"_id":14,"name":"scandinavia","dots":[(609, 110), (598, 95), (587, 99), (617, 66), (659, 84), (651, 57), (640, 90)]}
great_britain_dots = {"_id":15,"name":"great-britain","dots":[(534, 123), (558, 130)]}
western_europe_dots = {"_id":16,"name":"western-europe","dots":[(535, 196), (526, 192), (530, 169), (554, 170), (550, 146), (564, 143), (569, 137), (578, 143), (584, 145), (579, 153), (583, 159), (583, 164)]}
northern_europe_dots = {"_id":17,"name":"northern-europe","dots":[(575, 135), (591, 126), (593, 110), (607, 123), (622, 120), (636, 119), (639, 146), (624, 151), (619, 140), (599, 146), (592, 148), (588, 139)]}
southern_europe_dots = {"_id":18,"name":"southern-europe","dots":[(620, 180), (589, 161), (587, 151), (600, 152), (614, 145), (613, 145), (618, 154), (630, 159), (643, 151), (658, 149), (664, 161), (661, 170), (655, 175), (645, 194), (636, 181), (593, 153), (630, 152)]}
ukraine_dots = {"_id":19,"name":"ukraine","dots":[(687, 158), (677, 149), (667, 157), (660, 144), (645, 144), (651, 134), (639, 109), (645, 101), (661, 92), (667, 86), (657, 59), (760, 68), (747, 80), (756, 103), (766, 122), (773, 131), (743, 127), (736, 152), (727, 141), (742, 180), (719, 170), (703, 160), (705, 146)]}
north_africa_dots = {"_id":20,"name":"north-africa","dots":[(599, 350), (617, 351), (613, 331), (645, 312), (650, 289), (650, 276), (621, 262), (594, 251), (592, 228), (599, 214), (537, 205), (595, 197), (571, 202), (490, 305), (636, 269)]}
egypt_dots = {"_id":21,"name":"egypt","dots":[(603, 218), (598, 227), (599, 249), (616, 255), (651, 270), (656, 260), (694, 260), (697, 258), (691, 229), (669, 226), (643, 219), (637, 262)]}
sudan_dots = {"_id":22,"name":"sudan","dots":[(700, 263), (660, 266), (657, 275), (652, 296), (653, 308), (663, 326), (672, 340), (702, 349), (687, 372), (689, 400), (697, 410), (694, 427), (700, 434), (716, 411), (713, 388), (732, 360), (762, 315), (736, 318), (713, 292),(707, 412)]}
congo_dots = {"_id":23,"name":"congo","dots":[(601, 357), (623, 354), (618, 334), (649, 318), (671, 347), (694, 349), (685, 364), (677, 378), (677, 397), (670, 406), (670, 412), (675, 420), (664, 414), (650, 410), (641, 393), (631, 398), (624, 389), (608, 387), (623, 343), (612, 358)]}
south_africa_dots = {"_id":24,"name":"south-africa","dots":[(611, 394), (622, 393), (631, 405), (640, 398), (647, 416), (666, 420), (681, 423), (679, 403), (689, 421), (696, 439), (689, 432), (701, 421), (719, 416), (652, 467), (659, 419), (671, 424), (676, 411), (689, 413),(718, 433),(710, 420),(696, 470)]}
madagascar_dots = {"_id":25,"name":"madagascar","dots":[(742, 448)]}
middle_east_dots = {"_id":26,"name":"middle-east","dots":[(697, 227), (672, 182), (719, 180), (741, 189), (772, 196), (794, 203), (802, 246), (720, 266), (738, 300), (728, 278), (768, 288), (795, 216)]}
india_dots = {"_id":27,"name":"india","dots":[(810, 245), (800, 206), (814, 197), (832, 193), (845, 197), (868, 208), (867, 223), (888, 231), (903, 236), (919, 239), (937, 235), (943, 237), (933, 262), (869, 273), (806, 224)]}
siam_dots = {"_id":28,"name":"siam","dots":[(950, 241), (948, 243), (936, 268), (966, 324), (980, 347), (983, 352), (977, 341), (950, 254), (956, 260), (967, 269), (976, 265), (976, 266), (986, 262), (990, 266), (985, 278), (1002, 310)]}
china_dots = {"_id":29,"name":"china","dots":[(846, 186), (860, 181), (864, 163), (869, 154), (877, 146), (888, 151), (900, 165), (909, 165), (960, 197), (959, 197), (967, 194), (974, 196), (1003, 176), (1012, 183), (1008, 191), (1027, 196), (1035, 223), (995, 262), (986, 255), (985, 255), (967, 262), (956, 251), (953, 235), (937, 229), (926, 235), (915, 234), (910, 234), (896, 230), (888, 223), (876, 221), (873, 211), (870, 202), (861, 200),(942, 189),(930, 182)]}
central_asia_dots = {"_id":30,"name":"central-asia","dots":[(757, 167), (770, 187), (800, 197), (811, 189), (823, 192), (840, 191), (843, 179), (860, 169), (855, 161), (861, 156), (827, 123), (805, 119), (782, 124), (779, 129), (780, 137), (765, 136), (746, 135), (734, 141), (741, 148)]}        
ural_dots = {"_id":31,"name":"ural","dots":[(775, 123), (766, 116), (760, 107), (758, 96), (753, 83), (764, 62), (780, 60), (773, 52), (797, 54), (803, 61), (812, 63), (822, 73), (835, 81), (842, 94), (860, 104), (864, 125), (867, 146), (854, 138), (834, 120), (821, 119), (807, 112), (788, 115)]}
siberia_dots = {"_id":32,"name":"siberia","dots":[(803, 48), (819, 40), (849, 33), (876, 36), (872, 46), (883, 46), (890, 50), (886, 61), (898, 73), (904, 79), (909, 89), (913, 98), (906, 100), (896, 103), (897, 119), (888, 126), (879, 128), (876, 140), (865, 134), (873, 127), (860, 112), (870, 109), (859, 94), (849, 92), (842, 85), (839, 77), (827, 71), (816, 59), (808, 57)]}
yakutsk_dots = {"_id":33,"name":"yakutsk","dots":[(912, 76), (904, 72), (892, 58), (898, 51), (891, 45), (890, 45), (904, 47), (916, 49), (1049, 60), (1051, 65), (1046, 67), (1044, 71), (1036, 74), (1030, 77), (1030, 81), (1020, 84), (1019, 94), (1006, 100), (1009, 108), (973, 106), (955, 94), (939, 95), (933, 95), (947, 90), (924, 84)]}
irkutsk_dots = {"_id":34,"name":"irkutsk","dots":[(884, 131), (895, 126), (903, 118), (902, 106), (912, 102), (914, 92), (910, 82), (926, 93), (936, 101), (949, 97), (958, 100), (968, 109), (981, 111), (1009, 117), (1018, 117), (1018, 124), (1030, 126), (1026, 135), (1030, 139), (1015, 130), (994, 120), (983, 127), (985, 136), (974, 137), (963, 138), (951, 136), (937, 134), (917, 127), (911, 130), (911, 136), (895, 131)]}
kamtchatka_dots = {"_id":35,"name":"kamtchatka","dots":[(1053, 164), (1059, 158), (1058, 151), (1054, 144), (1043, 146), (1040, 141), (1040, 142), (1032, 134), (1036, 122), (1022, 120), (1023, 113), (1017, 112), (1012, 103), (1025, 97), (1025, 88), (1038, 87), (1035, 79), (1051, 70), (1061, 70), (1056, 62),(1112, 115)]}
mongolia_dots = {"_id":36,"name":"mongolia","dots":[(884, 143), (894, 137), (911, 141), (917, 133), (933, 140), (943, 139), (960, 145), (974, 142), (988, 143), (992, 133), (991, 127), (1001, 126), (1016, 139), (1032, 148), (1035, 149), (1051, 149), (1045, 153), (1052, 155), (1047, 162), (1050, 170), (1050, 179), (1046, 186), (1058, 201), (1052, 193), (1030, 182), (1024, 176), (1017, 178), (1005, 168), (991, 177), (974, 189), (959, 190), (944, 182), (932, 175), (909, 158), (901, 159)]}
japan_dots = {"_id":37,"name":"japan","dots":[(1075, 215), (1101, 197), (1095, 167)]}
indonesia_dots = {"_id":38,"name":"indonesia","dots":[(956, 343), (971, 358), (990, 380), (1002, 394), (1019, 398), (1059, 407), (1073, 404), (1060, 370), (1016, 373), (1012, 362), (1042, 339), (1044, 356)]}
papau_new_guinea_dots = {"_id":39,"name":"papau-new-guinea","dots":[(1087, 361), (1108, 370), (1111, 377), (1121, 380), (1134, 397), (1142, 402), (1174, 411)]}
western_australia_dots = {"_id":40,"name":"western-australia","dots":[(1084, 434), (1071, 478), (1119, 486), (1104, 528), (1048, 486)]}
eastern_australia_dots = {"_id":41,"name":"eastern-australia","dots":[(1089, 435), (1095, 425), (1114, 423), (1131, 448), (1145, 421), (1154, 436), (1140, 483), (1115, 556), (1109, 533), (1126, 483), (1076, 477)]}
hex0_dots = {"_id":42,"name":"hex0","dots":[(72, 98)]}
hex1_dots = {"_id":43,"name":"hex1","dots":[(151, 145)]}
hex2_dots = {"_id":44,"name":"hex2","dots":[(231, 98)]}
hex3_dots = {"_id":45,"name":"hex3","dots":[(310, 145)]}
hex4_dots = {"_id":46,"name":"hex4","dots":[(390, 98)]}
hex5_dots = {"_id":47,"name":"hex5","dots":[(469, 145)]}
hex6_dots = {"_id":48,"name":"hex6","dots":[(549, 98)]}
hex7_dots = {"_id":49,"name":"hex7","dots":[(628, 145)]}
hex8_dots = {"_id":50,"name":"hex8","dots":[(708, 98)]}
hex9_dots = {"_id":51,"name":"hex9","dots":[(787, 145)]}
hex10_dots = {"_id":52,"name":"hex10","dots":[(867, 98)]}
hex11_dots = {"_id":53,"name":"hex11","dots":[(946, 145)]}
hex12_dots = {"_id":54,"name":"hex12","dots":[(1026, 98)]}
hex13_dots = {"_id":55,"name":"hex13","dots":[(1105, 145)]}
hex14_dots = {"_id":56,"name":"hex14","dots":[(72, 193)]}
hex15_dots = {"_id":57,"name":"hex15","dots":[(151, 240)]}
hex16_dots = {"_id":58,"name":"hex16","dots":[(231, 193)]}
hex17_dots = {"_id":59,"name":"hex17","dots":[(310, 240)]}
hex18_dots = {"_id":60,"name":"hex18","dots":[(390, 193)]}
hex19_dots = {"_id":61,"name":"hex19","dots":[(469, 240)]}
hex20_dots = {"_id":62,"name":"hex20","dots":[(549, 193)]}
hex21_dots = {"_id":63,"name":"hex21","dots":[(628, 240)]}
hex22_dots = {"_id":64,"name":"hex22","dots":[(708, 193)]}
hex23_dots = {"_id":65,"name":"hex23","dots":[(787, 240)]}
hex24_dots = {"_id":66,"name":"hex24","dots":[(867, 193)]}
hex25_dots = {"_id":67,"name":"hex25","dots":[(946, 240)]}
hex26_dots = {"_id":68,"name":"hex26","dots":[(1026, 193)]}
hex27_dots = {"_id":69,"name":"hex27","dots":[(1105, 240)]}
hex28_dots = {"_id":70,"name":"hex28","dots":[(72, 288)]}
hex29_dots = {"_id":71,"name":"hex29","dots":[(151, 336)]}
hex30_dots = {"_id":72,"name":"hex30","dots":[(231, 288)]}
hex31_dots = {"_id":73,"name":"hex31","dots":[(310, 336)]}
hex32_dots = {"_id":74,"name":"hex32","dots":[(390, 288)]}
hex33_dots = {"_id":75,"name":"hex33","dots":[(469, 336)]}
hex34_dots = {"_id":76,"name":"hex34","dots":[(549, 288)]}
hex35_dots = {"_id":77,"name":"hex35","dots":[(628, 336)]}
hex36_dots = {"_id":78,"name":"hex36","dots":[(708, 288)]}
hex37_dots = {"_id":79,"name":"hex37","dots":[(787, 336)]}
hex38_dots = {"_id":80,"name":"hex38","dots":[(867, 288)]}
hex39_dots = {"_id":81,"name":"hex39","dots":[(946, 336)]}
hex40_dots = {"_id":82,"name":"hex40","dots":[(1026, 288)]}
hex41_dots = {"_id":83,"name":"hex41","dots":[(1105, 336)]}
hex42_dots = {"_id":84,"name":"hex42","dots":[(72, 383)]}
hex43_dots = {"_id":85,"name":"hex43","dots":[(151, 431)]}
hex44_dots = {"_id":86,"name":"hex44","dots":[(231, 383)]}
hex45_dots = {"_id":87,"name":"hex45","dots":[(310, 431)]}
hex46_dots = {"_id":88,"name":"hex46","dots":[(390, 383)]}
hex47_dots = {"_id":89,"name":"hex47","dots":[(469, 431)]}
hex48_dots = {"_id":90,"name":"hex48","dots":[(549, 383)]}
hex49_dots = {"_id":91,"name":"hex49","dots":[(628, 431)]}
hex50_dots = {"_id":92,"name":"hex50","dots":[(708, 383)]}
hex51_dots = {"_id":93,"name":"hex51","dots":[(787, 431)]}
hex52_dots = {"_id":94,"name":"hex52","dots":[(867, 383)]}
hex53_dots = {"_id":95,"name":"hex53","dots":[(946, 431)]}
hex54_dots = {"_id":96,"name":"hex54","dots":[(1026, 383)]}
hex55_dots = {"_id":97,"name":"hex55","dots":[(1105, 431)]}
pyr0_dots = {"_id":98,"name":"pyr0","dots":[(500, 100)]}
pyr1_dots = {"_id":99,"name":"pyr1","dots":[(470, 160)]}
pyr2_dots = {"_id":100,"name":"pyr2","dots":[(500, 142)]}
pyr3_dots = {"_id":101,"name":"pyr3","dots":[(530, 160)]}
pyr4_dots = {"_id":102,"name":"pyr4","dots":[(440, 220)]}
pyr5_dots = {"_id":103,"name":"pyr5","dots":[(470, 200)]}
pyr6_dots = {"_id":104,"name":"pyr6","dots":[(500, 220)]}
pyr7_dots = {"_id":105,"name":"pyr7","dots":[(530, 200)]}
pyr8_dots = {"_id":106,"name":"pyr8","dots":[(560, 220)]}
pyr9_dots = {"_id":107,"name":"pyr9","dots":[(410, 280)]}
pyr10_dots = {"_id":108,"name":"pyr10","dots":[(440, 260)]}
pyr11_dots = {"_id":109,"name":"pyr11","dots":[(470, 280)]}
pyr12_dots = {"_id":110,"name":"pyr12","dots":[(500, 260)]}
pyr13_dots = {"_id":111,"name":"pyr13","dots":[(530, 280)]}
pyr14_dots = {"_id":112,"name":"pyr14","dots":[(560, 260)]}
pyr15_dots = {"_id":113,"name":"pyr15","dots":[(590, 280)]}
pyr16_dots = {"_id":114,"name":"pyr16","dots":[(380, 340)]}
pyr17_dots = {"_id":115,"name":"pyr17","dots":[(410, 320)]}
pyr18_dots = {"_id":116,"name":"pyr18","dots":[(440, 340)]}
pyr19_dots = {"_id":117,"name":"pyr19","dots":[(470, 320)]}
pyr20_dots = {"_id":118,"name":"pyr20","dots":[(500, 340)]}
pyr21_dots = {"_id":119,"name":"pyr21","dots":[(530, 320)]}
pyr22_dots = {"_id":120,"name":"pyr22","dots":[(560, 340)]}
pyr23_dots = {"_id":121,"name":"pyr23","dots":[(590, 320)]}
pyr24_dots = {"_id":122,"name":"pyr24","dots":[(620, 340)]}
pyr25_dots = {"_id":123,"name":"pyr25","dots":[(350, 400)]}
pyr26_dots = {"_id":124,"name":"pyr26","dots":[(380, 380)]}
pyr27_dots = {"_id":125,"name":"pyr27","dots":[(410, 400)]}
pyr28_dots = {"_id":126,"name":"pyr28","dots":[(440, 380)]}
pyr29_dots = {"_id":127,"name":"pyr29","dots":[(470, 400)]}
pyr30_dots = {"_id":128,"name":"pyr30","dots":[(500, 380)]}
pyr31_dots = {"_id":129,"name":"pyr31","dots":[(530, 400)]}
pyr32_dots = {"_id":130,"name":"pyr32","dots":[(560, 380)]}
pyr33_dots = {"_id":131,"name":"pyr33","dots":[(590, 400)]}
pyr34_dots = {"_id":132,"name":"pyr34","dots":[(620, 380)]}
pyr35_dots = {"_id":133,"name":"pyr35","dots":[(650, 400)]}
pyr36_dots = {"_id":134,"name":"pyr36","dots":[(320, 460)]}
pyr37_dots = {"_id":135,"name":"pyr37","dots":[(350, 440)]}
pyr38_dots = {"_id":136,"name":"pyr38","dots":[(380, 460)]}
pyr39_dots = {"_id":137,"name":"pyr39","dots":[(410, 440)]}
pyr40_dots = {"_id":138,"name":"pyr40","dots":[(440, 460)]}
pyr41_dots = {"_id":139,"name":"pyr41","dots":[(470, 440)]}
pyr42_dots = {"_id":140,"name":"pyr42","dots":[(500, 460)]}
pyr43_dots = {"_id":141,"name":"pyr43","dots":[(530, 440)]}
pyr44_dots = {"_id":142,"name":"pyr44","dots":[(560, 460)]}
pyr45_dots = {"_id":143,"name":"pyr45","dots":[(590, 440)]}
pyr46_dots = {"_id":144,"name":"pyr46","dots":[(620, 460)]}
pyr47_dots = {"_id":145,"name":"pyr47","dots":[(650, 440)]}
pyr48_dots = {"_id":146,"name":"pyr48","dots":[(680, 460)]}
pyr49_dots = {"_id":147,"name":"pyr49","dots":[(290, 520)]}
pyr50_dots = {"_id":148,"name":"pyr50","dots":[(320, 500)]}
pyr51_dots = {"_id":149,"name":"pyr51","dots":[(350, 520)]}
pyr52_dots = {"_id":150,"name":"pyr52","dots":[(380, 500)]}
pyr53_dots = {"_id":151,"name":"pyr53","dots":[(410, 520)]}
pyr54_dots = {"_id":152,"name":"pyr54","dots":[(440, 500)]}
pyr55_dots = {"_id":153,"name":"pyr55","dots":[(470, 520)]}
pyr56_dots = {"_id":154,"name":"pyr56","dots":[(500, 500)]}
pyr57_dots = {"_id":155,"name":"pyr57","dots":[(530, 520)]}
pyr58_dots = {"_id":156,"name":"pyr58","dots":[(560, 500)]}
pyr59_dots = {"_id":157,"name":"pyr59","dots":[(590, 520)]}
pyr60_dots = {"_id":158,"name":"pyr60","dots":[(620, 500)]}
pyr61_dots = {"_id":159,"name":"pyr61","dots":[(650, 520)]}
pyr62_dots = {"_id":160,"name":"pyr62","dots":[(680, 500)]}
pyr63_dots = {"_id":161,"name":"pyr63","dots":[(710, 520)]}
qck0_dots = {"_id":162,"name":"qck0","dots":[(495, 175)]}
qck1_dots = {"_id":163,"name":"qck1","dots":[(420, 250)]}
qck2_dots = {"_id":164,"name":"qck2","dots":[(570, 250)]}
qck3_dots = {"_id":165,"name":"qck3","dots":[(495, 325)]}
srs0_dots = {"_id":166,"name":"srs0","dots":[(308, 123)]}
srs1_dots = {"_id":167,"name":"srs1","dots":[(363, 68)]}
srs2_dots = {"_id":168,"name":"srs2","dots":[(418, 68)]}
srs3_dots = {"_id":169,"name":"srs3","dots":[(473, 123)]}
srs4_dots = {"_id":170,"name":"srs4","dots":[(528, 123)]}
srs5_dots = {"_id":171,"name":"srs5","dots":[(583, 68)]}
srs6_dots = {"_id":172,"name":"srs6","dots":[(638, 68)]}
srs7_dots = {"_id":173,"name":"srs7","dots":[(693, 123)]}
srs8_dots = {"_id":174,"name":"srs8","dots":[(308, 178)]}
srs9_dots = {"_id":175,"name":"srs9","dots":[(363, 233)]}
srs10_dots = {"_id":176,"name":"srs10","dots":[(418, 233)]}
srs11_dots = {"_id":177,"name":"srs11","dots":[(473, 178)]}
srs12_dots = {"_id":178,"name":"srs12","dots":[(528, 178)]}
srs13_dots = {"_id":179,"name":"srs13","dots":[(583, 233)]}
srs14_dots = {"_id":180,"name":"srs14","dots":[(638, 233)]}
srs15_dots = {"_id":181,"name":"srs15","dots":[(693, 178)]}
srs16_dots = {"_id":182,"name":"srs16","dots":[(308, 343)]}
srs17_dots = {"_id":183,"name":"srs17","dots":[(363, 288)]}
srs18_dots = {"_id":184,"name":"srs18","dots":[(418, 288)]}
srs19_dots = {"_id":185,"name":"srs19","dots":[(473, 343)]}
srs20_dots = {"_id":186,"name":"srs20","dots":[(528, 343)]}
srs21_dots = {"_id":187,"name":"srs21","dots":[(583, 288)]}
srs22_dots = {"_id":188,"name":"srs22","dots":[(638, 288)]}
srs23_dots = {"_id":189,"name":"srs23","dots":[(693, 343)]}
srs24_dots = {"_id":190,"name":"srs24","dots":[(308, 398)]}
srs25_dots = {"_id":191,"name":"srs25","dots":[(363, 453)]}
srs26_dots = {"_id":192,"name":"srs26","dots":[(418, 453)]}
srs27_dots = {"_id":193,"name":"srs27","dots":[(473, 398)]}
srs28_dots = {"_id":194,"name":"srs28","dots":[(528, 398)]}
srs29_dots = {"_id":195,"name":"srs29","dots":[(583, 453)]}
srs30_dots = {"_id":196,"name":"srs30","dots":[(638, 453)]}
srs31_dots = {"_id":197,"name":"srs31","dots":[(693, 398)]}
sqr0_dots = {"_id":198,"name":"sqr0","dots":[(250, 150)]}
sqr1_dots = {"_id":199,"name":"sqr1","dots":[(350, 150)]}
sqr2_dots = {"_id":200,"name":"sqr2","dots":[(450, 150)]}
sqr3_dots = {"_id":201,"name":"sqr3","dots":[(550, 150)]}
sqr4_dots = {"_id":202,"name":"sqr4","dots":[(650, 150)]}
sqr5_dots = {"_id":203,"name":"sqr5","dots":[(750, 150)]}
sqr6_dots = {"_id":204,"name":"sqr6","dots":[(250, 250)]}
sqr7_dots = {"_id":205,"name":"sqr7","dots":[(350, 250)]}
sqr8_dots = {"_id":206,"name":"sqr8","dots":[(450, 250)]}
sqr9_dots = {"_id":207,"name":"sqr9","dots":[(550, 250)]}
sqr10_dots = {"_id":208,"name":"sqr10","dots":[(650, 250)]}
sqr11_dots = {"_id":209,"name":"sqr11","dots":[(750, 250)]}
sqr12_dots = {"_id":210,"name":"sqr12","dots":[(250, 350)]}
sqr13_dots = {"_id":211,"name":"sqr13","dots":[(350, 350)]}
sqr14_dots = {"_id":212,"name":"sqr14","dots":[(450, 350)]}
sqr15_dots = {"_id":213,"name":"sqr15","dots":[(550, 350)]}
sqr16_dots = {"_id":214,"name":"sqr16","dots":[(650, 350)]}
sqr17_dots = {"_id":215,"name":"sqr17","dots":[(750, 350)]}
sqr18_dots = {"_id":216,"name":"sqr18","dots":[(250, 450)]}
sqr19_dots = {"_id":217,"name":"sqr19","dots":[(350, 450)]}
sqr20_dots = {"_id":218,"name":"sqr20","dots":[(450, 450)]}
sqr21_dots = {"_id":219,"name":"sqr21","dots":[(550, 450)]}
sqr22_dots = {"_id":220,"name":"sqr22","dots":[(650, 450)]}
sqr23_dots = {"_id":221,"name":"sqr23","dots":[(750, 450)]}
sqr24_dots = {"_id":222,"name":"sqr24","dots":[(250, 550)]}
sqr25_dots = {"_id":223,"name":"sqr25","dots":[(350, 550)]}
sqr26_dots = {"_id":224,"name":"sqr26","dots":[(450, 550)]}
sqr27_dots = {"_id":225,"name":"sqr27","dots":[(550, 550)]}
sqr28_dots = {"_id":226,"name":"sqr28","dots":[(650, 550)]}
sqr29_dots = {"_id":227,"name":"sqr29","dots":[(750, 550)]}
sqr30_dots = {"_id":228,"name":"sqr30","dots":[(250, 650)]}
sqr31_dots = {"_id":229,"name":"sqr31","dots":[(350, 650)]}
sqr32_dots = {"_id":230,"name":"sqr32","dots":[(450, 650)]}
sqr33_dots = {"_id":231,"name":"sqr33","dots":[(550, 650)]}
sqr34_dots = {"_id":232,"name":"sqr34","dots":[(650, 650)]}
sqr35_dots = {"_id":233,"name":"sqr35","dots":[(750, 650)]}
stad0_dots = {"_id":234,"name":"stad0","dots":[(256, 192), (199, 133), (317, 85), (316, 166)]}
stad1_dots = {"_id":235,"name":"stad1","dots":[(326, 85), (408, 84), (407, 167), (325, 166)]}
stad2_dots = {"_id":236,"name":"stad2","dots":[(416, 84), (497, 85), (496, 167), (415, 168)]}
stad3_dots = {"_id":237,"name":"stad3","dots":[(505, 84), (587, 84), (587, 167), (505, 167)]}
stad4_dots = {"_id":238,"name":"stad4","dots":[(595, 84), (678, 84), (677, 167), (595, 167)]}
stad5_dots = {"_id":239,"name":"stad5","dots":[(685, 84), (686, 167), (743, 192), (802, 135)]}
stad6_dots = {"_id":240,"name":"stad6","dots":[(146, 255), (194, 142), (251, 197), (225, 256)]}
stad7_dots = {"_id":241,"name":"stad7","dots":[(235, 256), (257, 203), (312, 257)]}
stad8_dots = {"_id":242,"name":"stad8","dots":[(262, 197), (318, 176), (317, 251)]}
stad9_dots = {"_id":243,"name":"stad9","dots":[(325, 257), (325, 174), (407, 174), (407, 257)]}
stad10_dots = {"_id":244,"name":"stad10","dots":[(415, 174), (415, 257), (497, 258), (497, 175)]}
stad11_dots = {"_id":245,"name":"stad11","dots":[(506, 175), (586, 175), (586, 256), (505, 257)]}
stad12_dots = {"_id":246,"name":"stad12","dots":[(595, 257), (595, 175), (677, 174), (677, 257)]}
stad13_dots = {"_id":247,"name":"stad13","dots":[(685, 252), (686, 174), (739, 198)]}
stad14_dots = {"_id":248,"name":"stad14","dots":[(690, 257), (744, 203), (765, 257)]}
stad15_dots = {"_id":249,"name":"stad15","dots":[(772, 257), (748, 197), (807, 139), (855, 257)]}
stad16_dots = {"_id":250,"name":"stad16","dots":[(192, 384), (144, 264), (226, 266), (252, 324)]}
stad17_dots = {"_id":251,"name":"stad17","dots":[(257, 319), (235, 265), (313, 264)]}
stad18_dots = {"_id":252,"name":"stad18","dots":[(261, 325), (317, 267), (317, 347)]}
stad19_dots = {"_id":253,"name":"stad19","dots":[(325, 347), (325, 264), (406, 263), (407, 348)]}
stad20_dots = {"_id":254,"name":"stad20","dots":[(415, 347), (415, 264), (497, 264), (497, 347)]}
stad21_dots = {"_id":255,"name":"stad21","dots":[(506, 346), (506, 265), (587, 264), (587, 348)]}
stad22_dots = {"_id":256,"name":"stad22","dots":[(596, 347), (595, 264), (677, 264), (677, 347)]}
stad23_dots = {"_id":257,"name":"stad23","dots":[(685, 347), (684, 268), (739, 323)]}
stad24_dots = {"_id":258,"name":"stad24","dots":[(688, 264), (765, 265), (743, 318)]}
stad25_dots = {"_id":259,"name":"stad25","dots":[(748, 324), (773, 265), (856, 265), (807, 383)]}
stad26_dots = {"_id":260,"name":"stad26","dots":[(198, 389), (256, 329), (317, 353), (316, 439)]}
stad27_dots = {"_id":261,"name":"stad27","dots":[(326, 438), (325, 355), (407, 355), (407, 437)]}
stad28_dots = {"_id":262,"name":"stad28","dots":[(416, 355), (496, 355), (496, 438), (415, 437)]}
stad29_dots = {"_id":263,"name":"stad29","dots":[(506, 355), (587, 354), (587, 438), (505, 438)]}
stad30_dots = {"_id":264,"name":"stad30","dots":[(595, 354), (677, 354), (677, 438), (595, 438)]}
stad31_dots = {"_id":265,"name":"stad31","dots":[(685, 354), (744, 328), (803, 387), (685, 437)]}
kybrd0_dots = {"_id":266,"name":"kybrd0","dots":[(75, 75)]}
kybrd1_dots = {"_id":267,"name":"kybrd1","dots":[(175, 75)]}
kybrd2_dots = {"_id":268,"name":"kybrd2","dots":[(225, 75)]}
kybrd3_dots = {"_id":269,"name":"kybrd3","dots":[(275, 75)]}
kybrd4_dots = {"_id":270,"name":"kybrd4","dots":[(325, 75)]}
kybrd5_dots = {"_id":271,"name":"kybrd5","dots":[(403, 75)]}
kybrd6_dots = {"_id":272,"name":"kybrd6","dots":[(453, 75)]}
kybrd7_dots = {"_id":273,"name":"kybrd7","dots":[(503, 75)]}
kybrd8_dots = {"_id":274,"name":"kybrd8","dots":[(553, 75)]}
kybrd9_dots = {"_id":275,"name":"kybrd9","dots":[(632, 75)]}
kybrd10_dots = {"_id":276,"name":"kybrd10","dots":[(682, 75)]}
kybrd11_dots = {"_id":277,"name":"kybrd11","dots":[(732, 75)]}
kybrd12_dots = {"_id":278,"name":"kybrd12","dots":[(782, 75)]}
kybrd13_dots = {"_id":279,"name":"kybrd13","dots":[(860, 75)]}
kybrd14_dots = {"_id":280,"name":"kybrd14","dots":[(910, 75)]}
kybrd15_dots = {"_id":281,"name":"kybrd15","dots":[(960, 75)]}
kybrd16_dots = {"_id":282,"name":"kybrd16","dots":[(75, 175)]}
kybrd17_dots = {"_id":283,"name":"kybrd17","dots":[(125, 175)]}
kybrd18_dots = {"_id":284,"name":"kybrd18","dots":[(175, 175)]}
kybrd19_dots = {"_id":285,"name":"kybrd19","dots":[(225, 175)]}
kybrd20_dots = {"_id":286,"name":"kybrd20","dots":[(275, 175)]}
kybrd21_dots = {"_id":287,"name":"kybrd21","dots":[(325, 175)]}
kybrd22_dots = {"_id":288,"name":"kybrd22","dots":[(375, 175)]}
kybrd23_dots = {"_id":289,"name":"kybrd23","dots":[(425, 175)]}
kybrd24_dots = {"_id":290,"name":"kybrd24","dots":[(475, 175)]}
kybrd25_dots = {"_id":291,"name":"kybrd25","dots":[(525, 175)]}
kybrd26_dots = {"_id":292,"name":"kybrd26","dots":[(575, 175)]}
kybrd27_dots = {"_id":293,"name":"kybrd27","dots":[(625, 175)]}
kybrd28_dots = {"_id":294,"name":"kybrd28","dots":[(675, 175)]}
kybrd29_dots = {"_id":295,"name":"kybrd29","dots":[(726, 175), (753, 175), (784, 175)]}
kybrd30_dots = {"_id":296,"name":"kybrd30","dots":[(860, 175)]}
kybrd31_dots = {"_id":297,"name":"kybrd31","dots":[(910, 175)]}
kybrd32_dots = {"_id":298,"name":"kybrd32","dots":[(960, 175)]}
kybrd33_dots = {"_id":299,"name":"kybrd33","dots":[(1039, 175)]}
kybrd34_dots = {"_id":300,"name":"kybrd34","dots":[(1089, 175)]}
kybrd35_dots = {"_id":301,"name":"kybrd35","dots":[(1139, 175)]}
kybrd36_dots = {"_id":302,"name":"kybrd36","dots":[(1189, 175)]}
kybrd37_dots = {"_id":303,"name":"kybrd37","dots":[(74, 225), (87, 225), (100, 225)]}
kybrd38_dots = {"_id":304,"name":"kybrd38","dots":[(150, 225)]}
kybrd39_dots = {"_id":305,"name":"kybrd39","dots":[(200, 225)]}
kybrd40_dots = {"_id":306,"name":"kybrd40","dots":[(250, 225)]}
kybrd41_dots = {"_id":307,"name":"kybrd41","dots":[(300, 225)]}
kybrd42_dots = {"_id":308,"name":"kybrd42","dots":[(350, 225)]}
kybrd43_dots = {"_id":309,"name":"kybrd43","dots":[(400, 225)]}
kybrd44_dots = {"_id":310,"name":"kybrd44","dots":[(450, 225)]}
kybrd45_dots = {"_id":311,"name":"kybrd45","dots":[(500, 225)]}
kybrd46_dots = {"_id":312,"name":"kybrd46","dots":[(550, 225)]}
kybrd47_dots = {"_id":313,"name":"kybrd47","dots":[(600, 225)]}
kybrd48_dots = {"_id":314,"name":"kybrd48","dots":[(650, 225)]}
kybrd49_dots = {"_id":315,"name":"kybrd49","dots":[(700, 225)]}
kybrd50_dots = {"_id":316,"name":"kybrd50","dots":[(755, 225), (768, 250), (781, 225), (765, 275), (771, 275)]}
kybrd51_dots = {"_id":317,"name":"kybrd51","dots":[(860, 225)]}
kybrd52_dots = {"_id":318,"name":"kybrd52","dots":[(910, 225)]}
kybrd53_dots = {"_id":319,"name":"kybrd53","dots":[(960, 225)]}
kybrd54_dots = {"_id":320,"name":"kybrd54","dots":[(1039, 225)]}
kybrd55_dots = {"_id":321,"name":"kybrd55","dots":[(1089, 225)]}
kybrd56_dots = {"_id":322,"name":"kybrd56","dots":[(1139, 225)]}
kybrd57_dots = {"_id":323,"name":"kybrd57","dots":[(1189, 225), (1189, 250), (1189, 275)]}
kybrd58_dots = {"_id":324,"name":"kybrd58","dots":[(82, 275), (92, 275), (102, 275)]}
kybrd59_dots = {"_id":325,"name":"kybrd59","dots":[(160, 275)]}
kybrd60_dots = {"_id":326,"name":"kybrd60","dots":[(210, 275)]}
kybrd61_dots = {"_id":327,"name":"kybrd61","dots":[(260, 275)]}
kybrd62_dots = {"_id":328,"name":"kybrd62","dots":[(310, 275)]}
kybrd63_dots = {"_id":329,"name":"kybrd63","dots":[(360, 275)]}
kybrd64_dots = {"_id":330,"name":"kybrd64","dots":[(410, 275)]}
kybrd65_dots = {"_id":331,"name":"kybrd65","dots":[(460, 275)]}
kybrd66_dots = {"_id":332,"name":"kybrd66","dots":[(510, 275)]}
kybrd67_dots = {"_id":333,"name":"kybrd67","dots":[(560, 275)]}
kybrd68_dots = {"_id":334,"name":"kybrd68","dots":[(610, 275)]}
kybrd69_dots = {"_id":335,"name":"kybrd69","dots":[(660, 275)]}
kybrd70_dots = {"_id":336,"name":"kybrd70","dots":[(710, 275)]}
kybrd71_dots = {"_id":337,"name":"kybrd71","dots":[(1039, 275)]}
kybrd72_dots = {"_id":338,"name":"kybrd72","dots":[(1089, 275)]}
kybrd73_dots = {"_id":339,"name":"kybrd73","dots":[(1139, 275)]}
kybrd74_dots = {"_id":340,"name":"kybrd74","dots":[(75, 325)]}
kybrd75_dots = {"_id":341,"name":"kybrd75","dots":[(125, 325)]}
kybrd76_dots = {"_id":342,"name":"kybrd76","dots":[(175, 325)]}
kybrd77_dots = {"_id":343,"name":"kybrd77","dots":[(225, 325)]}
kybrd78_dots = {"_id":344,"name":"kybrd78","dots":[(275, 325)]}
kybrd79_dots = {"_id":345,"name":"kybrd79","dots":[(325, 325)]}
kybrd80_dots = {"_id":346,"name":"kybrd80","dots":[(375, 325)]}
kybrd81_dots = {"_id":347,"name":"kybrd81","dots":[(425, 325)]}
kybrd82_dots = {"_id":348,"name":"kybrd82","dots":[(475, 325)]}
kybrd83_dots = {"_id":349,"name":"kybrd83","dots":[(525, 325)]}
kybrd84_dots = {"_id":350,"name":"kybrd84","dots":[(575, 325)]}
kybrd85_dots = {"_id":351,"name":"kybrd85","dots":[(625, 325)]}
kybrd86_dots = {"_id":352,"name":"kybrd86","dots":[(675, 325), (700, 325), (728, 325), (753, 325), (778, 325)]}
kybrd87_dots = {"_id":353,"name":"kybrd87","dots":[(910, 325)]}
kybrd88_dots = {"_id":354,"name":"kybrd88","dots":[(1039, 325)]}
kybrd89_dots = {"_id":355,"name":"kybrd89","dots":[(1089, 325)]}
kybrd90_dots = {"_id":356,"name":"kybrd90","dots":[(1139, 325)]}
kybrd91_dots = {"_id":357,"name":"kybrd91","dots":[(1189, 325), (1189, 350), (1189, 375)]}
kybrd92_dots = {"_id":358,"name":"kybrd92","dots":[(80, 375)]}
kybrd93_dots = {"_id":359,"name":"kybrd93","dots":[(140, 375)]}
kybrd94_dots = {"_id":360,"name":"kybrd94","dots":[(200, 375)]}
kybrd95_dots = {"_id":361,"name":"kybrd95","dots":[(260, 375), (290, 375), (320, 375), (350, 375), (390, 375), (420, 375), (450, 375), (480, 375), (520, 375)]}
kybrd96_dots = {"_id":362,"name":"kybrd96","dots":[(580, 375)]}
kybrd97_dots = {"_id":363,"name":"kybrd97","dots":[(640, 375)]}
kybrd98_dots = {"_id":364,"name":"kybrd98","dots":[(700, 375)]}
kybrd99_dots = {"_id":365,"name":"kybrd99","dots":[(758, 375), (768, 375), (778, 375)]}
kybrd100_dots = {"_id":366,"name":"kybrd100","dots":[(860, 375)]}
kybrd101_dots = {"_id":367,"name":"kybrd101","dots":[(910, 375)]}
kybrd102_dots = {"_id":368,"name":"kybrd102","dots":[(960, 375)]}
kybrd103_dots = {"_id":369,"name":"kybrd103","dots":[(1039, 375), (1064, 375), (1089, 375)]}
kybrd104_dots = {"_id":370,"name":"kybrd104","dots":[(1139, 375)]}

collection.insert_one(alaska_dots)
collection.insert_one(north_west_territory_dots)
collection.insert_one(alberta_dots)
collection.insert_one(ontario_dots)
collection.insert_one(quebec_dots)
collection.insert_one(western_united_states_dots)
collection.insert_one(eastern_united_states_dots)
collection.insert_one(greenland_dots)
collection.insert_one(mexico_dots)
collection.insert_one(venezuela_dots)
collection.insert_one(peru_dots)
collection.insert_one(argentina_dots)
collection.insert_one(brazil_dots)
collection.insert_one(iceland_dots)
collection.insert_one(scandinavia_dots)
collection.insert_one(great_britain_dots)
collection.insert_one(western_europe_dots)
collection.insert_one(northern_europe_dots)
collection.insert_one(southern_europe_dots)
collection.insert_one(ukraine_dots)
collection.insert_one(north_africa_dots)
collection.insert_one(egypt_dots)
collection.insert_one(sudan_dots)
collection.insert_one(congo_dots)
collection.insert_one(south_africa_dots)
collection.insert_one(madagascar_dots)
collection.insert_one(middle_east_dots)
collection.insert_one(india_dots)
collection.insert_one(siam_dots)
collection.insert_one(china_dots)
collection.insert_one(central_asia_dots)
collection.insert_one(ural_dots)
collection.insert_one(siberia_dots)
collection.insert_one(yakutsk_dots)
collection.insert_one(irkutsk_dots)
collection.insert_one(kamtchatka_dots)
collection.insert_one(mongolia_dots)
collection.insert_one(japan_dots)
collection.insert_one(indonesia_dots)
collection.insert_one(papau_new_guinea_dots)
collection.insert_one(western_australia_dots)
collection.insert_one(eastern_australia_dots)
collection.insert_one(hex0_dots)
collection.insert_one(hex1_dots)
collection.insert_one(hex2_dots)
collection.insert_one(hex3_dots)
collection.insert_one(hex4_dots)
collection.insert_one(hex5_dots)
collection.insert_one(hex6_dots)
collection.insert_one(hex7_dots)
collection.insert_one(hex8_dots)
collection.insert_one(hex9_dots)
collection.insert_one(hex10_dots)
collection.insert_one(hex11_dots)
collection.insert_one(hex12_dots)
collection.insert_one(hex13_dots)
collection.insert_one(hex14_dots)
collection.insert_one(hex15_dots)
collection.insert_one(hex16_dots)
collection.insert_one(hex17_dots)
collection.insert_one(hex18_dots)
collection.insert_one(hex19_dots)
collection.insert_one(hex20_dots)
collection.insert_one(hex21_dots)
collection.insert_one(hex22_dots)
collection.insert_one(hex23_dots)
collection.insert_one(hex24_dots)
collection.insert_one(hex25_dots)
collection.insert_one(hex26_dots)
collection.insert_one(hex27_dots)
collection.insert_one(hex28_dots)
collection.insert_one(hex29_dots)
collection.insert_one(hex30_dots)
collection.insert_one(hex31_dots)
collection.insert_one(hex32_dots)
collection.insert_one(hex33_dots)
collection.insert_one(hex34_dots)
collection.insert_one(hex35_dots)
collection.insert_one(hex36_dots)
collection.insert_one(hex37_dots)
collection.insert_one(hex38_dots)
collection.insert_one(hex39_dots)
collection.insert_one(hex40_dots)
collection.insert_one(hex41_dots)
collection.insert_one(hex42_dots)
collection.insert_one(hex43_dots)
collection.insert_one(hex44_dots)
collection.insert_one(hex45_dots)
collection.insert_one(hex46_dots)
collection.insert_one(hex47_dots)
collection.insert_one(hex48_dots)
collection.insert_one(hex49_dots)
collection.insert_one(hex50_dots)
collection.insert_one(hex51_dots)
collection.insert_one(hex52_dots)
collection.insert_one(hex53_dots)
collection.insert_one(hex54_dots)
collection.insert_one(hex55_dots)
collection.insert_one(pyr0_dots)
collection.insert_one(pyr1_dots)
collection.insert_one(pyr2_dots)
collection.insert_one(pyr3_dots)
collection.insert_one(pyr4_dots)
collection.insert_one(pyr5_dots)
collection.insert_one(pyr6_dots)
collection.insert_one(pyr7_dots)
collection.insert_one(pyr8_dots)
collection.insert_one(pyr9_dots)
collection.insert_one(pyr10_dots)
collection.insert_one(pyr11_dots)
collection.insert_one(pyr12_dots)
collection.insert_one(pyr13_dots)
collection.insert_one(pyr14_dots)
collection.insert_one(pyr15_dots)
collection.insert_one(pyr16_dots)
collection.insert_one(pyr17_dots)
collection.insert_one(pyr18_dots)
collection.insert_one(pyr19_dots)
collection.insert_one(pyr20_dots)
collection.insert_one(pyr21_dots)
collection.insert_one(pyr22_dots)
collection.insert_one(pyr23_dots)
collection.insert_one(pyr24_dots)
collection.insert_one(pyr25_dots)
collection.insert_one(pyr26_dots)
collection.insert_one(pyr27_dots)
collection.insert_one(pyr28_dots)
collection.insert_one(pyr29_dots)
collection.insert_one(pyr30_dots)
collection.insert_one(pyr31_dots)
collection.insert_one(pyr32_dots)
collection.insert_one(pyr33_dots)
collection.insert_one(pyr34_dots)
collection.insert_one(pyr35_dots)
collection.insert_one(pyr36_dots)
collection.insert_one(pyr37_dots)
collection.insert_one(pyr38_dots)
collection.insert_one(pyr39_dots)
collection.insert_one(pyr40_dots)
collection.insert_one(pyr41_dots)
collection.insert_one(pyr42_dots)
collection.insert_one(pyr43_dots)
collection.insert_one(pyr44_dots)
collection.insert_one(pyr45_dots)
collection.insert_one(pyr46_dots)
collection.insert_one(pyr47_dots)
collection.insert_one(pyr48_dots)
collection.insert_one(pyr49_dots)
collection.insert_one(pyr50_dots)
collection.insert_one(pyr51_dots)
collection.insert_one(pyr52_dots)
collection.insert_one(pyr53_dots)
collection.insert_one(pyr54_dots)
collection.insert_one(pyr55_dots)
collection.insert_one(pyr56_dots)
collection.insert_one(pyr57_dots)
collection.insert_one(pyr58_dots)
collection.insert_one(pyr59_dots)
collection.insert_one(pyr60_dots)
collection.insert_one(pyr61_dots)
collection.insert_one(pyr62_dots)
collection.insert_one(pyr63_dots)
collection.insert_one(qck0_dots)
collection.insert_one(qck1_dots)
collection.insert_one(qck2_dots)
collection.insert_one(qck3_dots)
collection.insert_one(srs0_dots)
collection.insert_one(srs1_dots)
collection.insert_one(srs2_dots)
collection.insert_one(srs3_dots)
collection.insert_one(srs4_dots)
collection.insert_one(srs5_dots)
collection.insert_one(srs6_dots)
collection.insert_one(srs7_dots)
collection.insert_one(srs8_dots)
collection.insert_one(srs9_dots)
collection.insert_one(srs10_dots)
collection.insert_one(srs11_dots)
collection.insert_one(srs12_dots)
collection.insert_one(srs13_dots)
collection.insert_one(srs14_dots)
collection.insert_one(srs15_dots)
collection.insert_one(srs16_dots)
collection.insert_one(srs17_dots)
collection.insert_one(srs18_dots)
collection.insert_one(srs19_dots)
collection.insert_one(srs20_dots)
collection.insert_one(srs21_dots)
collection.insert_one(srs22_dots)
collection.insert_one(srs23_dots)
collection.insert_one(srs24_dots)
collection.insert_one(srs25_dots)
collection.insert_one(srs26_dots)
collection.insert_one(srs27_dots)
collection.insert_one(srs28_dots)
collection.insert_one(srs29_dots)
collection.insert_one(srs30_dots)
collection.insert_one(srs31_dots)
collection.insert_one(sqr0_dots)
collection.insert_one(sqr1_dots)
collection.insert_one(sqr2_dots)
collection.insert_one(sqr3_dots)
collection.insert_one(sqr4_dots)
collection.insert_one(sqr5_dots)
collection.insert_one(sqr6_dots)
collection.insert_one(sqr7_dots)
collection.insert_one(sqr8_dots)
collection.insert_one(sqr9_dots)
collection.insert_one(sqr10_dots)
collection.insert_one(sqr11_dots)
collection.insert_one(sqr12_dots)
collection.insert_one(sqr13_dots)
collection.insert_one(sqr14_dots)
collection.insert_one(sqr15_dots)
collection.insert_one(sqr16_dots)
collection.insert_one(sqr17_dots)
collection.insert_one(sqr18_dots)
collection.insert_one(sqr19_dots)
collection.insert_one(sqr20_dots)
collection.insert_one(sqr21_dots)
collection.insert_one(sqr22_dots)
collection.insert_one(sqr23_dots)
collection.insert_one(sqr24_dots)
collection.insert_one(sqr25_dots)
collection.insert_one(sqr26_dots)
collection.insert_one(sqr27_dots)
collection.insert_one(sqr28_dots)
collection.insert_one(sqr29_dots)
collection.insert_one(sqr30_dots)
collection.insert_one(sqr31_dots)
collection.insert_one(sqr32_dots)
collection.insert_one(sqr33_dots)
collection.insert_one(sqr34_dots)
collection.insert_one(sqr35_dots)
collection.insert_one(stad0_dots)
collection.insert_one(stad1_dots)
collection.insert_one(stad2_dots)
collection.insert_one(stad3_dots)
collection.insert_one(stad4_dots)
collection.insert_one(stad5_dots)
collection.insert_one(stad6_dots)
collection.insert_one(stad7_dots)
collection.insert_one(stad8_dots)
collection.insert_one(stad9_dots)
collection.insert_one(stad10_dots)
collection.insert_one(stad11_dots)
collection.insert_one(stad12_dots)
collection.insert_one(stad13_dots)
collection.insert_one(stad14_dots)
collection.insert_one(stad15_dots)
collection.insert_one(stad16_dots)
collection.insert_one(stad17_dots)
collection.insert_one(stad18_dots)
collection.insert_one(stad19_dots)
collection.insert_one(stad20_dots)
collection.insert_one(stad21_dots)
collection.insert_one(stad22_dots)
collection.insert_one(stad23_dots)
collection.insert_one(stad24_dots)
collection.insert_one(stad25_dots)
collection.insert_one(stad26_dots)
collection.insert_one(stad27_dots)
collection.insert_one(stad28_dots)
collection.insert_one(stad29_dots)
collection.insert_one(stad30_dots)
collection.insert_one(stad31_dots)
collection.insert_one(kybrd0_dots)
collection.insert_one(kybrd1_dots)
collection.insert_one(kybrd2_dots)
collection.insert_one(kybrd3_dots)
collection.insert_one(kybrd4_dots)
collection.insert_one(kybrd5_dots)
collection.insert_one(kybrd6_dots)
collection.insert_one(kybrd7_dots)
collection.insert_one(kybrd8_dots)
collection.insert_one(kybrd9_dots)
collection.insert_one(kybrd10_dots)
collection.insert_one(kybrd11_dots)
collection.insert_one(kybrd12_dots)
collection.insert_one(kybrd13_dots)
collection.insert_one(kybrd14_dots)
collection.insert_one(kybrd15_dots)
collection.insert_one(kybrd16_dots)
collection.insert_one(kybrd17_dots)
collection.insert_one(kybrd18_dots)
collection.insert_one(kybrd19_dots)
collection.insert_one(kybrd20_dots)
collection.insert_one(kybrd21_dots)
collection.insert_one(kybrd22_dots)
collection.insert_one(kybrd23_dots)
collection.insert_one(kybrd24_dots)
collection.insert_one(kybrd25_dots)
collection.insert_one(kybrd26_dots)
collection.insert_one(kybrd27_dots)
collection.insert_one(kybrd28_dots)
collection.insert_one(kybrd29_dots)
collection.insert_one(kybrd30_dots)
collection.insert_one(kybrd31_dots)
collection.insert_one(kybrd32_dots)
collection.insert_one(kybrd33_dots)
collection.insert_one(kybrd34_dots)
collection.insert_one(kybrd35_dots)
collection.insert_one(kybrd36_dots)
collection.insert_one(kybrd37_dots)
collection.insert_one(kybrd38_dots)
collection.insert_one(kybrd39_dots)
collection.insert_one(kybrd40_dots)
collection.insert_one(kybrd41_dots)
collection.insert_one(kybrd42_dots)
collection.insert_one(kybrd43_dots)
collection.insert_one(kybrd44_dots)
collection.insert_one(kybrd45_dots)
collection.insert_one(kybrd46_dots)
collection.insert_one(kybrd47_dots)
collection.insert_one(kybrd48_dots)
collection.insert_one(kybrd49_dots)
collection.insert_one(kybrd50_dots)
collection.insert_one(kybrd51_dots)
collection.insert_one(kybrd52_dots)
collection.insert_one(kybrd53_dots)
collection.insert_one(kybrd54_dots)
collection.insert_one(kybrd55_dots)
collection.insert_one(kybrd56_dots)
collection.insert_one(kybrd57_dots)
collection.insert_one(kybrd58_dots)
collection.insert_one(kybrd59_dots)
collection.insert_one(kybrd60_dots)
collection.insert_one(kybrd61_dots)
collection.insert_one(kybrd62_dots)
collection.insert_one(kybrd63_dots)
collection.insert_one(kybrd64_dots)
collection.insert_one(kybrd65_dots)
collection.insert_one(kybrd66_dots)
collection.insert_one(kybrd67_dots)
collection.insert_one(kybrd68_dots)
collection.insert_one(kybrd69_dots)
collection.insert_one(kybrd70_dots)
collection.insert_one(kybrd71_dots)
collection.insert_one(kybrd72_dots)
collection.insert_one(kybrd73_dots)
collection.insert_one(kybrd74_dots)
collection.insert_one(kybrd75_dots)
collection.insert_one(kybrd76_dots)
collection.insert_one(kybrd77_dots)
collection.insert_one(kybrd78_dots)
collection.insert_one(kybrd79_dots)
collection.insert_one(kybrd80_dots)
collection.insert_one(kybrd81_dots)
collection.insert_one(kybrd82_dots)
collection.insert_one(kybrd83_dots)
collection.insert_one(kybrd84_dots)
collection.insert_one(kybrd85_dots)
collection.insert_one(kybrd86_dots)
collection.insert_one(kybrd87_dots)
collection.insert_one(kybrd88_dots)
collection.insert_one(kybrd89_dots)
collection.insert_one(kybrd90_dots)
collection.insert_one(kybrd91_dots)
collection.insert_one(kybrd92_dots)
collection.insert_one(kybrd93_dots)
collection.insert_one(kybrd94_dots)
collection.insert_one(kybrd95_dots)
collection.insert_one(kybrd96_dots)
collection.insert_one(kybrd97_dots)
collection.insert_one(kybrd98_dots)
collection.insert_one(kybrd99_dots)
collection.insert_one(kybrd100_dots)
collection.insert_one(kybrd101_dots)
collection.insert_one(kybrd102_dots)
collection.insert_one(kybrd103_dots)
collection.insert_one(kybrd104_dots)