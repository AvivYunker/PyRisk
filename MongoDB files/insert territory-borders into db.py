import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_borders"]

# COUNTRIES BORDERS
# alaska_borders ~ eastern_australia_borders
alaska_borders = {"_id":0,"name":"Alaska","borders":(1,2,35)} #V
north_west_territory_borders = {"_id":1,"name":"North-West-Territory","borders":(0,2,3,7)} #V
alberta_borders = {"_id":2,"name":"Alberta","borders":(0,1,3,5)} #V
ontario_borders = {"_id":3,"name":"Ontario","borders":(1,2,4,5,6,7)} #V
quebec_borders = {"_id":4,"name":"Quebec","borders":(3,6,7)} #V
western_united_states_borders = {"_id":5,"name":"Western-United-States","borders":(2,3,6,8)} #V
eastern_united_states_borders = {"_id":6,"name":"Eastern-United-States","borders":(3,4,5,8)} #V
greenland_borders = {"_id":7,"name":"Greenland","borders":(1,3,4,13)} #V
mexico_borders = {"_id":8,"name":"Mexico","borders":(5,6,9)} #V
venezuela_borders = {"_id":9,"name":"Venezuela","borders":(8,10,12)} #V
peru_borders = {"_id":10,"name":"Peru","borders":(9,11,12)} #V
argentina_borders = {"_id":11,"name":"Argentina","borders":(10,12)} #V
brazil_borders = {"_id":12,"name":"Brazil","borders":(9,10,11,20)} #V
iceland_borders = {"_id":13,"name":"Iceland","borders":(7,14,15)} #V
scandinavia_borders = {"_id":14,"name":"Scandinavia","borders":(13,15,17,19)} #V
great_britain_borders = {"_id":15,"name":"Great-Britain","borders":(13,14,16,17)} #V
western_europe_borders = {"_id":16,"name":"Western-Europe","borders":(15,17,18,20)} #V
northern_europe_borders = {"_id":17,"name":"Northern-Europe","borders":(14,15,16,18,19)} #V
southern_europe_borders = {"_id":18,"name":"Southern-Europe","borders":(16,17,19,20,21,26)} #V
ukraine_borders = {"_id":19,"name":"Ukraine","borders":(14,17,18,26,30,31)} #V
north_africa_borders = {"_id":20,"name":"North-Africa","borders":(12,16,18,21,22,23)} #V
egypt_borders = {"_id":21,"name":"Egypt","borders":(18,20,22,26)} #V
sudan_borders = {"_id":22,"name":"Sudan","borders":(20,21,23,24,25,26)} #V
congo_borders = {"_id":23,"name":"Congo","borders":(20,22,24)} #V
south_africa_borders = {"_id":24,"name":"South-Africa","borders":(22,23,25)} #V
madagascar_borders = {"_id":25,"name":"Madagascar","borders":(22,24)} #V
middle_east_borders = {"_id":26,"name":"Middle-East","borders":(18,19,21,22,27,30)} #V
india_borders = {"_id":27,"name":"India","borders":(26,28,29,30)} #V
siam_borders = {"_id":28,"name":"Siam","borders":(27,29,38)} #V
china_borders = {"_id":29,"name":"China","borders":(27,28,30,31,32,36)} #V
central_asia_borders = {"_id":30,"name":"Central-Asia","borders":(19,26,27,29,31)} #V
ural_borders = {"_id":31,"name":"Ural","borders":(19,29,30,32)} #V
siberia_borders = {"_id":32,"name":"Siberia","borders":(29,31,33,34,36)} #v
yakutsk_borders = {"_id":33,"name":"Yakutsk","borders":(32,34,35)} #V
irkutsk_borders = {"_id":34,"name":"Irkutsk","borders":(32,33,35,36)} #V
kamtchatka_borders = {"_id":35,"name":"Kamtchatka","borders":(0,33,34,36,37)} #V
mongolia_borders = {"_id":36,"name":"Mongolia","borders":(29,32,34,35,37)} #V
japan_borders = {"_id":37,"name":"Japan","borders":(35,36)} #V
indonesia_borders = {"_id":38,"name":"Indonesia","borders":(28,39,40)} #V
papau_new_guinea_borders = {"_id":39,"name":"Papau-New-Guinea","borders":(38,40,41)} #V
western_australia_borders = {"_id":40,"name":"Western-Australia","borders":(38,39,41)} #V
eastern_australia_borders = {"_id":41,"name":"Eastern-Astralia","borders":(39,40)} #V

