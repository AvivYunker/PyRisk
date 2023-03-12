import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_positions"]


alaska_position = {"_id":0, "name":"Alaska","position":(26,54)}
north_west_territory_position = {"_id":1, "name":"North-West-Territory","position":(100,53)}
alberta_position = {"_id":2, "name":"Alberta","position":(106,97)}
ontario_position = {"_id":3, "name":"Ontario","position":(193,97)}
quebec_position = {"_id":4, "name":"Quebec","position":(268,88)}
western_united_states_position = {"_id":5, "name":"Western-United-States","position":(83,144)}
eastern_united_states_position = {"_id":6, "name":"Eastern-United-States","position":(136,144)}
greenland_position = {"_id":7, "name":"Greenland","position":(380,13)}
mexico_position = {"_id":8, "name":"Mexico","position":(95,217)}
venezuela_position = {"_id":9, "name":"Venezuela","position":(228,310)}
peru_position = {"_id":10, "name":"Peru","position":(219,359)}
argentina_position = {"_id":11, "name":"Argentina","position":(268,445)}
brazil_position = {"_id":12, "name":"Brazil","position":(250,342)}
iceland_position = {"_id":13, "name":"Iceland","position":(497,67)}
scandinavia_position = {"_id":14, "name":"Scandinavia","position":(583,52)}
great_britain_position = {"_id":15, "name":"Great-Britan","position":(502,111)}
western_europe_position = {"_id":16, "name":"Western-Europe","position":(496,136)}
northern_europe_position = {"_id":17, "name":"Northern-Europe","position":(574,109)}
southern_europe_position = {"_id":18, "name":"Southern-Europe","position":(584,144)}
ukraine_position = {"_id":19, "name":"Ukraine","position":(637,58)}
north_africa_position = {"_id":20, "name":"North-Africa","position":(488,197)}
egypt_position = {"_id":21, "name":"Egypt","position":(597,216)}
sudan_position = {"_id":22, "name":"Sudan","position":(648,261)}
congo_position = {"_id":23, "name":"Congo","position":(595,315)}
south_africa_position = {"_id":24, "name":"South-Africa","position":(606,392)}
madagascar_position = {"_id":25, "name":"Madagascar","position":(734,424)}
middle_east_position = {"_id":26, "name":"Middle-East","position":(660,175)}
india_position = {"_id":27, "name":"India","position":(797,191)}
siam_position = {"_id":28, "name":"Siam","position":(934,238)}
china_position = {"_id":29, "name":"China","position":(843,143)}
central_asia_position = {"_id":30, "name":"Central-Asia","position":(732,117)}
ural_position = {"_id":31, "name":"Ural","position":(751,48)}
siberia_position = {"_id":32, "name":"Siberia","position":(800,31)}
yakutsk_position = {"_id":33, "name":"Yakutsk","position":(890,45)}
irkutsk_position = {"_id":34, "name":"Irkutsk","position":(880,80)}
kamtchatka_position = {"_id":35, "name":"Kamtchatka","position":(1010,58)}
mongolia_position = {"_id":36, "name":"Mongolia","position":(882,124)}
japan_position = {"_id":37, "name":"Japan","position":(1073,164)}
indonesia_position = {"_id":38, "name":"Indonesia","position":(955,336)}
papau_new_guinea_position = {"_id":39, "name":"Papau-New-Guinea","position":(1087,355)}
western_australia_position = {"_id":40, "name":"Western-Australia","position":(1018,429)}
eastern_australia_position = {"_id":41, "name":"Eastern-Australia","position":(1075,419)}
hex0_position = {"_id":42, "name":"1st-Hexagon","position":(23,52,)}
hex1_position = {"_id":43, "name":"2nd-Hexagon","position":(103,99)}
hex2_position = {"_id":44, "name":"3rd-Hexagon","position":(182,52)}
hex3_position = {"_id":45, "name":"4th-Hexagon","position":(262,99)}
hex4_position = {"_id":46, "name":"5th-Hexagon","position":(341,52)}
hex5_position = {"_id":47, "name":"6th-Hexagon","position":(421,99)}
hex6_position = {"_id":48, "name":"7th-Hexagon","position":(500,52)}
hex7_position = {"_id":49, "name":"8th-Hexagon","position":(580,99)}
hex8_position = {"_id":50, "name":"9th-Hexagon","position":(659,52)}
hex9_position = {"_id":51, "name":"10th-Hexagon","position":(739,99)}
hex10_position = {"_id":52, "name":"11th-Hexagon","position":(818,52)}
hex11_position = {"_id":53, "name":"12th-Hexagon","position":(898,99)}
hex12_position = {"_id":54, "name":"13th-Hexagon","position":(977,52)}
hex13_position = {"_id":55, "name":"14th-Hexagon","position":(1057,99)}
hex14_position = {"_id":56, "name":"15th-Hexagon","position":(23,147)}
hex15_position = {"_id":57, "name":"16th-Hexagon","position":(103,195)}
hex16_position = {"_id":58, "name":"17th-Hexagon","position":(182,147)}
hex17_position = {"_id":59, "name":"18th-Hexagon","position":(262,195)}
hex18_position = {"_id":60, "name":"19th-Hexagon","position":(341,147)}
hex19_position = {"_id":61, "name":"20th-Hexagon","position":(421,195)}
hex20_position = {"_id":62, "name":"21th-Hexagon","position":(500,147)}
hex21_position = {"_id":63, "name":"22th-Hexagon","position":(580,195)}
hex22_position = {"_id":64, "name":"23th-Hexagon","position":(659,147)}
hex23_position = {"_id":65, "name":"24th-Hexagon","position":(739,195)}
hex24_position = {"_id":66, "name":"25th-Hexagon","position":(818,147)}
hex25_position = {"_id":67, "name":"26th-Hexagon","position":(898,195)}
hex26_position = {"_id":68, "name":"27th-Hexagon","position":(977,147)}
hex27_position = {"_id":69, "name":"28th-Hexagon","position":(1057,195)}
hex28_position = {"_id":70, "name":"29th-Hexagon","position":(24,242)}
hex29_position = {"_id":71, "name":"30th-Hexagon","position":(103,290)}
hex30_position = {"_id":72, "name":"31th-Hexagon","position":(183,242)}
hex31_position = {"_id":73, "name":"32th-Hexagon","position":(262,290)}
hex32_position = {"_id":74, "name":"33th-Hexagon","position":(342,242)}
hex33_position = {"_id":75, "name":"34th-Hexagon","position":(421,290)}
hex34_position = {"_id":76, "name":"35th-Hexagon","position":(501,242)}
hex35_position = {"_id":77, "name":"36th-Hexagon","position":(580,290)}
hex36_position = {"_id":78, "name":"37th-Hexagon","position":(660,242)}
hex37_position = {"_id":79, "name":"38th-Hexagon","position":(739,290)}
hex38_position = {"_id":80, "name":"39th-Hexagon","position":(819,242)}
hex39_position = {"_id":81, "name":"40th-Hexagon","position":(898,290)}
hex40_position = {"_id":82, "name":"41th-Hexagon","position":(978,242)}
hex41_position = {"_id":83, "name":"42th-Hexagon","position":(1057,290)}
hex42_position = {"_id":84, "name":"43th-Hexagon","position":(23,338)}
hex43_position = {"_id":85, "name":"44th-Hexagon","position":(103,386)}
hex44_position = {"_id":86, "name":"45th-Hexagon","position":(182,338)}
hex45_position = {"_id":87, "name":"46th-Hexagon","position":(262,386)}
hex46_position = {"_id":88, "name":"47th-Hexagon","position":(341,338)}
hex47_position = {"_id":89, "name":"48th-Hexagon","position":(421,386)}
hex48_position = {"_id":90, "name":"49th-Hexagon","position":(500,338)}
hex49_position = {"_id":91, "name":"50th-Hexagon","position":(580,386)}
hex50_position = {"_id":92, "name":"51th-Hexagon","position":(659,338)}
hex51_position = {"_id":93, "name":"52th-Hexagon","position":(739,386)}
hex52_position = {"_id":94, "name":"53th-Hexagon","position":(818,338)}
hex53_position = {"_id":95, "name":"54th-Hexagon","position":(898,386)}
hex54_position = {"_id":96, "name":"55th-Hexagon","position":(977,338)}
hex55_position = {"_id":97, "name":"56th-Hexagon","position":(1057,386)}
pyr0_position = {"_id":98, "name":"1st-Pyramid-Triangle","position":(473,64)}
pyr1_position = {"_id":99, "name":"2nd-Pyramid-Triangle","position":(443,124)}
pyr2_position = {"_id":100, "name":"3rd-Pyramid-Triangle","position":(473,122)}
pyr3_position = {"_id":101, "name":"4th-Pyramid-Triangle","position":(503,124)}
pyr4_position = {"_id":102, "name":"5th-Pyramid-Triangle","position":(413,184)}
pyr5_position = {"_id":103, "name":"6th-Pyramid-Triangle","position":(443,182)}
pyr6_position = {"_id":104, "name":"7th-Pyramid-Triangle","position":(473,184)}
pyr7_position = {"_id":105, "name":"8th-Pyramid-Triangle","position":(503,182)}
pyr8_position = {"_id":106, "name":"9th-Pyramid-Triangle","position":(533,184)}
pyr9_position = {"_id":107, "name":"10th-Pyramid-Triangle","position":(383,244)}
pyr10_position = {"_id":108, "name":"11th-Pyramid-Triangle","position":(413,242)}
pyr11_position = {"_id":109, "name":"12th-Pyramid-Triangle","position":(443,244)}
pyr12_position = {"_id":110, "name":"13th-Pyramid-Triangle","position":(473,242)}
pyr13_position = {"_id":111, "name":"14th-Pyramid-Triangle","position":(503,244)}
pyr14_position = {"_id":112, "name":"15th-Pyramid-Triangle","position":(533,242)}
pyr15_position = {"_id":113, "name":"16th-Pyramid-Triangle","position":(563,244)}
pyr16_position = {"_id":114, "name":"17th-Pyramid-Triangle","position":(353,304)}
pyr17_position = {"_id":115, "name":"18th-Pyramid-Triangle","position":(383,302)}
pyr18_position = {"_id":116, "name":"19th-Pyramid-Triangle","position":(413,304)}
pyr19_position = {"_id":117, "name":"20th-Pyramid-Triangle","position":(443,302)}
pyr20_position = {"_id":118, "name":"21th-Pyramid-Triangle","position":(473,304)}
pyr21_position = {"_id":119, "name":"22th-Pyramid-Triangle","position":(503,302)}
pyr22_position = {"_id":120, "name":"23th-Pyramid-Triangle","position":(533,304)}
pyr23_position = {"_id":121, "name":"24th-Pyramid-Triangle","position":(563,302)}
pyr24_position = {"_id":122, "name":"25th-Pyramid-Triangle","position":(593,304)}
pyr25_position = {"_id":123, "name":"26th-Pyramid-Triangle","position":(323,364)}
pyr26_position = {"_id":124, "name":"27th-Pyramid-Triangle","position":(353,362)}
pyr27_position = {"_id":125, "name":"28th-Pyramid-Triangle","position":(383,364)}
pyr28_position = {"_id":126, "name":"29th-Pyramid-Triangle","position":(413,362)}
pyr29_position = {"_id":127, "name":"30th-Pyramid-Triangle","position":(443,364)}
pyr30_position = {"_id":128, "name":"31th-Pyramid-Triangle","position":(473,362)}
pyr31_position = {"_id":129, "name":"32th-Pyramid-Triangle","position":(503,364)}
pyr32_position = {"_id":130, "name":"33th-Pyramid-Triangle","position":(533,362)}
pyr33_position = {"_id":131, "name":"34th-Pyramid-Triangle","position":(563,364)}
pyr34_position = {"_id":132, "name":"35th-Pyramid-Triangle","position":(593,362)}
pyr35_position = {"_id":133, "name":"36th-Pyramid-Triangle","position":(623,364)}
pyr36_position = {"_id":134, "name":"37th-Pyramid-Triangle","position":(293,424)}
pyr37_position = {"_id":135, "name":"38th-Pyramid-Triangle","position":(323,422)}
pyr38_position = {"_id":136, "name":"39th-Pyramid-Triangle","position":(353,424)}
pyr39_position = {"_id":137, "name":"40th-Pyramid-Triangle","position":(383,422)}
pyr40_position = {"_id":138, "name":"41th-Pyramid-Triangle","position":(413,424)}
pyr41_position = {"_id":139, "name":"42th-Pyramid-Triangle","position":(443,422)}
pyr42_position = {"_id":140, "name":"43th-Pyramid-Triangle","position":(473,424)}
pyr43_position = {"_id":141, "name":"44th-Pyramid-Triangle","position":(503,422)}
pyr44_position = {"_id":142, "name":"45th-Pyramid-Triangle","position":(533,424)}
pyr45_position = {"_id":143, "name":"46th-Pyramid-Triangle","position":(563,422)}
pyr46_position = {"_id":144, "name":"47th-Pyramid-Triangle","position":(593,424)}
pyr47_position = {"_id":145, "name":"48th-Pyramid-Triangle","position":(623,422)}
pyr48_position = {"_id":146, "name":"49th-Pyramid-Triangle","position":(653,424)}
pyr49_position = {"_id":147, "name":"50th-Pyramid-Triangle","position":(263,484)}
pyr50_position = {"_id":148, "name":"51th-Pyramid-Triangle","position":(293,482)}
pyr51_position = {"_id":149, "name":"52th-Pyramid-Triangle","position":(323,484)}
pyr52_position = {"_id":150, "name":"53th-Pyramid-Triangle","position":(353,482)}
pyr53_position = {"_id":151, "name":"54th-Pyramid-Triangle","position":(383,484)}
pyr54_position = {"_id":152, "name":"55th-Pyramid-Triangle","position":(413,482)}
pyr55_position = {"_id":153, "name":"56th-Pyramid-Triangle","position":(443,484)}
pyr56_position = {"_id":154, "name":"57th-Pyramid-Triangle","position":(473,482)}
pyr57_position = {"_id":155, "name":"58th-Pyramid-Triangle","position":(503,484)}
pyr58_position = {"_id":156, "name":"59th-Pyramid-Triangle","position":(533,482)}
pyr59_position = {"_id":157, "name":"60th-Pyramid-Triangle","position":(563,484)}
pyr60_position = {"_id":158, "name":"61th-Pyramid-Triangle","position":(593,482)}
pyr61_position = {"_id":159, "name":"62th-Pyramid-Triangle","position":(623,484)}
pyr62_position = {"_id":160, "name":"63th-Pyramid-Triangle","position":(653,482)}
pyr63_position = {"_id":161, "name":"64th-Pyramid-Triangle","position":(683,484)}
qck0_position = {"_id":162, "name":"1st-Quick-Triangle","position":(351,103)}
qck1_position = {"_id":163, "name":"2nd-Quick-Triangle","position":(348,105)}
qck2_position = {"_id":164, "name":"3rd-Quick-Triangle","position":(498,105)}
qck3_position = {"_id":165, "name":"4th-Quick-Triangle","position":(350,253)}
srs0_position = {"_id":166, "name":"1st-Serious-Triangle","position":(283,45)}
srs1_position = {"_id":167, "name":"2nd-Serious-Triangle","position":(286,43)}
srs2_position = {"_id":168, "name":"3rd-Serious-Triangle","position":(393,43)}
srs3_position = {"_id":169, "name":"4th-Serious-Triangle","position":(395,45)}
srs4_position = {"_id":170, "name":"5th-Serious-Triangle","position":(503,45)}
srs5_position = {"_id":171, "name":"6th-Serious-Triangle","position":(506,43)}
srs6_position = {"_id":172, "name":"7th-Serious-Triangle","position":(613,43)}
srs7_position = {"_id":173, "name":"8th-Serious-Triangle","position":(615,45)}
srs8_position = {"_id":174, "name":"9th-Serious-Triangle","position":(283,153)}
srs9_position = {"_id":175, "name":"10th-Serious-Triangle","position":(285,155)}
srs10_position = {"_id":176, "name":"11th-Serious-Triangle","position":(393,155)}
srs11_position = {"_id":177, "name":"12th-Serious-Triangle","position":(396,153)}
srs12_position = {"_id":178, "name":"13th-Serious-Triangle","position":(503,153)}
srs13_position = {"_id":179, "name":"14th-Serious-Triangle","position":(505,155)}
srs14_position = {"_id":180, "name":"15th-Serious-Triangle","position":(613,155)}
srs15_position = {"_id":181, "name":"16th-Serious-Triangle","position":(616,153)}
srs16_position = {"_id":182, "name":"17th-Serious-Triangle","position":(283,265)}
srs17_position = {"_id":183, "name":"18th-Serious-Triangle","position":(286,263)}
srs18_position = {"_id":184, "name":"19th-Serious-Triangle","position":(393,263)}
srs19_position = {"_id":185, "name":"20th-Serious-Triangle","position":(395,265)}
srs20_position = {"_id":186, "name":"21th-Serious-Triangle","position":(503,265)}
srs21_position = {"_id":187, "name":"22th-Serious-Triangle","position":(506,263)}
srs22_position = {"_id":188, "name":"23th-Serious-Triangle","position":(613,263)}
srs23_position = {"_id":189, "name":"24th-Serious-Triangle","position":(615,265)}
srs24_position = {"_id":190, "name":"25th-Serious-Triangle","position":(283,373)}
srs25_position = {"_id":191, "name":"26th-Serious-Triangle","position":(285,375)}
srs26_position = {"_id":192, "name":"27th-Serious-Triangle","position":(393,375)}
srs27_position = {"_id":193, "name":"28th-Serious-Triangle","position":(396,373)}
srs28_position = {"_id":194, "name":"29th-Serious-Triangle","position":(503,373)}
srs29_position = {"_id":195, "name":"30th-Serious-Triangle","position":(505,375)}
srs30_position = {"_id":196, "name":"31th-Serious-Triangle","position":(613,375)}
srs31_position = {"_id":197, "name":"32th-Serious-Triangle","position":(616,373)}
sqr0_position = {"_id":198, "name":"1st-Square","position":(202,102)}
sqr1_position = {"_id":199, "name":"2nd-Square","position":(302,102)}
sqr2_position = {"_id":200, "name":"3rd-Square","position":(402,102)}
sqr3_position = {"_id":201, "name":"4th-Square","position":(502,102)}
sqr4_position = {"_id":202, "name":"5th-Square","position":(602,102)}
sqr5_position = {"_id":203, "name":"6th-Square","position":(702,102)}
sqr6_position = {"_id":204, "name":"7th-Square","position":(202,202)}
sqr7_position = {"_id":205, "name":"8th-Square","position":(302,202)}
sqr8_position = {"_id":206, "name":"9th-Square","position":(402,202)}
sqr9_position = {"_id":207, "name":"10th-Square","position":(502,202)}
sqr10_position = {"_id":208, "name":"11th-Square","position":(602,202)}
sqr11_position = {"_id":209, "name":"12th-Square","position":(702,202)}
sqr12_position = {"_id":210, "name":"13th-Square","position":(202,302)}
sqr13_position = {"_id":211, "name":"14th-Square","position":(302,302)}
sqr14_position = {"_id":212, "name":"15th-Square","position":(402,302)}
sqr15_position = {"_id":213, "name":"16th-Square","position":(502,302)}
sqr16_position = {"_id":214, "name":"17th-Square","position":(602,302)}
sqr17_position = {"_id":215, "name":"18th-Square","position":(702,302)}
sqr18_position = {"_id":216, "name":"19th-Square","position":(202,402)}
sqr19_position = {"_id":217, "name":"20th-Square","position":(302,402)}
sqr20_position = {"_id":218, "name":"21th-Square","position":(402,402)}
sqr21_position = {"_id":219, "name":"22th-Square","position":(502,402)}
sqr22_position = {"_id":220, "name":"23th-Square","position":(602,402)}
sqr23_position = {"_id":221, "name":"24th-Square","position":(702,402)}
sqr24_position = {"_id":222, "name":"25th-Square","position":(202,502)}
sqr25_position = {"_id":223, "name":"26th-Square","position":(302,502)}
sqr26_position = {"_id":224, "name":"27th-Square","position":(402,502)}
sqr27_position = {"_id":225, "name":"28th-Square","position":(502,502)}
sqr28_position = {"_id":226, "name":"29th-Square","position":(602,502)}
sqr29_position = {"_id":227, "name":"30th-Square","position":(702,502)}
sqr30_position = {"_id":228, "name":"31th-Square","position":(202,602)}
sqr31_position = {"_id":229, "name":"32th-Square","position":(302,602)}
sqr32_position = {"_id":230, "name":"33th-Square","position":(402,602)}
sqr33_position = {"_id":231, "name":"34th-Square","position":(502,602)}
sqr34_position = {"_id":232, "name":"35th-Square","position":(602,602)}
sqr35_position = {"_id":233, "name":"36th-Square","position":(702,602)}
stad0_position = {"_id":234, "name":"1st-Stadium-Piece","position":(195,82)}
stad1_position = {"_id":235, "name":"2nd-Stadium-Piece","position":(323,82)}
stad2_position = {"_id":236, "name":"3rd-Stadium-Piece","position":(413,82)}
stad3_position = {"_id":237, "name":"4th-Stadium-Piece","position":(503,82)}
stad4_position = {"_id":238, "name":"5th-Stadium-Piece","position":(593,82)}
stad5_position = {"_id":239, "name":"6th-Stadium-Piece","position":(683,82)}
stad6_position = {"_id":240, "name":"7th-Stadium-Piece","position":(142,135)}
stad7_position = {"_id":241, "name":"8th-Stadium-Piece","position":(232,198)}
stad8_position = {"_id":242, "name":"9th-Stadium-Piece","position":(258,172)}
stad9_position = {"_id":243, "name":"10th-Stadium-Piece","position":(323,172)}
stad10_position = {"_id":244, "name":"11th-Stadium-Piece","position":(413,172)}
stad11_position = {"_id":245, "name":"12th-Stadium-Piece","position":(503,172)}
stad12_position = {"_id":246, "name":"13th-Stadium-Piece","position":(593,172)}
stad13_position = {"_id":247, "name":"14th-Stadium-Piece","position":(683,172)}
stad14_position = {"_id":248, "name":"15th-Stadium-Piece","position":(685,200)}
stad15_position = {"_id":249, "name":"16th-Stadium-Piece","position":(745,136)}
stad16_position = {"_id":250, "name":"17th-Stadium-Piece","position":(142,262)}
stad17_position = {"_id":251, "name":"18th-Stadium-Piece","position":(232,262)}
stad18_position = {"_id":252, "name":"19th-Stadium-Piece","position":(258,264)}
stad19_position = {"_id":253, "name":"20th-Stadium-Piece","position":(323,262)}
stad20_position = {"_id":254, "name":"21th-Stadium-Piece","position":(413,262)}
stad21_position = {"_id":255, "name":"22th-Stadium-Piece","position":(503,262)}
stad22_position = {"_id":256, "name":"23th-Stadium-Piece","position":(593,262)}
stad23_position = {"_id":257, "name":"24th-Stadium-Piece","position":(682,264)}
stad24_position = {"_id":258, "name":"25th-Stadium-Piece","position":(684,262)}
stad25_position = {"_id":259, "name":"26th-Stadium-Piece","position":(745,262)}
stad26_position = {"_id":260, "name":"27th-Stadium-Piece","position":(194,327)}
stad27_position = {"_id":261, "name":"28th-Stadium-Piece","position":(323,353)}
stad28_position = {"_id":262, "name":"29th-Stadium-Piece","position":(413,353)}
stad29_position = {"_id":263, "name":"30th-Stadium-Piece","position":(503,353)}
stad30_position = {"_id":264, "name":"31th-Stadium-Piece","position":(593,353)}
stad31_position = {"_id":265, "name":"32th-Stadium-Piece","position":(683,325)}
kybrd0_position = {"_id":266, "name":"1st-Keyboard-Key","position":(52,52)}
kybrd1_position = {"_id":267, "name":"2nd-Keyboard-Key","position":(152,52)}
kybrd2_position = {"_id":268, "name":"3rd-Keyboard-Key","position":(202,52)}
kybrd3_position = {"_id":269, "name":"4th-Keyboard-Key","position":(252,52)}
kybrd4_position = {"_id":270, "name":"5th-Keyboard-Key","position":(302,52)}
kybrd5_position = {"_id":271, "name":"6th-Keyboard-Key","position":(380,52)}
kybrd6_position = {"_id":272, "name":"7th-Keyboard-Key","position":(430,52)}
kybrd7_position = {"_id":273, "name":"8th-Keyboard-Key","position":(480,52)}
kybrd8_position = {"_id":274, "name":"9th-Keyboard-Key","position":(530,52)}
kybrd9_position = {"_id":275, "name":"10th-Keyboard-Key","position":(609,52)}
kybrd10_position = {"_id":276, "name":"11th-Keyboard-Key","position":(659,52)}
kybrd11_position = {"_id":277, "name":"12th-Keyboard-Key","position":(709,52)}
kybrd12_position = {"_id":278, "name":"13th-Keyboard-Key","position":(759,52)}
kybrd13_position = {"_id":279, "name":"14th-Keyboard-Key","position":(837,52)}
kybrd14_position = {"_id":280, "name":"15th-Keyboard-Key","position":(887,52)}
kybrd15_position = {"_id":281, "name":"16th-Keyboard-Key","position":(937,52)}
kybrd16_position = {"_id":282, "name":"17th-Keyboard-Key","position":(52,152)}
kybrd17_position = {"_id":283, "name":"18th-Keyboard-Key","position":(102,152)}
kybrd18_position = {"_id":284, "name":"19th-Keyboard-Key","position":(152,152)}
kybrd19_position = {"_id":285, "name":"20th-Keyboard-Key","position":(202,152)}
kybrd20_position = {"_id":286, "name":"21th-Keyboard-Key","position":(252,152)}
kybrd21_position = {"_id":287, "name":"22th-Keyboard-Key","position":(302,152)}
kybrd22_position = {"_id":288, "name":"23th-Keyboard-Key","position":(352,152)}
kybrd23_position = {"_id":289, "name":"24th-Keyboard-Key","position":(402,152)}
kybrd24_position = {"_id":290, "name":"25th-Keyboard-Key","position":(452,152)}
kybrd25_position = {"_id":291, "name":"26th-Keyboard-Key","position":(502,152)}
kybrd26_position = {"_id":292, "name":"27th-Keyboard-Key","position":(552,152)}
kybrd27_position = {"_id":293, "name":"28th-Keyboard-Key","position":(602,152)}
kybrd28_position = {"_id":294, "name":"29th-Keyboard-Key","position":(652,152)}
kybrd29_position = {"_id":295, "name":"30th-Keyboard-Key","position":(702,152)}
kybrd30_position = {"_id":296, "name":"31th-Keyboard-Key","position":(837,152)}
kybrd31_position = {"_id":297, "name":"32th-Keyboard-Key","position":(887,152)}
kybrd32_position = {"_id":298, "name":"33th-Keyboard-Key","position":(937,152)}
kybrd33_position = {"_id":299, "name":"34th-Keyboard-Key","position":(1016,152)}
kybrd34_position = {"_id":300, "name":"35th-Keyboard-Key","position":(1066,152)}
kybrd35_position = {"_id":301, "name":"36th-Keyboard-Key","position":(1116,152)}
kybrd36_position = {"_id":302, "name":"37th-Keyboard-Key","position":(1166,152)}
kybrd37_position = {"_id":303, "name":"38th-Keyboard-Key","position":(52,202)}
kybrd38_position = {"_id":304, "name":"39th-Keyboard-Key","position":(127,202)}
kybrd39_position = {"_id":305, "name":"40th-Keyboard-Key","position":(177,202)}
kybrd40_position = {"_id":306, "name":"41th-Keyboard-Key","position":(227,202)}
kybrd41_position = {"_id":307, "name":"42th-Keyboard-Key","position":(277,202)}
kybrd42_position = {"_id":308, "name":"43th-Keyboard-Key","position":(327,202)}
kybrd43_position = {"_id":309, "name":"44th-Keyboard-Key","position":(377,202)}
kybrd44_position = {"_id":310, "name":"45th-Keyboard-Key","position":(427,202)}
kybrd45_position = {"_id":311, "name":"46th-Keyboard-Key","position":(477,202)}
kybrd46_position = {"_id":312, "name":"47th-Keyboard-Key","position":(527,202)}
kybrd47_position = {"_id":313, "name":"48th-Keyboard-Key","position":(577,202)}
kybrd48_position = {"_id":314, "name":"49th-Keyboard-Key","position":(627,202)}
kybrd49_position = {"_id":315, "name":"50th-Keyboard-Key","position":(677,202)}
kybrd50_position = {"_id":316, "name":"51th-Keyboard-Key","position":(727,202)}
kybrd51_position = {"_id":317, "name":"52th-Keyboard-Key","position":(837,202)}
kybrd52_position = {"_id":318, "name":"53th-Keyboard-Key","position":(887,202)}
kybrd53_position = {"_id":319, "name":"54th-Keyboard-Key","position":(937,202)}
kybrd54_position = {"_id":320, "name":"55th-Keyboard-Key","position":(1016,202)}
kybrd55_position = {"_id":321, "name":"56th-Keyboard-Key","position":(1066,202)}
kybrd56_position = {"_id":322, "name":"57th-Keyboard-Key","position":(1116,202)}
kybrd57_position = {"_id":323, "name":"58th-Keyboard-Key","position":(1166,202)}
kybrd58_position = {"_id":324, "name":"59th-Keyboard-Key","position":(52,252)}
kybrd59_position = {"_id":325, "name":"60th-Keyboard-Key","position":(137,252)}
kybrd60_position = {"_id":326, "name":"61th-Keyboard-Key","position":(187,252)}
kybrd61_position = {"_id":327, "name":"62th-Keyboard-Key","position":(237,252)}
kybrd62_position = {"_id":328, "name":"63th-Keyboard-Key","position":(287,252)}
kybrd63_position = {"_id":329, "name":"64th-Keyboard-Key","position":(337,252)}
kybrd64_position = {"_id":330, "name":"65th-Keyboard-Key","position":(387,252)}
kybrd65_position = {"_id":331, "name":"66th-Keyboard-Key","position":(437,252)}
kybrd66_position = {"_id":332, "name":"67th-Keyboard-Key","position":(487,252)}
kybrd67_position = {"_id":333, "name":"68th-Keyboard-Key","position":(537,252)}
kybrd68_position = {"_id":334, "name":"69th-Keyboard-Key","position":(587,252)}
kybrd69_position = {"_id":335, "name":"70th-Keyboard-Key","position":(637,252)}
kybrd70_position = {"_id":336, "name":"71th-Keyboard-Key","position":(687,252)}
kybrd71_position = {"_id":337, "name":"72th-Keyboard-Key","position":(1016,252)}
kybrd72_position = {"_id":338, "name":"73th-Keyboard-Key","position":(1066,252)}
kybrd73_position = {"_id":339, "name":"74th-Keyboard-Key","position":(1116,252)}
kybrd74_position = {"_id":340, "name":"75th-Keyboard-Key","position":(52,302)}
kybrd75_position = {"_id":341, "name":"76th-Keyboard-Key","position":(102,302)}
kybrd76_position = {"_id":342, "name":"77th-Keyboard-Key","position":(152,302)}
kybrd77_position = {"_id":343, "name":"78th-Keyboard-Key","position":(202,302)}
kybrd78_position = {"_id":344, "name":"79th-Keyboard-Key","position":(252,302)}
kybrd79_position = {"_id":345, "name":"80th-Keyboard-Key","position":(302,302)}
kybrd80_position = {"_id":346, "name":"81th-Keyboard-Key","position":(352,302)}
kybrd81_position = {"_id":347, "name":"82th-Keyboard-Key","position":(402,302)}
kybrd82_position = {"_id":348, "name":"83th-Keyboard-Key","position":(452,302)}
kybrd83_position = {"_id":349, "name":"84th-Keyboard-Key","position":(502,302)}
kybrd84_position = {"_id":350, "name":"85th-Keyboard-Key","position":(552,302)}
kybrd85_position = {"_id":351, "name":"86th-Keyboard-Key","position":(602,302)}
kybrd86_position = {"_id":352, "name":"87th-Keyboard-Key","position":(652,302)}
kybrd87_position = {"_id":353, "name":"88th-Keyboard-Key","position":(887,302)}
kybrd88_position = {"_id":354, "name":"89th-Keyboard-Key","position":(1016,302)}
kybrd89_position = {"_id":355, "name":"90th-Keyboard-Key","position":(1066,302)}
kybrd90_position = {"_id":356, "name":"91th-Keyboard-Key","position":(1116,302)}
kybrd91_position = {"_id":357, "name":"92th-Keyboard-Key","position":(1166,302)}
kybrd92_position = {"_id":358, "name":"93th-Keyboard-Key","position":(52,352)}
kybrd93_position = {"_id":359, "name":"94th-Keyboard-Key","position":(112,352)}
kybrd94_position = {"_id":360, "name":"95th-Keyboard-Key","position":(172,352)}
kybrd95_position = {"_id":361, "name":"96th-Keyboard-Key","position":(232,352)}
kybrd96_position = {"_id":362, "name":"97th-Keyboard-Key","position":(552,352)}
kybrd97_position = {"_id":363, "name":"98th-Keyboard-Key","position":(612,352)}
kybrd98_position = {"_id":364, "name":"99th-Keyboard-Key","position":(672,352)}
kybrd99_position = {"_id":365, "name":"100th-Keyboard-Key","position":(732,352)}
kybrd100_position = {"_id":366, "name":"101th-Keyboard-Key","position":(837,352)}
kybrd101_position = {"_id":367, "name":"102th-Keyboard-Key","position":(887,352)}
kybrd102_position = {"_id":368, "name":"103th-Keyboard-Key","position":(937,352)}
kybrd103_position = {"_id":369, "name":"104th-Keyboard-Key","position":(1016,352)}
kybrd104_position = {"_id":370, "name":"105th-Keyboard-Key","position":(1116,352)}