# HEXAGONS BORDERS
# hex1_borders ~ hex56_borders
hex0_borders = {"_id":42,"name":"1st-Hexagon","borders":(43,56)} #V
hex1_borders = {"_id":43,"name":"2nd-Hexagon","borders":(42,44,56,57,58)} #V
hex2_borders = {"_id":44,"name":"3rd-Hexagon","borders":(43,45,58)} #V
hex3_borders = {"_id":45,"name":"4th-Hexagon","borders":(44,46,58,59,60)} #V
hex4_borders = {"_id":46,"name":"5th-Hexagon","borders":(45,47,60)} #V
hex5_borders = {"_id":47,"name":"6th-Hexagon","borders":(46,48,60,61,62)} #V
hex6_borders = {"_id":48,"name":"7th-Hexagon","borders":(47,49,62)} #V
hex7_borders = {"_id":49,"name":"8th-Hexagon","borders":(48,50,62,63,64)} #V
hex8_borders = {"_id":50,"name":"9th-Hexagon","borders":(49,51,64)} #V
hex9_borders = {"_id":51,"name":"10th-Hexagon","borders":(50,52,64,65,66)} #V
hex10_borders = {"_id":52,"name":"11th-Hexagon","borders":(51,53,66)} #V
hex11_borders = {"_id":53,"name":"12th-Hexagon","borders":(52,54,66,67,68)} #V
hex12_borders = {"_id":54,"name":"13th-Hexagon","borders":(53,55,68)} #V
hex13_borders = {"_id":55,"name":"14th-Hexagon","borders":(54,68,69)} #V
hex14_borders = {"_id":56,"name":"15th-Hexagon","borders":(42,43,57,70)} #V
hex15_borders = {"_id":57,"name":"16th-Hexagon","borders":(43,56,58,70,71,72)} #V
hex16_borders = {"_id":58,"name":"17th-Hexagon","borders":(43,44,45,57,59,72)} #V
hex17_borders = {"_id":59,"name":"18th-Hexagon","borders":(45,58,60,72,73,74)} #V
hex18_borders = {"_id":60,"name":"19th-Hexagon","borders":(45,46,47,59,61,74)} #V
hex19_borders = {"_id":61,"name":"20th-Hexagon","borders":(47,60,62,74,75,76)} #V
hex20_borders = {"_id":62,"name":"21th-Hexagon","borders":(47,48,49,61,63,76)} #V
hex21_borders = {"_id":63,"name":"22th-Hexagon","borders":(49,62,64,76,77,78)} #V
hex22_borders = {"_id":64,"name":"23th-Hexagon","borders":(49,50,51,63,65,78)} #V
hex23_borders = {"_id":65,"name":"24th-Hexagon","borders":(51,64,66,78,79,80)} #V
hex24_borders = {"_id":66,"name":"25th-Hexagon","borders":(51,52,53,65,67,80)} #V
hex25_borders = {"_id":67,"name":"26th-Hexagon","borders":(53,66,68,80,81,82)} #V
hex26_borders = {"_id":68,"name":"27th-Hexagon","borders":(53,54,55,67,69,82)} #V
hex27_borders = {"_id":69,"name":"28th-Hexagon","borders":(55,68,82,83)} #V
hex28_borders = {"_id":70,"name":"29th-Hexagon","borders":(56,57,71,84)} #V
hex29_borders = {"_id":71,"name":"30th-Hexagon","borders":(57,70,72,84,85,86)} #V
hex30_borders = {"_id":72,"name":"31th-Hexagon","borders":(57,58,59,71,73,86)} #V
hex31_borders = {"_id":73,"name":"32th-Hexagon","borders":(59,72,74,86,87,88)} #V
hex32_borders = {"_id":74,"name":"33th-Hexagon","borders":(59,60,61,73,75,88)} #V
hex33_borders = {"_id":75,"name":"34th-Hexagon","borders":(61,74,76,88,89,90)} #V
hex34_borders = {"_id":76,"name":"35th-Hexagon","borders":(61,62,63,75,77,90)} #V
hex35_borders = {"_id":77,"name":"36th-Hexagon","borders":(63,76,78,90,91,92)} #V
hex36_borders = {"_id":78,"name":"37th-Hexagon","borders":(63,64,65,77,79,92)} #V
hex37_borders = {"_id":79,"name":"38th-Hexagon","borders":(65,78,80,92,93,94)} #V
hex38_borders = {"_id":80,"name":"39th-Hexagon","borders":(65,66,67,79,81,94)} #V
hex39_borders = {"_id":81,"name":"40th-Hexagon","borders":(67,80,82,94,95,96)} #V
hex40_borders = {"_id":82,"name":"41th-Hexagon","borders":(67,68,69,81,83,96)} #V
hex41_borders = {"_id":83,"name":"42th-Hexagon","borders":(69,82,96,97)} #V
hex42_borders = {"_id":84,"name":"43th-Hexagon","borders":(70,71,85)} #V
hex43_borders = {"_id":85,"name":"44th-Hexagon","borders":(71,84,86)} #V
hex44_borders = {"_id":86,"name":"45th-Hexagon","borders":(71,72,73,85,87)} #V
hex45_borders = {"_id":87,"name":"46th-Hexagon","borders":(73,86,88)} #V
hex46_borders = {"_id":88,"name":"47th-Hexagon","borders":(73,74,75,87,89)} #V
hex47_borders = {"_id":89,"name":"48th-Hexagon","borders":(75,88,90)} #V
hex48_borders = {"_id":90,"name":"49th-Hexagon","borders":(75,76,77,89,91)} #V
hex49_borders = {"_id":91,"name":"50th-Hexagon","borders":(77,90,92)} #V
hex50_borders = {"_id":92,"name":"51th-Hexagon","borders":(77,78,79,91,93)} #V
hex51_borders = {"_id":93,"name":"52th-Hexagon","borders":(79,92,94)} #V
hex52_borders = {"_id":94,"name":"53th-Hexagon","borders":(79,80,81,93,95)} #V
hex53_borders = {"_id":95,"name":"54th-Hexagon","borders":(81,94,96)} #V
hex54_borders = {"_id":96,"name":"55th-Hexagon","borders":(81,82,83,95,97)} #V
hex55_borders = {"_id":97,"name":"56th-Hexagon","borders":(83,96)} #V


# PYRAMID BORDERS
# pyr1_borders ~ pyr64_borders
pyr0_borders = {"_id":98, "name":"1st-Pyramid-Triangle","borders":(100)} #V
pyr1_borders = {"_id":99, "name":"2nd-Pyramid-Triangle","borders":(100,103)} #V
pyr2_borders = {"_id":100, "name":"3rd-Pyramid-Triangle","borders":(98,99,101)} #V
pyr3_borders = {"_id":101, "name":"4th-Pyramid-Triangle","borders":(100,105)} #V
pyr4_borders = {"_id":102, "name":"5th-Pyramid-Triangle","borders":(103,108)} #V
pyr5_borders = {"_id":103, "name":"6th-Pyramid-Triangle","borders":(99,102,104)} #V
pyr6_borders = {"_id":104, "name":"7th-Pyramid-Triangle","borders":(103,105,110)} #V
pyr7_borders = {"_id":105, "name":"8th-Pyramid-Triangle","borders":(101,104,106)} #V
pyr8_borders = {"_id":106, "name":"9th-Pyramid-Triangle","borders":(105,112)} #V
pyr9_borders = {"_id":107, "name":"10th-Pyramid-Triangle","borders":(108,115)} #V
pyr10_borders = {"_id":108, "name":"11th-Pyramid-Triangle","borders":(102,107,109)} #V
pyr11_borders = {"_id":109, "name":"12th-Pyramid-Triangle","borders":(108,110,117)} #V
pyr12_borders = {"_id":110, "name":"13th-Pyramid-Triangle","borders":(104,109,111)} #V
pyr13_borders = {"_id":111, "name":"14th-Pyramid-Triangle","borders":(110,112,119)} #V
pyr14_borders = {"_id":112, "name":"15th-Pyramid-Triangle","borders":(106,111,113)} #V
pyr15_borders = {"_id":113, "name":"16th-Pyramid-Triangle","borders":(112,121)} #V
pyr16_borders = {"_id":114, "name":"17th-Pyramid-Triangle","borders":(115,124)} #V
pyr17_borders = {"_id":115, "name":"18th-Pyramid-Triangle","borders":(107,114,116)} #V
pyr18_borders = {"_id":116, "name":"19th-Pyramid-Triangle","borders":(115,117,126)} #V
pyr19_borders = {"_id":117, "name":"20th-Pyramid-Triangle","borders":(109,116,118)} #V
pyr20_borders = {"_id":118, "name":"21th-Pyramid-Triangle","borders":(117,119,128)} #V
pyr21_borders = {"_id":119, "name":"22th-Pyramid-Triangle","borders":(111,118,120)} #V
pyr22_borders = {"_id":120, "name":"23th-Pyramid-Triangle","borders":(119,121,130)} #V
pyr23_borders = {"_id":121, "name":"24th-Pyramid-Triangle","borders":(113,120,122)} #V
pyr24_borders = {"_id":122, "name":"25th-Pyramid-Triangle","borders":(121,132)} #V
pyr25_borders = {"_id":123, "name":"26th-Pyramid-Triangle","borders":(124,135)} #V
pyr26_borders = {"_id":124, "name":"27th-Pyramid-Triangle","borders":(114,123,125)} #V
pyr27_borders = {"_id":125, "name":"28th-Pyramid-Triangle","borders":(124,126,137)} #V
pyr28_borders = {"_id":126, "name":"29th-Pyramid-Triangle","borders":(116,125,127)} #V
pyr29_borders = {"_id":127, "name":"30th-Pyramid-Triangle","borders":(126,128,139)} #V
pyr30_borders = {"_id":128, "name":"31th-Pyramid-Triangle","borders":(118,127,129)} #V
pyr31_borders = {"_id":129, "name":"32th-Pyramid-Triangle","borders":(128,130,141)} #V
pyr32_borders = {"_id":130, "name":"33th-Pyramid-Triangle","borders":(120,129,131)} #V
pyr33_borders = {"_id":131, "name":"34th-Pyramid-Triangle","borders":(130,132,143)} #V
pyr34_borders = {"_id":132, "name":"35th-Pyramid-Triangle","borders":(122,131,133)} #V
pyr35_borders = {"_id":133, "name":"36th-Pyramid-Triangle","borders":(132,145)} #V
pyr36_borders = {"_id":134, "name":"37th-Pyramid-Triangle","borders":(135,148)} #V
pyr37_borders = {"_id":135, "name":"38th-Pyramid-Triangle","borders":(123,134,136)} #V
pyr38_borders = {"_id":136, "name":"39th-Pyramid-Triangle","borders":(135,137,150)} #V
pyr39_borders = {"_id":137, "name":"40th-Pyramid-Triangle","borders":(125,136,138)} #V
pyr40_borders = {"_id":138, "name":"41th-Pyramid-Triangle","borders":(137,139,152)} #V
pyr41_borders = {"_id":139, "name":"42th-Pyramid-Triangle","borders":(127,138,140)} #V
pyr42_borders = {"_id":140, "name":"43th-Pyramid-Triangle","borders":(139,141,154)} #V
pyr43_borders = {"_id":141, "name":"44th-Pyramid-Triangle","borders":(129,140,142)} #V
pyr44_borders = {"_id":142, "name":"45th-Pyramid-Triangle","borders":(141,143,156)} #V
pyr45_borders = {"_id":143, "name":"46th-Pyramid-Triangle","borders":(131,142,144)} #V
pyr46_borders = {"_id":144, "name":"47th-Pyramid-Triangle","borders":(143,145,158)} #V
pyr47_borders = {"_id":145, "name":"48th-Pyramid-Triangle","borders":(133,144,146)} #V
pyr48_borders = {"_id":146, "name":"49th-Pyramid-Triangle","borders":(145,160)} #V
pyr49_borders = {"_id":147, "name":"50th-Pyramid-Triangle","borders":(148)} #V
pyr50_borders = {"_id":148, "name":"51th-Pyramid-Triangle","borders":(134,147,149)} #V
pyr51_borders = {"_id":149, "name":"52th-Pyramid-Triangle","borders":(148,150)} #V
pyr52_borders = {"_id":150, "name":"53th-Pyramid-Triangle","borders":(136,149,151)} #V
pyr53_borders = {"_id":151, "name":"54th-Pyramid-Triangle","borders":(150,152)} #V
pyr54_borders = {"_id":152, "name":"55th-Pyramid-Triangle","borders":(138,151,153)} #V
pyr55_borders = {"_id":153, "name":"56th-Pyramid-Triangle","borders":(152,154)} #V
pyr56_borders = {"_id":154, "name":"57th-Pyramid-Triangle","borders":(140,153,155)} #V
pyr57_borders = {"_id":155, "name":"58th-Pyramid-Triangle","borders":(154,156)} #V
pyr58_borders = {"_id":156, "name":"59th-Pyramid-Triangle","borders":(142,155,157)} #V
pyr59_borders = {"_id":157, "name":"60th-Pyramid-Triangle","borders":(156,158)} #V
pyr60_borders = {"_id":158, "name":"61th-Pyramid-Triangle","borders":(144,157,159)} #V
pyr61_borders = {"_id":159, "name":"62th-Pyramid-Triangle","borders":(158,160)} #V
pyr62_borders = {"_id":160, "name":"63th-Pyramid-Triangle","borders":(146,159,161)} #V
pyr63_borders = {"_id":161, "name":"64th-Pyramid-Triangle","borders":(160)} #V

# QUICK-TRIANGLES BORDERS
# qck1_borders ~ qck4_borders
qck0_borders = {"_id":162,"name":"1st-Quick-Triangle","borders":(163,164)} #V
qck1_borders = {"_id":163,"name":"2nd-Quick-Triangle","borders":(162,165)} #V
qck2_borders = {"_id":164,"name":"3rd-Quick-Triangle","borders":(162,165)} #V
qck3_borders = {"_id":165,"name":"4th-Quick-Triangle","borders":(163,164)} #V

# SERIOUS-TRIANGLES BORDERS
# srs1_borders ~ srs32_borders
srs0_borders = {"_id":166, "name":"1st-Serious-Triangle","borders":(167,174)} #V
srs1_borders = {"_id":167, "name":"2nd-Serious-Triangle","borders":(166,168)} #V
srs2_borders = {"_id":168, "name":"3rd-Serious-Triangle","borders":(167,169)} #V
srs3_borders = {"_id":169, "name":"4th-Serious-Triangle","borders":(168,170,177)} #V
srs4_borders = {"_id":170, "name":"5th-Serious-Triangle","borders":(169,171,178)} #V
srs5_borders = {"_id":171, "name":"6th-Serious-Triangle","borders":(170,172)} #V
srs6_borders = {"_id":172, "name":"7th-Serious-Triangle","borders":(171,173)} #V
srs7_borders = {"_id":173, "name":"8th-Serious-Triangle","borders":(172,181)} #V
srs8_borders = {"_id":174, "name":"9th-Serious-Triangle","borders":(166,175)} #V
srs9_borders = {"_id":175, "name":"10th-Serious-Triangle","borders":(174,176,183)} #V
srs10_borders = {"_id":176, "name":"11th-Serious-Triangle","borders":(175,177,184)} #V
srs11_borders = {"_id":177, "name":"12th-Serious-Triangle","borders":(169,176,178)} #V
srs12_borders = {"_id":178, "name":"13th-Serious-Triangle","borders":(170,177,179)} #V
srs13_borders = {"_id":179, "name":"14th-Serious-Triangle","borders":(178,180,187)} #V
srs14_borders = {"_id":180, "name":"15th-Serious-Triangle","borders":(179,181,188)} #V
srs15_borders = {"_id":181, "name":"16th-Serious-Triangle","borders":(173,180)} #V
srs16_borders = {"_id":182, "name":"17th-Serious-Triangle","borders":(183,190)} #V
srs17_borders = {"_id":183, "name":"18th-Serious-Triangle","borders":(175,182,184)} #V
srs18_borders = {"_id":184, "name":"19th-Serious-Triangle","borders":(176,183,185)} #V
srs19_borders = {"_id":185, "name":"20th-Serious-Triangle","borders":(184,186,193)} #V
srs20_borders = {"_id":186, "name":"21th-Serious-Triangle","borders":(185,187,194)} #V
srs21_borders = {"_id":187, "name":"22th-Serious-Triangle","borders":(179,186,188)} #V
srs22_borders = {"_id":188, "name":"23th-Serious-Triangle","borders":(180,187,189)} #V
srs23_borders = {"_id":189, "name":"24th-Serious-Triangle","borders":(188,197)} #V
srs24_borders = {"_id":190, "name":"25th-Serious-Triangle","borders":(182,191)} #V
srs25_borders = {"_id":191, "name":"26th-Serious-Triangle","borders":(190,192)} #V
srs26_borders = {"_id":192, "name":"27th-Serious-Triangle","borders":(191,193)} #V
srs27_borders = {"_id":193, "name":"28th-Serious-Triangle","borders":(185,192,194)} #V
srs28_borders = {"_id":194, "name":"29th-Serious-Triangle","borders":(186,193,195)} #V
srs29_borders = {"_id":195, "name":"30th-Serious-Triangle","borders":(194,196)} #V
srs30_borders = {"_id":196, "name":"31th-Serious-Triangle","borders":(195,197)} #V
srs31_borders = {"_id":197, "name":"32th-Serious-Triangle","borders":(189,196)} #V