collection.insert_one(alaska_position)
collection.insert_one(north_west_territory_position)
collection.insert_one(alberta_position)
collection.insert_one(ontario_position)
collection.insert_one(quebec_position)
collection.insert_one(western_united_states_position)
collection.insert_one(eastern_united_states_position)
collection.insert_one(greenland_position)
collection.insert_one(mexico_position)
collection.insert_one(venezuela_position)
collection.insert_one(peru_position)
collection.insert_one(argentina_position)
collection.insert_one(brazil_position)
collection.insert_one(iceland_position)
collection.insert_one(scandinavia_position)
collection.insert_one(great_britain_position)
collection.insert_one(western_europe_position)
collection.insert_one(northern_europe_position)
collection.insert_one(southern_europe_position)
collection.insert_one(ukraine_position)
collection.insert_one(north_africa_position)
collection.insert_one(egypt_position)
collection.insert_one(sudan_position)
collection.insert_one(congo_position)
collection.insert_one(south_africa_position)
collection.insert_one(madagascar_position)
collection.insert_one(middle_east_position)
collection.insert_one(india_position)
collection.insert_one(siam_position)
collection.insert_one(china_position)
collection.insert_one(central_asia_position)
collection.insert_one(ural_position)
collection.insert_one(siberia_position)
collection.insert_one(yakutsk_position)
collection.insert_one(irkutsk_position)
collection.insert_one(kamtchatka_position)
collection.insert_one(mongolia_position)
collection.insert_one(japan_position)
collection.insert_one(indonesia_position)
collection.insert_one(papau_new_guinea_position)
collection.insert_one(western_australia_position)
collection.insert_one(eastern_australia_position)
collection.insert_one(hex0_position)
collection.insert_one(hex1_position)
collection.insert_one(hex2_position)
collection.insert_one(hex3_position)
collection.insert_one(hex4_position)
collection.insert_one(hex5_position)
collection.insert_one(hex6_position)
collection.insert_one(hex7_position)
collection.insert_one(hex8_position)
collection.insert_one(hex9_position)
collection.insert_one(hex10_position)
collection.insert_one(hex11_position)
collection.insert_one(hex12_position)
collection.insert_one(hex13_position)
collection.insert_one(hex14_position)
collection.insert_one(hex15_position)
collection.insert_one(hex16_position)
collection.insert_one(hex17_position)
collection.insert_one(hex18_position)
collection.insert_one(hex19_position)
collection.insert_one(hex20_position)
collection.insert_one(hex21_position)
collection.insert_one(hex22_position)
collection.insert_one(hex23_position)
collection.insert_one(hex24_position)
collection.insert_one(hex25_position)
collection.insert_one(hex26_position)
collection.insert_one(hex27_position)
collection.insert_one(hex28_position)
collection.insert_one(hex29_position)
collection.insert_one(hex30_position)
collection.insert_one(hex31_position)
collection.insert_one(hex32_position)
collection.insert_one(hex33_position)
collection.insert_one(hex34_position)
collection.insert_one(hex35_position)
collection.insert_one(hex36_position)
collection.insert_one(hex37_position)
collection.insert_one(hex38_position)
collection.insert_one(hex39_position)
collection.insert_one(hex40_position)
collection.insert_one(hex41_position)
collection.insert_one(hex42_position)
collection.insert_one(hex43_position)
collection.insert_one(hex44_position)
collection.insert_one(hex45_position)
collection.insert_one(hex46_position)
collection.insert_one(hex47_position)
collection.insert_one(hex48_position)
collection.insert_one(hex49_position)
collection.insert_one(hex50_position)
collection.insert_one(hex51_position)
collection.insert_one(hex52_position)
collection.insert_one(hex53_position)
collection.insert_one(hex54_position)
collection.insert_one(hex55_position)
collection.insert_one(pyr0_position)
collection.insert_one(pyr1_position)
collection.insert_one(pyr2_position)
collection.insert_one(pyr3_position)
collection.insert_one(pyr4_position)
collection.insert_one(pyr5_position)
collection.insert_one(pyr6_position)
collection.insert_one(pyr7_position)
collection.insert_one(pyr8_position)
collection.insert_one(pyr9_position)
collection.insert_one(pyr10_position)
collection.insert_one(pyr11_position)
collection.insert_one(pyr12_position)
collection.insert_one(pyr13_position)
collection.insert_one(pyr14_position)
collection.insert_one(pyr15_position)
collection.insert_one(pyr16_position)
collection.insert_one(pyr17_position)
collection.insert_one(pyr18_position)
collection.insert_one(pyr19_position)
collection.insert_one(pyr20_position)
collection.insert_one(pyr21_position)
collection.insert_one(pyr22_position)
collection.insert_one(pyr23_position)
collection.insert_one(pyr24_position)
collection.insert_one(pyr25_position)
collection.insert_one(pyr26_position)
collection.insert_one(pyr27_position)
collection.insert_one(pyr28_position)
collection.insert_one(pyr29_position)
collection.insert_one(pyr30_position)
collection.insert_one(pyr31_position)
collection.insert_one(pyr32_position)
collection.insert_one(pyr33_position)
collection.insert_one(pyr34_position)
collection.insert_one(pyr35_position)
collection.insert_one(pyr36_position)
collection.insert_one(pyr37_position)
collection.insert_one(pyr38_position)
collection.insert_one(pyr39_position)
collection.insert_one(pyr40_position)
collection.insert_one(pyr41_position)
collection.insert_one(pyr42_position)
collection.insert_one(pyr43_position)
collection.insert_one(pyr44_position)
collection.insert_one(pyr45_position)
collection.insert_one(pyr46_position)
collection.insert_one(pyr47_position)
collection.insert_one(pyr48_position)
collection.insert_one(pyr49_position)
collection.insert_one(pyr50_position)
collection.insert_one(pyr51_position)
collection.insert_one(pyr52_position)
collection.insert_one(pyr53_position)
collection.insert_one(pyr54_position)
collection.insert_one(pyr55_position)
collection.insert_one(pyr56_position)
collection.insert_one(pyr57_position)
collection.insert_one(pyr58_position)
collection.insert_one(pyr59_position)
collection.insert_one(pyr60_position)
collection.insert_one(pyr61_position)
collection.insert_one(pyr62_position)
collection.insert_one(pyr63_position)
collection.insert_one(qck0_position)
collection.insert_one(qck1_position)
collection.insert_one(qck2_position)
collection.insert_one(qck3_position)
collection.insert_one(srs0_position)
collection.insert_one(srs1_position)
collection.insert_one(srs2_position)
collection.insert_one(srs3_position)
collection.insert_one(srs4_position)
collection.insert_one(srs5_position)
collection.insert_one(srs6_position)
collection.insert_one(srs7_position)
collection.insert_one(srs8_position)
collection.insert_one(srs9_position)
collection.insert_one(srs10_position)
collection.insert_one(srs11_position)
collection.insert_one(srs12_position)
collection.insert_one(srs13_position)
collection.insert_one(srs14_position)
collection.insert_one(srs15_position)
collection.insert_one(srs16_position)
collection.insert_one(srs17_position)
collection.insert_one(srs18_position)
collection.insert_one(srs19_position)
collection.insert_one(srs20_position)
collection.insert_one(srs21_position)
collection.insert_one(srs22_position)
collection.insert_one(srs23_position)
collection.insert_one(srs24_position)
collection.insert_one(srs25_position)
collection.insert_one(srs26_position)
collection.insert_one(srs27_position)
collection.insert_one(srs28_position)
collection.insert_one(srs29_position)
collection.insert_one(srs30_position)
collection.insert_one(srs31_position)
collection.insert_one(sqr0_position)
collection.insert_one(sqr1_position)
collection.insert_one(sqr2_position)
collection.insert_one(sqr3_position)
collection.insert_one(sqr4_position)
collection.insert_one(sqr5_position)
collection.insert_one(sqr6_position)
collection.insert_one(sqr7_position)
collection.insert_one(sqr8_position)
collection.insert_one(sqr9_position)
collection.insert_one(sqr10_position)
collection.insert_one(sqr11_position)
collection.insert_one(sqr12_position)
collection.insert_one(sqr13_position)
collection.insert_one(sqr14_position)
collection.insert_one(sqr15_position)
collection.insert_one(sqr16_position)
collection.insert_one(sqr17_position)
collection.insert_one(sqr18_position)
collection.insert_one(sqr19_position)
collection.insert_one(sqr20_position)
collection.insert_one(sqr21_position)
collection.insert_one(sqr22_position)
collection.insert_one(sqr23_position)
collection.insert_one(sqr24_position)
collection.insert_one(sqr25_position)
collection.insert_one(sqr26_position)
collection.insert_one(sqr27_position)
collection.insert_one(sqr28_position)
collection.insert_one(sqr29_position)
collection.insert_one(sqr30_position)
collection.insert_one(sqr31_position)
collection.insert_one(sqr32_position)
collection.insert_one(sqr33_position)
collection.insert_one(sqr34_position)
collection.insert_one(sqr35_position)
collection.insert_one(stad0_position)
collection.insert_one(stad1_position)
collection.insert_one(stad2_position)
collection.insert_one(stad3_position)
collection.insert_one(stad4_position)
collection.insert_one(stad5_position)
collection.insert_one(stad6_position)
collection.insert_one(stad7_position)
collection.insert_one(stad8_position)
collection.insert_one(stad9_position)
collection.insert_one(stad10_position)
collection.insert_one(stad11_position)
collection.insert_one(stad12_position)
collection.insert_one(stad13_position)
collection.insert_one(stad14_position)
collection.insert_one(stad15_position)
collection.insert_one(stad16_position)
collection.insert_one(stad17_position)
collection.insert_one(stad18_position)
collection.insert_one(stad19_position)
collection.insert_one(stad20_position)
collection.insert_one(stad21_position)
collection.insert_one(stad22_position)
collection.insert_one(stad23_position)
collection.insert_one(stad24_position)
collection.insert_one(stad25_position)
collection.insert_one(stad26_position)
collection.insert_one(stad27_position)
collection.insert_one(stad28_position)
collection.insert_one(stad29_position)
collection.insert_one(stad30_position)
collection.insert_one(stad31_position)
collection.insert_one(kybrd0_position)
collection.insert_one(kybrd1_position)
collection.insert_one(kybrd2_position)
collection.insert_one(kybrd3_position)
collection.insert_one(kybrd4_position)
collection.insert_one(kybrd5_position)
collection.insert_one(kybrd6_position)
collection.insert_one(kybrd7_position)
collection.insert_one(kybrd8_position)
collection.insert_one(kybrd9_position)
collection.insert_one(kybrd10_position)
collection.insert_one(kybrd11_position)
collection.insert_one(kybrd12_position)
collection.insert_one(kybrd13_position)
collection.insert_one(kybrd14_position)
collection.insert_one(kybrd15_position)
collection.insert_one(kybrd16_position)
collection.insert_one(kybrd17_position)
collection.insert_one(kybrd18_position)
collection.insert_one(kybrd19_position)
collection.insert_one(kybrd20_position)
collection.insert_one(kybrd21_position)
collection.insert_one(kybrd22_position)
collection.insert_one(kybrd23_position)
collection.insert_one(kybrd24_position)
collection.insert_one(kybrd25_position)
collection.insert_one(kybrd26_position)
collection.insert_one(kybrd27_position)
collection.insert_one(kybrd28_position)
collection.insert_one(kybrd29_position)
collection.insert_one(kybrd30_position)
collection.insert_one(kybrd31_position)
collection.insert_one(kybrd32_position)
collection.insert_one(kybrd33_position)
collection.insert_one(kybrd34_position)
collection.insert_one(kybrd35_position)
collection.insert_one(kybrd36_position)
collection.insert_one(kybrd37_position)
collection.insert_one(kybrd38_position)
collection.insert_one(kybrd39_position)
collection.insert_one(kybrd40_position)
collection.insert_one(kybrd41_position)
collection.insert_one(kybrd42_position)
collection.insert_one(kybrd43_position)
collection.insert_one(kybrd44_position)
collection.insert_one(kybrd45_position)
collection.insert_one(kybrd46_position)
collection.insert_one(kybrd47_position)
collection.insert_one(kybrd48_position)
collection.insert_one(kybrd49_position)
collection.insert_one(kybrd50_position)
collection.insert_one(kybrd51_position)
collection.insert_one(kybrd52_position)
collection.insert_one(kybrd53_position)
collection.insert_one(kybrd54_position)
collection.insert_one(kybrd55_position)
collection.insert_one(kybrd56_position)
collection.insert_one(kybrd57_position)
collection.insert_one(kybrd58_position)
collection.insert_one(kybrd59_position)
collection.insert_one(kybrd60_position)
collection.insert_one(kybrd61_position)
collection.insert_one(kybrd62_position)
collection.insert_one(kybrd63_position)
collection.insert_one(kybrd64_position)
collection.insert_one(kybrd65_position)
collection.insert_one(kybrd66_position)
collection.insert_one(kybrd67_position)
collection.insert_one(kybrd68_position)
collection.insert_one(kybrd69_position)
collection.insert_one(kybrd70_position)
collection.insert_one(kybrd71_position)
collection.insert_one(kybrd72_position)
collection.insert_one(kybrd73_position)
collection.insert_one(kybrd74_position)
collection.insert_one(kybrd75_position)
collection.insert_one(kybrd76_position)
collection.insert_one(kybrd77_position)
collection.insert_one(kybrd78_position)
collection.insert_one(kybrd79_position)
collection.insert_one(kybrd80_position)
collection.insert_one(kybrd81_position)
collection.insert_one(kybrd82_position)
collection.insert_one(kybrd83_position)
collection.insert_one(kybrd84_position)
collection.insert_one(kybrd85_position)
collection.insert_one(kybrd86_position)
collection.insert_one(kybrd87_position)
collection.insert_one(kybrd88_position)
collection.insert_one(kybrd89_position)
collection.insert_one(kybrd90_position)
collection.insert_one(kybrd91_position)
collection.insert_one(kybrd92_position)
collection.insert_one(kybrd93_position)
collection.insert_one(kybrd94_position)
collection.insert_one(kybrd95_position)
collection.insert_one(kybrd96_position)
collection.insert_one(kybrd97_position)
collection.insert_one(kybrd98_position)
collection.insert_one(kybrd99_position)
collection.insert_one(kybrd100_position)
collection.insert_one(kybrd101_position)
collection.insert_one(kybrd102_position)
collection.insert_one(kybrd103_position)
collection.insert_one(kybrd104_position)