# SQUARES BORDERS
# sqr1_borders ~ sqr36_borders
sqr0_borders = {"_id":198, "name":"1st-Square","borders":(199,204)} #V
sqr1_borders = {"_id":199, "name":"2nd-Square","borders":(198,200,205)} #V
sqr2_borders = {"_id":200, "name":"3rd-Square","borders":(199,201,206)} #V
sqr3_borders = {"_id":201, "name":"4th-Square","borders":(200,202,207)} #V
sqr4_borders = {"_id":202, "name":"5th-Square","borders":(201,203,208)} #V
sqr5_borders = {"_id":203, "name":"6th-Square","borders":(202,209)} #V
sqr6_borders = {"_id":204, "name":"7th-Square","borders":(198,205,210)} #V
sqr7_borders = {"_id":205, "name":"8th-Square","borders":(199,204,206,211)} #V
sqr8_borders = {"_id":206, "name":"9th-Square","borders":(200,205,207,212)} #V
sqr9_borders = {"_id":207, "name":"10th-Square","borders":(201,206,208,213)} #V
sqr10_borders = {"_id":208, "name":"11th-Square","borders":(202,207,209,214)} #V
sqr11_borders = {"_id":209, "name":"12th-Square","borders":(203,208,215)} #V
sqr12_borders = {"_id":210, "name":"13th-Square","borders":(204,211,216)} #V
sqr13_borders = {"_id":211, "name":"14th-Square","borders":(205,210,212,217)} #V
sqr14_borders = {"_id":212, "name":"15th-Square","borders":(206,211,213,218)} #V
sqr15_borders = {"_id":213, "name":"16th-Square","borders":(207,212,214,219)} #V
sqr16_borders = {"_id":214, "name":"17th-Square","borders":(208,213,215,220)} #V
sqr17_borders = {"_id":215, "name":"18th-Square","borders":(209,214,221)} #V
sqr18_borders = {"_id":216, "name":"19th-Square","borders":(210,217,222)} #V
sqr19_borders = {"_id":217, "name":"20th-Square","borders":(211,216,218,223)} #V
sqr20_borders = {"_id":218, "name":"21th-Square","borders":(212,217,219,224)} #V
sqr21_borders = {"_id":219, "name":"22th-Square","borders":(213,218,220,225)} #V
sqr22_borders = {"_id":220, "name":"23th-Square","borders":(214,219,221,226)} #V
sqr23_borders = {"_id":221, "name":"24th-Square","borders":(215,220,227)} #V
sqr24_borders = {"_id":222, "name":"25th-Square","borders":(216,223,228)} #V
sqr25_borders = {"_id":223, "name":"26th-Square","borders":(217,222,224,229)} #V
sqr26_borders = {"_id":224, "name":"27th-Square","borders":(218,223,225,230)} #V
sqr27_borders = {"_id":225, "name":"28th-Square","borders":(219,224,226,231)} #V
sqr28_borders = {"_id":226, "name":"29th-Square","borders":(220,225,227,232)} #V
sqr29_borders = {"_id":227, "name":"30th-Square","borders":(221,226,233)} #V
sqr30_borders = {"_id":228, "name":"31th-Square","borders":(222,229)} #V
sqr31_borders = {"_id":229, "name":"32th-Square","borders":(223,228,230)} #V
sqr32_borders = {"_id":230, "name":"33th-Square","borders":(224,229,231)} #V
sqr33_borders = {"_id":231, "name":"34th-Square","borders":(225,230,232)} #V
sqr34_borders = {"_id":232, "name":"35th-Square","borders":(226,231,233)} #V
sqr35_borders = {"_id":233, "name":"36th-Square","borders":(227,232)} #V

# STADIUM BORDERS
# stad1_borders ~ stad32_borders
stad0_borders = {"_id":234, "name":"1st-Stadium-Piece","borders":(235,240,242)} #V
stad1_borders = {"_id":235, "name":"2nd-Stadium-Piece","borders":(234,236,243)} #V
stad2_borders = {"_id":236, "name":"3rd-Stadium-Piece","borders":(235,237,244)} #V
stad3_borders = {"_id":237, "name":"4th-Stadium-Piece","borders":(236,238,245)} #V
stad4_borders = {"_id":238, "name":"5th-Stadium-Piece","borders":(237,239,246)} #V
stad5_borders = {"_id":239, "name":"6th-Stadium-Piece","borders":(238,247,249)} #V
stad6_borders = {"_id":240, "name":"7th-Stadium-Piece","borders":(234,241,250)} #V
stad7_borders = {"_id":241, "name":"8th-Stadium-Piece","borders":(240,242,251)} #V
stad8_borders = {"_id":242, "name":"9th-Stadium-Piece","borders":(234,241,243)} #V
stad9_borders = {"_id":243, "name":"10th-Stadium-Piece","borders":(235,242,244,253)} #V
stad10_borders = {"_id":244, "name":"11th-Stadium-Piece","borders":(236,243,245,254)} #V
stad11_borders = {"_id":245, "name":"12th-Stadium-Piece","borders":(237,244,246,255)} #V
stad12_borders = {"_id":246, "name":"13th-Stadium-Piece","borders":(238,245,247,256)} #V
stad13_borders = {"_id":247, "name":"14th-Stadium-Piece","borders":(239,246,248)} #V
stad14_borders = {"_id":248, "name":"15th-Stadium-Piece","borders":(247,249,258)} #V
stad15_borders = {"_id":249, "name":"16th-Stadium-Piece","borders":(239,248,259)} #V
stad16_borders = {"_id":250, "name":"17th-Stadium-Piece","borders":(240,251,260)} #V
stad17_borders = {"_id":251, "name":"18th-Stadium-Piece","borders":(241,250,252)} #V
stad18_borders = {"_id":252, "name":"19th-Stadium-Piece","borders":(251,253,260)} #V
stad19_borders = {"_id":253, "name":"20th-Stadium-Piece","borders":(243,252,254,261)} #V
stad20_borders = {"_id":254, "name":"21th-Stadium-Piece","borders":(244,253,255,262)} #V
stad21_borders = {"_id":255, "name":"22th-Stadium-Piece","borders":(245,254,256,263)} #V
stad22_borders = {"_id":256, "name":"23th-Stadium-Piece","borders":(246,255,257,264)} #V
stad23_borders = {"_id":257, "name":"24th-Stadium-Piece","borders":(256,258,265)} #V
stad24_borders = {"_id":258, "name":"25th-Stadium-Piece","borders":(248,257,259)} #V
stad25_borders = {"_id":259, "name":"26th-Stadium-Piece","borders":(249,258,265)} #V
stad26_borders = {"_id":260, "name":"27th-Stadium-Piece","borders":(250,252,261)} #V
stad27_borders = {"_id":261, "name":"28th-Stadium-Piece","borders":(253,260,262)} #V
stad28_borders = {"_id":262, "name":"29th-Stadium-Piece","borders":(254,261,263)} #V
stad29_borders = {"_id":263, "name":"30th-Stadium-Piece","borders":(255,262,264)} #V
stad30_borders = {"_id":264, "name":"31th-Stadium-Piece","borders":(256,263,265)} #V
stad31_borders = {"_id":265, "name":"32th-Stadium-Piece","borders":(257,259,264)} #V

# KEYBOARD BORDERS
# ...
# kybrd1 ~ kybrd105
# _id:266 ~ _id:370
kybrd0_borders = {"_id":266, "name":"Esc Key","borders":(267,282)} #V
kybrd1_borders = {"_id":267, "name":"F1 Key","borders":(266,268,284)} #V
kybrd2_borders = {"_id":268, "name":"F2 Key","borders":(267,269)} #V
kybrd3_borders = {"_id":269, "name":"F3 Key","borders":(268,270)} #V
kybrd4_borders = {"_id":270, "name":"F4 Key","borders":(269,271,287)} #V
kybrd5_borders = {"_id":271, "name":"F5 Key","borders":(270,272,289)} #V
kybrd6_borders = {"_id":272, "name":"F6 Key","borders":(271,273)} #V
kybrd7_borders = {"_id":273, "name":"F7 Key","borders":(272,274)} #V
kybrd8_borders = {"_id":274, "name":"F8 Key","borders":(273,275,292)} #V
kybrd9_borders = {"_id":275, "name":"F9 Key","borders":(274,276,293)} #V
kybrd10_borders = {"_id":276, "name":"F10 Key","borders":(275,277)} #V
kybrd11_borders = {"_id":277, "name":"F11 Key","borders":(276,278)} #V
kybrd12_borders = {"_id":278, "name":"F12 Key","borders":(277,279,295)} #V
kybrd13_borders = {"_id":279, "name":"Print-Screen Key","borders":(278,296,280)} #V
kybrd14_borders = {"_id":280, "name":"Scroll-Lock Key","borders":(279,281)} #V
kybrd15_borders = {"_id":281, "name":"Pause-Break Key","borders":(280,298)} #V
kybrd16_borders = {"_id":282, "name":"~ Key","borders":(266,283,302)} #V
kybrd17_borders = {"_id":283, "name":"1 Key","borders":(282,284,303,304)} #V
kybrd18_borders = {"_id":284, "name":"2 Key","borders":(267,283,285,304,305)} #V
kybrd19_borders = {"_id":285, "name":"3 Key","borders":(284,286,305,306)} #V
kybrd20_borders = {"_id":286, "name":"4 Key","borders":(285,287,306,307)} #V
kybrd21_borders = {"_id":287, "name":"5 Key","borders":(270,286,288,307,308)} #V
kybrd22_borders = {"_id":288, "name":"6 Key","borders":(287,289,308,309)} #V
kybrd23_borders = {"_id":289, "name":"7 Key","borders":(271,288,290,309,310)} #V
kybrd24_borders = {"_id":290, "name":"8 Key","borders":(289,291,310,311)} #V
kybrd25_borders = {"_id":291, "name":"9 Key","borders":(290,292,311,312)} #V
kybrd26_borders = {"_id":292, "name":"0 Key","borders":(274,291,293,312,313)} #V
kybrd27_borders = {"_id":293, "name":"_ Key","borders":(275,292,294,313,314)} #V
kybrd28_borders = {"_id":294, "name":"= Key","borders":(293,295,314,315)} #V
kybrd29_borders = {"_id":295, "name":"Backspace Key","borders":(278,294,296,315,316)} #V
kybrd30_borders = {"_id":296, "name":"Insert Key","borders":(279,295,297,317)} #V
kybrd31_borders = {"_id":297, "name":"Home Key","borders":(296,298,318)} #V
kybrd32_borders = {"_id":298, "name":"Page-Up Key","borders":(281,297,299,319)} #V
kybrd33_borders = {"_id":299, "name":"Num-Lock Key","borders":(298,300,320)} #V
kybrd34_borders = {"_id":300, "name":"/ Key","borders":(299,301,321)} #V
kybrd35_borders = {"_id":301, "name":"* Key","borders":(300,302,322)} #V
kybrd36_borders = {"_id":302, "name":"- Key","borders":(282,301,323)} #V
kybrd37_borders = {"_id":303, "name":"Tab Key","borders":(282,283,304,324)} #V
kybrd38_borders = {"_id":304, "name":"Q Key","borders":(283,284,303,305,324,325)} #V
kybrd39_borders = {"_id":305, "name":"W Key","borders":(284,285,304,306,325,326)} #V
kybrd40_borders = {"_id":306, "name":"E Key","borders":(285,286,305,307,326,327)} #V
kybrd41_borders = {"_id":307, "name":"R Key","borders":(286,287,306,308,327,328)} #V
kybrd42_borders = {"_id":308, "name":"T Key","borders":(287,288,307,309,328,329)} #V
kybrd43_borders = {"_id":309, "name":"Y Key","borders":(288,289,308,310,329,330)} #V
kybrd44_borders = {"_id":310, "name":"U Key","borders":(289,290,390,311,330,331)} #V
kybrd45_borders = {"_id":311, "name":"I Key","borders":(290,291,310,312,331,332)} #V
kybrd46_borders = {"_id":312, "name":"O Key","borders":(291,292,311,313,332,333)} #V
kybrd47_borders = {"_id":313, "name":"P Key","borders":(292,293,312,314,333,334)} #V
kybrd48_borders = {"_id":314, "name":"{ Key","borders":(293,294,313,315,334,335)} #V
kybrd49_borders = {"_id":315, "name":"} Key","borders":(294,295,314,316,335,336)} #V
kybrd50_borders = {"_id":316, "name":"| Key","borders":(295,315,336,352)} #V
kybrd51_borders = {"_id":317, "name":"Delete Key","borders":(296,318)} #V
kybrd52_borders = {"_id":318, "name":"End Key","borders":(297,317,319,353)} #V
kybrd53_borders = {"_id":319, "name":"Page-Down Key","borders":(298,318)} #V
kybrd54_borders = {"_id":320, "name":"7-Pad Key","borders":(299,321,337)} #V
kybrd55_borders = {"_id":321, "name":"8-Pad Key","borders":(300,320,322,338)} #V
kybrd56_borders = {"_id":322, "name":"9-Pad Key","borders":(301,321,323,339)} #V
kybrd57_borders = {"_id":323, "name":"+-Pad Key","borders":(302,322,339,357)} #V
kybrd58_borders = {"_id":324, "name":"Caps-Lock Key","borders":(303,304,325,340,341)} #V
kybrd59_borders = {"_id":325, "name":"A Key","borders":(304,305,324,326,341,342)} #V
kybrd60_borders = {"_id":326, "name":"S Key","borders":(305,306,325,327,342,343)} #V
kybrd61_borders = {"_id":327, "name":"D Key","borders":(306,307,326,328,343,344)} #V
kybrd62_borders = {"_id":328, "name":"F Key","borders":(307,308,327,329,344,345)} #V
kybrd63_borders = {"_id":329, "name":"G Key","borders":(308,309,328,330,345,346)} #V
kybrd64_borders = {"_id":330, "name":"H Key","borders":(309,310,329,331,346,347)} #V
kybrd65_borders = {"_id":331, "name":"J Key","borders":(310,311,330,332,347,348)} #V
kybrd66_borders = {"_id":332, "name":"K Key","borders":(311,312,331,333,348,349)} #V
kybrd67_borders = {"_id":333, "name":"L Key","borders":(312,313,332,334,349,350)} #V
kybrd68_borders = {"_id":334, "name":"[ Key","borders":(313,314,333,335,350,351)} #V
kybrd69_borders = {"_id":335, "name":"] Key","borders":(314,315,334,336,351,352)} #
kybrd70_borders = {"_id":336, "name":", Key","borders":(315,316,335,352)} #V
kybrd71_borders = {"_id":337, "name":"4-Pad Key","borders":(320,338,354)} #V
kybrd72_borders = {"_id":338, "name":"5-Pad Key","borders":(321,337,339,355)} #V
kybrd73_borders = {"_id":339, "name":"6-Pad Key","borders":(322,338,323,356)} #V
kybrd74_borders = {"_id":340, "name":"Left-Shift Key","borders":(324,341,358)} #V
kybrd75_borders = {"_id":341, "name":"Z Key","borders":(324,325,340,342,358,359)} #V
kybrd76_borders = {"_id":342, "name":"X Key","borders":(325,326,341,343,359,360)} #V
kybrd77_borders = {"_id":343, "name":"C Key","borders":(326,327,342,344,360,361)} #V
kybrd78_borders = {"_id":344, "name":"V Key","borders":(327,328,343,345,361)} #V
kybrd79_borders = {"_id":345, "name":"B Key","borders":(328,329,344,346,361)} #V
kybrd80_borders = {"_id":346, "name":"N Key","borders":(329,330,345,347,361)} #V
kybrd81_borders = {"_id":347, "name":"M Key","borders":(330,331,346,348,361)} #V
kybrd82_borders = {"_id":348, "name":"< Key","borders":(331,332,347,349,361)} #V
kybrd83_borders = {"_id":349, "name":"> Key","borders":(332,333,348,350,361)} #V
kybrd84_borders = {"_id":350, "name":"? Key","borders":(333,334,349,351,362)} #V
kybrd85_borders = {"_id":351, "name":". Key","borders":(334,335,350,352,362,363)} #V
kybrd86_borders = {"_id":352, "name":"Right-Shift Key","borders":(316,335,336,351,363,364,365)} #V
kybrd87_borders = {"_id":353, "name":"Up-Arrow Key","borders":(318,367)} #V
kybrd88_borders = {"_id":354, "name":"1-Pad Key","borders":(337,355,369)} #V
kybrd89_borders = {"_id":355, "name":"2-Pad Key","borders":(338,354,356,369)} #V
kybrd90_borders = {"_id":356, "name":"3-Pad Key","borders":(339,355,357,370)} #V
kybrd91_borders = {"_id":357, "name":"Enter-Pad Key","borders":(323,356,370)} #V
kybrd92_borders = {"_id":358, "name":"Left-CTRL Key","borders":(340,341,359)} #V
kybrd93_borders = {"_id":359, "name":"Left-Win Key","borders":(341,342,358,360)} #V
kybrd94_borders = {"_id":360, "name":"Left-Alt Key","borders":(342,343,359,361)} #V
kybrd95_borders = {"_id":361, "name":"Space Key","borders":(343,344,345,346,347,348,349,360,362)} #V
kybrd96_borders = {"_id":362, "name":"Right-Alt Key","borders":(350,351,361,363)} #V
kybrd97_borders = {"_id":363, "name":"Right-Win Key","borders":(351,352,362,364)} #V
kybrd98_borders = {"_id":364, "name":"Menu Key","borders":(352,363,365)} #V
kybrd99_borders = {"_id":365, "name":"Right-CTRL Key","borders":(352,364,366)} #V
kybrd100_borders = {"_id":366, "name":"Left-Arrow Key","borders":(365,367)} #V
kybrd101_borders = {"_id":367, "name":"Down-Arrow Key","borders":(353,366,368)} #V
kybrd102_borders = {"_id":368, "name":"Right-Arrow Key","borders":(367,369)} #V
kybrd103_borders = {"_id":369, "name":"0-Pad Key","borders":(354,355,368,370)} #V
kybrd104_borders = {"_id":370, "name":"Del-Pad Key","borders":(356,357,369)} #V

collection.insert_one(alaska_borders)
collection.insert_one(north_west_territory_borders)
collection.insert_one(alberta_borders)
collection.insert_one(ontario_borders)
collection.insert_one(quebec_borders)
collection.insert_one(western_united_states_borders)
collection.insert_one(eastern_united_states_borders)
collection.insert_one(greenland_borders)
collection.insert_one(mexico_borders)
collection.insert_one(venezuela_borders)
collection.insert_one(peru_borders)
collection.insert_one(argentina_borders)
collection.insert_one(brazil_borders)
collection.insert_one(iceland_borders)
collection.insert_one(scandinavia_borders)
collection.insert_one(great_britain_borders)
collection.insert_one(western_europe_borders)
collection.insert_one(northern_europe_borders)
collection.insert_one(southern_europe_borders)
collection.insert_one(ukraine_borders)
collection.insert_one(north_africa_borders)
collection.insert_one(egypt_borders)
collection.insert_one(sudan_borders)
collection.insert_one(congo_borders)
collection.insert_one(south_africa_borders)
collection.insert_one(madagascar_borders)
collection.insert_one(middle_east_borders)
collection.insert_one(india_borders)
collection.insert_one(siam_borders)
collection.insert_one(china_borders)
collection.insert_one(central_asia_borders)
collection.insert_one(ural_borders)
collection.insert_one(siberia_borders)
collection.insert_one(yakutsk_borders)
collection.insert_one(irkutsk_borders)
collection.insert_one(kamtchatka_borders)
collection.insert_one(mongolia_borders)
collection.insert_one(japan_borders)
collection.insert_one(indonesia_borders)
collection.insert_one(papau_new_guinea_borders)
collection.insert_one(western_australia_borders)
collection.insert_one(eastern_australia_borders)
collection.insert_one(hex0_borders)
collection.insert_one(hex1_borders)
collection.insert_one(hex2_borders)
collection.insert_one(hex3_borders)
collection.insert_one(hex4_borders)
collection.insert_one(hex5_borders)
collection.insert_one(hex6_borders)
collection.insert_one(hex7_borders)
collection.insert_one(hex8_borders)
collection.insert_one(hex9_borders)
collection.insert_one(hex10_borders)
collection.insert_one(hex11_borders)
collection.insert_one(hex12_borders)
collection.insert_one(hex13_borders)
collection.insert_one(hex14_borders)
collection.insert_one(hex15_borders)
collection.insert_one(hex16_borders)
collection.insert_one(hex17_borders)
collection.insert_one(hex18_borders)
collection.insert_one(hex19_borders)
collection.insert_one(hex20_borders)
collection.insert_one(hex21_borders)
collection.insert_one(hex22_borders)
collection.insert_one(hex23_borders)
collection.insert_one(hex24_borders)
collection.insert_one(hex25_borders)
collection.insert_one(hex26_borders)
collection.insert_one(hex27_borders)
collection.insert_one(hex28_borders)
collection.insert_one(hex29_borders)
collection.insert_one(hex30_borders)
collection.insert_one(hex31_borders)
collection.insert_one(hex32_borders)
collection.insert_one(hex33_borders)
collection.insert_one(hex34_borders)
collection.insert_one(hex35_borders)
collection.insert_one(hex36_borders)
collection.insert_one(hex37_borders)
collection.insert_one(hex38_borders)
collection.insert_one(hex39_borders)
collection.insert_one(hex40_borders)
collection.insert_one(hex41_borders)
collection.insert_one(hex42_borders)
collection.insert_one(hex43_borders)
collection.insert_one(hex44_borders)
collection.insert_one(hex45_borders)
collection.insert_one(hex46_borders)
collection.insert_one(hex47_borders)
collection.insert_one(hex48_borders)
collection.insert_one(hex49_borders)
collection.insert_one(hex50_borders)
collection.insert_one(hex51_borders)
collection.insert_one(hex52_borders)
collection.insert_one(hex53_borders)
collection.insert_one(hex54_borders)
collection.insert_one(hex55_borders)
collection.insert_one(pyr0_borders)
collection.insert_one(pyr1_borders)
collection.insert_one(pyr2_borders)
collection.insert_one(pyr3_borders)
collection.insert_one(pyr4_borders)
collection.insert_one(pyr5_borders)
collection.insert_one(pyr6_borders)
collection.insert_one(pyr7_borders)
collection.insert_one(pyr8_borders)
collection.insert_one(pyr9_borders)
collection.insert_one(pyr10_borders)
collection.insert_one(pyr11_borders)
collection.insert_one(pyr12_borders)
collection.insert_one(pyr13_borders)
collection.insert_one(pyr14_borders)
collection.insert_one(pyr15_borders)
collection.insert_one(pyr16_borders)
collection.insert_one(pyr17_borders)
collection.insert_one(pyr18_borders)
collection.insert_one(pyr19_borders)
collection.insert_one(pyr20_borders)
collection.insert_one(pyr21_borders)
collection.insert_one(pyr22_borders)
collection.insert_one(pyr23_borders)
collection.insert_one(pyr24_borders)
collection.insert_one(pyr25_borders)
collection.insert_one(pyr26_borders)
collection.insert_one(pyr27_borders)
collection.insert_one(pyr28_borders)
collection.insert_one(pyr29_borders)
collection.insert_one(pyr30_borders)
collection.insert_one(pyr31_borders)
collection.insert_one(pyr32_borders)
collection.insert_one(pyr33_borders)
collection.insert_one(pyr34_borders)
collection.insert_one(pyr35_borders)
collection.insert_one(pyr36_borders)
collection.insert_one(pyr37_borders)
collection.insert_one(pyr38_borders)
collection.insert_one(pyr39_borders)
collection.insert_one(pyr40_borders)
collection.insert_one(pyr41_borders)
collection.insert_one(pyr42_borders)
collection.insert_one(pyr43_borders)
collection.insert_one(pyr44_borders)
collection.insert_one(pyr45_borders)
collection.insert_one(pyr46_borders)
collection.insert_one(pyr47_borders)
collection.insert_one(pyr48_borders)
collection.insert_one(pyr49_borders)
collection.insert_one(pyr50_borders)
collection.insert_one(pyr51_borders)
collection.insert_one(pyr52_borders)
collection.insert_one(pyr53_borders)
collection.insert_one(pyr54_borders)
collection.insert_one(pyr55_borders)
collection.insert_one(pyr56_borders)
collection.insert_one(pyr57_borders)
collection.insert_one(pyr58_borders)
collection.insert_one(pyr59_borders)
collection.insert_one(pyr60_borders)
collection.insert_one(pyr61_borders)
collection.insert_one(pyr62_borders)
collection.insert_one(pyr63_borders)
collection.insert_one(qck0_borders)
collection.insert_one(qck1_borders)
collection.insert_one(qck2_borders)
collection.insert_one(qck3_borders)
collection.insert_one(srs0_borders)
collection.insert_one(srs1_borders)
collection.insert_one(srs2_borders)
collection.insert_one(srs3_borders)
collection.insert_one(srs4_borders)
collection.insert_one(srs5_borders)
collection.insert_one(srs6_borders)
collection.insert_one(srs7_borders)
collection.insert_one(srs8_borders)
collection.insert_one(srs9_borders)
collection.insert_one(srs10_borders)
collection.insert_one(srs11_borders)
collection.insert_one(srs12_borders)
collection.insert_one(srs13_borders)
collection.insert_one(srs14_borders)
collection.insert_one(srs15_borders)
collection.insert_one(srs16_borders)
collection.insert_one(srs17_borders)
collection.insert_one(srs18_borders)
collection.insert_one(srs19_borders)
collection.insert_one(srs20_borders)
collection.insert_one(srs21_borders)
collection.insert_one(srs22_borders)
collection.insert_one(srs23_borders)
collection.insert_one(srs24_borders)
collection.insert_one(srs25_borders)
collection.insert_one(srs26_borders)
collection.insert_one(srs27_borders)
collection.insert_one(srs28_borders)
collection.insert_one(srs29_borders)
collection.insert_one(srs30_borders)
collection.insert_one(srs31_borders)
collection.insert_one(sqr0_borders)
collection.insert_one(sqr1_borders)
collection.insert_one(sqr2_borders)
collection.insert_one(sqr3_borders)
collection.insert_one(sqr4_borders)
collection.insert_one(sqr5_borders)
collection.insert_one(sqr6_borders)
collection.insert_one(sqr7_borders)
collection.insert_one(sqr8_borders)
collection.insert_one(sqr9_borders)
collection.insert_one(sqr10_borders)
collection.insert_one(sqr11_borders)
collection.insert_one(sqr12_borders)
collection.insert_one(sqr13_borders)
collection.insert_one(sqr14_borders)
collection.insert_one(sqr15_borders)
collection.insert_one(sqr16_borders)
collection.insert_one(sqr17_borders)
collection.insert_one(sqr18_borders)
collection.insert_one(sqr19_borders)
collection.insert_one(sqr20_borders)
collection.insert_one(sqr21_borders)
collection.insert_one(sqr22_borders)
collection.insert_one(sqr23_borders)
collection.insert_one(sqr24_borders)
collection.insert_one(sqr25_borders)
collection.insert_one(sqr26_borders)
collection.insert_one(sqr27_borders)
collection.insert_one(sqr28_borders)
collection.insert_one(sqr29_borders)
collection.insert_one(sqr30_borders)
collection.insert_one(sqr31_borders)
collection.insert_one(sqr32_borders)
collection.insert_one(sqr33_borders)
collection.insert_one(sqr34_borders)
collection.insert_one(sqr35_borders)
collection.insert_one(stad0_borders)
collection.insert_one(stad1_borders)
collection.insert_one(stad2_borders)
collection.insert_one(stad3_borders)
collection.insert_one(stad4_borders)
collection.insert_one(stad5_borders)
collection.insert_one(stad6_borders)
collection.insert_one(stad7_borders)
collection.insert_one(stad8_borders)
collection.insert_one(stad9_borders)
collection.insert_one(stad10_borders)
collection.insert_one(stad11_borders)
collection.insert_one(stad12_borders)
collection.insert_one(stad13_borders)
collection.insert_one(stad14_borders)
collection.insert_one(stad15_borders)
collection.insert_one(stad16_borders)
collection.insert_one(stad17_borders)
collection.insert_one(stad18_borders)
collection.insert_one(stad19_borders)
collection.insert_one(stad20_borders)
collection.insert_one(stad21_borders)
collection.insert_one(stad22_borders)
collection.insert_one(stad23_borders)
collection.insert_one(stad24_borders)
collection.insert_one(stad25_borders)
collection.insert_one(stad26_borders)
collection.insert_one(stad27_borders)
collection.insert_one(stad28_borders)
collection.insert_one(stad29_borders)
collection.insert_one(stad30_borders)
collection.insert_one(stad31_borders)
collection.insert_one(kybrd0_borders)
collection.insert_one(kybrd1_borders)
collection.insert_one(kybrd2_borders)
collection.insert_one(kybrd3_borders)
collection.insert_one(kybrd4_borders)
collection.insert_one(kybrd5_borders)
collection.insert_one(kybrd6_borders)
collection.insert_one(kybrd7_borders)
collection.insert_one(kybrd8_borders)
collection.insert_one(kybrd9_borders)
collection.insert_one(kybrd10_borders)
collection.insert_one(kybrd11_borders)
collection.insert_one(kybrd12_borders)
collection.insert_one(kybrd13_borders)
collection.insert_one(kybrd14_borders)
collection.insert_one(kybrd15_borders)
collection.insert_one(kybrd16_borders)
collection.insert_one(kybrd17_borders)
collection.insert_one(kybrd18_borders)
collection.insert_one(kybrd19_borders)
collection.insert_one(kybrd20_borders)
collection.insert_one(kybrd21_borders)
collection.insert_one(kybrd22_borders)
collection.insert_one(kybrd23_borders)
collection.insert_one(kybrd24_borders)
collection.insert_one(kybrd25_borders)
collection.insert_one(kybrd26_borders)
collection.insert_one(kybrd27_borders)
collection.insert_one(kybrd28_borders)
collection.insert_one(kybrd29_borders)
collection.insert_one(kybrd30_borders)
collection.insert_one(kybrd31_borders)
collection.insert_one(kybrd32_borders)
collection.insert_one(kybrd33_borders)
collection.insert_one(kybrd34_borders)
collection.insert_one(kybrd35_borders)
collection.insert_one(kybrd36_borders)
collection.insert_one(kybrd37_borders)
collection.insert_one(kybrd38_borders)
collection.insert_one(kybrd39_borders)
collection.insert_one(kybrd40_borders)
collection.insert_one(kybrd41_borders)
collection.insert_one(kybrd42_borders)
collection.insert_one(kybrd43_borders)
collection.insert_one(kybrd44_borders)
collection.insert_one(kybrd45_borders)
collection.insert_one(kybrd46_borders)
collection.insert_one(kybrd47_borders)
collection.insert_one(kybrd48_borders)
collection.insert_one(kybrd49_borders)
collection.insert_one(kybrd50_borders)
collection.insert_one(kybrd51_borders)
collection.insert_one(kybrd52_borders)
collection.insert_one(kybrd53_borders)
collection.insert_one(kybrd54_borders)
collection.insert_one(kybrd55_borders)
collection.insert_one(kybrd56_borders)
collection.insert_one(kybrd57_borders)
collection.insert_one(kybrd58_borders)
collection.insert_one(kybrd59_borders)
collection.insert_one(kybrd60_borders)
collection.insert_one(kybrd61_borders)
collection.insert_one(kybrd62_borders)
collection.insert_one(kybrd63_borders)
collection.insert_one(kybrd64_borders)
collection.insert_one(kybrd65_borders)
collection.insert_one(kybrd66_borders)
collection.insert_one(kybrd67_borders)
collection.insert_one(kybrd68_borders)
collection.insert_one(kybrd69_borders)
collection.insert_one(kybrd70_borders)
collection.insert_one(kybrd71_borders)
collection.insert_one(kybrd72_borders)
collection.insert_one(kybrd73_borders)
collection.insert_one(kybrd74_borders)
collection.insert_one(kybrd75_borders)
collection.insert_one(kybrd76_borders)
collection.insert_one(kybrd77_borders)
collection.insert_one(kybrd78_borders)
collection.insert_one(kybrd79_borders)
collection.insert_one(kybrd80_borders)
collection.insert_one(kybrd81_borders)
collection.insert_one(kybrd82_borders)
collection.insert_one(kybrd83_borders)
collection.insert_one(kybrd84_borders)
collection.insert_one(kybrd85_borders)
collection.insert_one(kybrd86_borders)
collection.insert_one(kybrd87_borders)
collection.insert_one(kybrd88_borders)
collection.insert_one(kybrd89_borders)
collection.insert_one(kybrd90_borders)
collection.insert_one(kybrd91_borders)
collection.insert_one(kybrd92_borders)
collection.insert_one(kybrd93_borders)
collection.insert_one(kybrd94_borders)
collection.insert_one(kybrd95_borders)
collection.insert_one(kybrd96_borders)
collection.insert_one(kybrd97_borders)
collection.insert_one(kybrd98_borders)
collection.insert_one(kybrd99_borders)
collection.insert_one(kybrd100_borders)
collection.insert_one(kybrd101_borders)
collection.insert_one(kybrd102_borders)
collection.insert_one(kybrd103_borders)
collection.insert_one(kybrd104_borders)