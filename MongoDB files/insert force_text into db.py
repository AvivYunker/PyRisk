import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_force_text"]

alaska_force_text = {"_id":0,"name":"alaska","force_text":(70,60)}
north_west_territory_force_text = {"_id":1,"name":"north_west_territory","force_text":(170,65)}
alberta_force_text = {"_id":2,"name":"alberta","force_text":(140,105)}
ontario_force_text = {"_id":3,"name":"ontario","force_text":(225,110)}
quebec_force_text = {"_id":4,"name":"quebec","force_text":(305,105)}
western_united_states_force_text = {"_id":5,"name":"western_united_states","force_text":(130,165)}
eastern_united_states_force_text = {"_id":6,"name":"eastern_united_states","force_text":(210,180)}
greenland_force_text = {"_id":7,"name":"greenland","force_text":(440,30)}
mexico_force_text = {"_id":8,"name":"mexico","force_text":(125,235)}
venezuela_force_text = {"_id":9,"name":"venezuela","force_text":(255,325)}
peru_force_text = {"_id":10,"name":"peru","force_text":(265,420)}
argentina_force_text = {"_id":11,"name":"argentina","force_text":(285,490)}
brazil_force_text = {"_id":12,"name":"brazil","force_text":(330,400)}
iceland_force_text = {"_id":13,"name":"iceland","force_text":(542,65)}
scandinavia_force_text = {"_id":14,"name":"scandinavia","force_text":(602,50)}
great_britain_force_text = {"_id":15,"name":"great_britain","force_text":(502,130)}
western_europe_force_text = {"_id":16,"name":"western_europe","force_text":(497,180)}
northern_europe_force_text = {"_id":17,"name":"northern_europe","force_text":(600,120)}
southern_europe_force_text = {"_id":18,"name":"southern_europe","force_text":(632,150)}
ukraine_force_text = {"_id":19,"name":"ukraine","force_text":(690,100)}
north_africa_force_text = {"_id":20,"name":"north_africa","force_text":(550,265)}
egypt_force_text = {"_id":21,"name":"egypt","force_text":(635,230)}
sudan_force_text = {"_id":22,"name":"sudan","force_text":(700,321)}
congo_force_text = {"_id":23,"name":"congo","force_text":(630,355)}
south_africa_force_text = {"_id":24,"name":"south_africa","force_text":(640,445)}
madagascar_force_text = {"_id":25,"name":"madagascar","force_text":(785,445)}
middle_east_force_text = {"_id":26,"name":"middle_east","force_text":(710,200)}
india_force_text = {"_id":27,"name":"india","force_text":(860,240)}
siam_force_text = {"_id":28,"name":"siam","force_text":(958,270)}
china_force_text = {"_id":29,"name":"china","force_text":(930,195)}
central_asia_force_text = {"_id":30,"name":"central_asia","force_text":(790,150)}
ural_force_text = {"_id":31,"name":"ural","force_text":(790,80)}
siberia_force_text = {"_id":32,"name":"siberia","force_text":(860,70)}
yakutsk_force_text = {"_id":33,"name":"yakutsk","force_text":(950,65)}
irkutsk_force_text = {"_id":34,"name":"irkutsk","force_text":(930,105)}
kamtchatka_force_text = {"_id":35,"name":"kamtchatka","force_text":(1075,60)}
mongolia_force_text = {"_id":36,"name":"mongolia","force_text":(945,150)}
japan_force_text = {"_id":37,"name":"japan","force_text":(1130,180)}
indonesia_force_text = {"_id":38,"name":"indonesia","force_text":(995,352)}
papau_new_guinea_force_text = {"_id":39,"name":"papau_new_guinea","force_text":(1140,352)}
western_australia_force_text = {"_id":40,"name":"western_australia","force_text":(1035,470)}
eastern_australia_force_text = {"_id":41,"name":"eastern_australia","force_text":(1100,450)}
hex0_force_text = {"_id":42,"name":"hex0","force_text":(60,84)}
hex1_force_text = {"_id":43,"name":"hex1","force_text":(139,131)}
hex2_force_text = {"_id":44,"name":"hex2","force_text":(219,84)}
hex3_force_text = {"_id":45,"name":"hex3","force_text":(298,131)}
hex4_force_text = {"_id":46,"name":"hex4","force_text":(378,84)}
hex5_force_text = {"_id":47,"name":"hex5","force_text":(457,131)}
hex6_force_text = {"_id":48,"name":"hex6","force_text":(537,84)}
hex7_force_text = {"_id":49,"name":"hex7","force_text":(616,131)}
hex8_force_text = {"_id":50,"name":"hex8","force_text":(696,84)}
hex9_force_text = {"_id":51,"name":"hex9","force_text":(775,131)}
hex10_force_text = {"_id":52,"name":"hex10","force_text":(855,84)}
hex11_force_text = {"_id":53,"name":"hex11","force_text":(934,131)}
hex12_force_text = {"_id":54,"name":"hex12","force_text":(1014,84)}
hex13_force_text = {"_id":55,"name":"hex13","force_text":(1093,131)}
hex14_force_text = {"_id":56,"name":"hex14","force_text":(60,179)}
hex15_force_text = {"_id":57,"name":"hex15","force_text":(139,226)}
hex16_force_text = {"_id":58,"name":"hex16","force_text":(219,179)}
hex17_force_text = {"_id":59,"name":"hex17","force_text":(298,226)}
hex18_force_text = {"_id":60,"name":"hex18","force_text":(378,179)}
hex19_force_text = {"_id":61,"name":"hex19","force_text":(457,226)}
hex20_force_text = {"_id":62,"name":"hex20","force_text":(537,179)}
hex21_force_text = {"_id":63,"name":"hex21","force_text":(616,226)}
hex22_force_text = {"_id":64,"name":"hex22","force_text":(696,179)}
hex23_force_text = {"_id":65,"name":"hex23","force_text":(775,226)}
hex24_force_text = {"_id":66,"name":"hex24","force_text":(855,179)}
hex25_force_text = {"_id":67,"name":"hex25","force_text":(934,226)}
hex26_force_text = {"_id":68,"name":"hex26","force_text":(1014,179)}
hex27_force_text = {"_id":69,"name":"hex27","force_text":(1093,226)}
hex28_force_text = {"_id":70,"name":"hex28","force_text":(60,274)}
hex29_force_text = {"_id":71,"name":"hex29","force_text":(139,322)}
hex30_force_text = {"_id":72,"name":"hex30","force_text":(219,274)}
hex31_force_text = {"_id":73,"name":"hex31","force_text":(298,322)}
hex32_force_text = {"_id":74,"name":"hex32","force_text":(378,274)}
hex33_force_text = {"_id":75,"name":"hex33","force_text":(457,322)}
hex34_force_text = {"_id":76,"name":"hex34","force_text":(537,274)}
hex35_force_text = {"_id":77,"name":"hex35","force_text":(616,322)}
hex36_force_text = {"_id":78,"name":"hex36","force_text":(696,274)}
hex37_force_text = {"_id":79,"name":"hex37","force_text":(775,322)}
hex38_force_text = {"_id":80,"name":"hex38","force_text":(855,274)}
hex39_force_text = {"_id":81,"name":"hex39","force_text":(934,322)}
hex40_force_text = {"_id":82,"name":"hex40","force_text":(1014,274)}
hex41_force_text = {"_id":83,"name":"hex41","force_text":(1093,322)}
hex42_force_text = {"_id":84,"name":"hex42","force_text":(60,369)}
hex43_force_text = {"_id":85,"name":"hex43","force_text":(139,417)}
hex44_force_text = {"_id":86,"name":"hex44","force_text":(219,369)}
hex45_force_text = {"_id":87,"name":"hex45","force_text":(298,417)}
hex46_force_text = {"_id":88,"name":"hex46","force_text":(378,369)}
hex47_force_text = {"_id":89,"name":"hex47","force_text":(457,417)}
hex48_force_text = {"_id":90,"name":"hex48","force_text":(537,369)}
hex49_force_text = {"_id":91,"name":"hex49","force_text":(616,417)}
hex50_force_text = {"_id":92,"name":"hex50","force_text":(696,369)}
hex51_force_text = {"_id":93,"name":"hex51","force_text":(775,417)}
hex52_force_text = {"_id":94,"name":"hex52","force_text":(855,369)}
hex53_force_text = {"_id":95,"name":"hex53","force_text":(934,417)}
hex54_force_text = {"_id":96,"name":"hex54","force_text":(1014,369)}
hex55_force_text = {"_id":97,"name":"hex55","force_text":(1093,417)}
pyr0_force_text = {"_id":98,"name":"pyr0","force_text":(485,90)}
pyr1_force_text = {"_id":99,"name":"pyr1","force_text":(455,150)}
pyr2_force_text = {"_id":100,"name":"pyr2","force_text":(485,132)}
pyr3_force_text = {"_id":101,"name":"pyr3","force_text":(515,150)}
pyr4_force_text = {"_id":102,"name":"pyr4","force_text":(425,210)}
pyr5_force_text = {"_id":103,"name":"pyr5","force_text":(455,190)}
pyr6_force_text = {"_id":104,"name":"pyr6","force_text":(485,210)}
pyr7_force_text = {"_id":105,"name":"pyr7","force_text":(515,190)}
pyr8_force_text = {"_id":106,"name":"pyr8","force_text":(545,210)}
pyr9_force_text = {"_id":107,"name":"pyr9","force_text":(395,270)}
pyr10_force_text = {"_id":108,"name":"pyr10","force_text":(425,250)}
pyr11_force_text = {"_id":109,"name":"pyr11","force_text":(455,270)}
pyr12_force_text = {"_id":110,"name":"pyr12","force_text":(485,250)}
pyr13_force_text = {"_id":111,"name":"pyr13","force_text":(515,270)}
pyr14_force_text = {"_id":112,"name":"pyr14","force_text":(545,250)}
pyr15_force_text = {"_id":113,"name":"pyr15","force_text":(575,270)}
pyr16_force_text = {"_id":114,"name":"pyr16","force_text":(365,330)}
pyr17_force_text = {"_id":115,"name":"pyr17","force_text":(395,310)}
pyr18_force_text = {"_id":116,"name":"pyr18","force_text":(425,330)}
pyr19_force_text = {"_id":117,"name":"pyr19","force_text":(455,310)}
pyr20_force_text = {"_id":118,"name":"pyr20","force_text":(485,330)}
pyr21_force_text = {"_id":119,"name":"pyr21","force_text":(515,310)}
pyr22_force_text = {"_id":120,"name":"pyr22","force_text":(545,330)}
pyr23_force_text = {"_id":121,"name":"pyr23","force_text":(575,310)}
pyr24_force_text = {"_id":122,"name":"pyr24","force_text":(605,330)}
pyr25_force_text = {"_id":123,"name":"pyr25","force_text":(335,390)}
pyr26_force_text = {"_id":124,"name":"pyr26","force_text":(365,370)}
pyr27_force_text = {"_id":125,"name":"pyr27","force_text":(395,390)}
pyr28_force_text = {"_id":126,"name":"pyr28","force_text":(425,370)}
pyr29_force_text = {"_id":127,"name":"pyr29","force_text":(455,390)}
pyr30_force_text = {"_id":128,"name":"pyr30","force_text":(485,370)}
pyr31_force_text = {"_id":129,"name":"pyr31","force_text":(515,390)}
pyr32_force_text = {"_id":130,"name":"pyr32","force_text":(545,370)}
pyr33_force_text = {"_id":131,"name":"pyr33","force_text":(575,390)}
pyr34_force_text = {"_id":132,"name":"pyr34","force_text":(605,370)}
pyr35_force_text = {"_id":133,"name":"pyr35","force_text":(635,390)}
pyr36_force_text = {"_id":134,"name":"pyr36","force_text":(305,450)}
pyr37_force_text = {"_id":135,"name":"pyr37","force_text":(335,430)}
pyr38_force_text = {"_id":136,"name":"pyr38","force_text":(365,450)}
pyr39_force_text = {"_id":137,"name":"pyr39","force_text":(395,430)}
pyr40_force_text = {"_id":138,"name":"pyr40","force_text":(425,450)}
pyr41_force_text = {"_id":139,"name":"pyr41","force_text":(455,430)}
pyr42_force_text = {"_id":140,"name":"pyr42","force_text":(485,450)}
pyr43_force_text = {"_id":141,"name":"pyr43","force_text":(515,430)}
pyr44_force_text = {"_id":142,"name":"pyr44","force_text":(545,450)}
pyr45_force_text = {"_id":143,"name":"pyr45","force_text":(575,430)}
pyr46_force_text = {"_id":144,"name":"pyr46","force_text":(605,450)}
pyr47_force_text = {"_id":145,"name":"pyr47","force_text":(635,430)}
pyr48_force_text = {"_id":146,"name":"pyr48","force_text":(665,450)}
pyr49_force_text = {"_id":147,"name":"pyr49","force_text":(275,510)}
pyr50_force_text = {"_id":148,"name":"pyr50","force_text":(305,490)}
pyr51_force_text = {"_id":149,"name":"pyr51","force_text":(335,510)}
pyr52_force_text = {"_id":150,"name":"pyr52","force_text":(365,490)}
pyr53_force_text = {"_id":151,"name":"pyr53","force_text":(395,510)}
pyr54_force_text = {"_id":152,"name":"pyr54","force_text":(425,490)}
pyr55_force_text = {"_id":153,"name":"pyr55","force_text":(455,510)}
pyr56_force_text = {"_id":154,"name":"pyr56","force_text":(485,490)}
pyr57_force_text = {"_id":155,"name":"pyr57","force_text":(515,510)}
pyr58_force_text = {"_id":156,"name":"pyr58","force_text":(545,490)}
pyr59_force_text = {"_id":157,"name":"pyr59","force_text":(575,510)}
pyr60_force_text = {"_id":158,"name":"pyr60","force_text":(605,490)}
pyr61_force_text = {"_id":159,"name":"pyr61","force_text":(635,510)}
pyr62_force_text = {"_id":160,"name":"pyr62","force_text":(665,490)}
pyr63_force_text = {"_id":161,"name":"pyr63","force_text":(695,510)}
qck0_force_text = {"_id":162,"name":"qck0","force_text":(478,150)}
qck1_force_text = {"_id":163,"name":"qck1","force_text":(395,240)}
qck2_force_text = {"_id":164,"name":"qck2","force_text":(565,240)}
qck3_force_text = {"_id":165,"name":"qck3","force_text":(478,330)}
srs0_force_text = {"_id":166,"name":"srs0","force_text":(293,110)}
srs1_force_text = {"_id":167,"name":"srs1","force_text":(348,55)}
srs2_force_text = {"_id":168,"name":"srs2","force_text":(403,55)}
srs3_force_text = {"_id":169,"name":"srs3","force_text":(458,110)}
srs4_force_text = {"_id":170,"name":"srs4","force_text":(513,110)}
srs5_force_text = {"_id":171,"name":"srs5","force_text":(568,55)}
srs6_force_text = {"_id":172,"name":"srs6","force_text":(623,55)}
srs7_force_text = {"_id":173,"name":"srs7","force_text":(678,110)}
srs8_force_text = {"_id":174,"name":"srs8","force_text":(293,165)}
srs9_force_text = {"_id":175,"name":"srs9","force_text":(348,220)}
srs10_force_text = {"_id":176,"name":"srs10","force_text":(403,220)}
srs11_force_text = {"_id":177,"name":"srs11","force_text":(458,165)}
srs12_force_text = {"_id":178,"name":"srs12","force_text":(513,165)}
srs13_force_text = {"_id":179,"name":"srs13","force_text":(568,220)}
srs14_force_text = {"_id":180,"name":"srs14","force_text":(623,220)}
srs15_force_text = {"_id":181,"name":"srs15","force_text":(678,165)}
srs16_force_text = {"_id":182,"name":"srs16","force_text":(293,330)}
srs17_force_text = {"_id":183,"name":"srs17","force_text":(348,275)}
srs18_force_text = {"_id":184,"name":"srs18","force_text":(403,275)}
srs19_force_text = {"_id":185,"name":"srs19","force_text":(458,330)}
srs20_force_text = {"_id":186,"name":"srs20","force_text":(513,330)}
srs21_force_text = {"_id":187,"name":"srs21","force_text":(568,275)}
srs22_force_text = {"_id":188,"name":"srs22","force_text":(623,275)}
srs23_force_text = {"_id":189,"name":"srs23","force_text":(678,330)}
srs24_force_text = {"_id":190,"name":"srs24","force_text":(293,385)}
srs25_force_text = {"_id":191,"name":"srs25","force_text":(348,440)}
srs26_force_text = {"_id":192,"name":"srs26","force_text":(403,440)}
srs27_force_text = {"_id":193,"name":"srs27","force_text":(458,385)}
srs28_force_text = {"_id":194,"name":"srs28","force_text":(513,385)}
srs29_force_text = {"_id":195,"name":"srs29","force_text":(568,440)}
srs30_force_text = {"_id":196,"name":"srs30","force_text":(623,440)}
srs31_force_text = {"_id":197,"name":"srs31","force_text":(678,385)}
sqr0_force_text = {"_id":198,"name":"sqr0","force_text":(240,140)}
sqr1_force_text = {"_id":199,"name":"sqr1","force_text":(340,140)}
sqr2_force_text = {"_id":200,"name":"sqr2","force_text":(440,140)}
sqr3_force_text = {"_id":201,"name":"sqr3","force_text":(540,140)}
sqr4_force_text = {"_id":202,"name":"sqr4","force_text":(640,140)}
sqr5_force_text = {"_id":203,"name":"sqr5","force_text":(740,140)}
sqr6_force_text = {"_id":204,"name":"sqr6","force_text":(240,240)}
sqr7_force_text = {"_id":205,"name":"sqr7","force_text":(340,240)}
sqr8_force_text = {"_id":206,"name":"sqr8","force_text":(440,240)}
sqr9_force_text = {"_id":207,"name":"sqr9","force_text":(540,240)}
sqr10_force_text = {"_id":208,"name":"sqr10","force_text":(640,240)}
sqr11_force_text = {"_id":209,"name":"sqr11","force_text":(740,240)}
sqr12_force_text = {"_id":210,"name":"sqr12","force_text":(240,340)}
sqr13_force_text = {"_id":211,"name":"sqr13","force_text":(340,340)}
sqr14_force_text = {"_id":212,"name":"sqr14","force_text":(440,340)}
sqr15_force_text = {"_id":213,"name":"sqr15","force_text":(540,340)}
sqr16_force_text = {"_id":214,"name":"sqr16","force_text":(640,340)}
sqr17_force_text = {"_id":215,"name":"sqr17","force_text":(740,340)}
sqr18_force_text = {"_id":216,"name":"sqr18","force_text":(240,440)}
sqr19_force_text = {"_id":217,"name":"sqr19","force_text":(340,440)}
sqr20_force_text = {"_id":218,"name":"sqr20","force_text":(440,440)}
sqr21_force_text = {"_id":219,"name":"sqr21","force_text":(540,440)}
sqr22_force_text = {"_id":220,"name":"sqr22","force_text":(640,440)}
sqr23_force_text = {"_id":221,"name":"sqr23","force_text":(740,440)}
sqr24_force_text = {"_id":222,"name":"sqr24","force_text":(240,540)}
sqr25_force_text = {"_id":223,"name":"sqr25","force_text":(340,540)}
sqr26_force_text = {"_id":224,"name":"sqr26","force_text":(440,540)}
sqr27_force_text = {"_id":225,"name":"sqr27","force_text":(540,540)}
sqr28_force_text = {"_id":226,"name":"sqr28","force_text":(640,540)}
sqr29_force_text = {"_id":227,"name":"sqr29","force_text":(740,540)}
sqr30_force_text = {"_id":228,"name":"sqr30","force_text":(240,640)}
sqr31_force_text = {"_id":229,"name":"sqr31","force_text":(340,640)}
sqr32_force_text = {"_id":230,"name":"sqr32","force_text":(440,640)}
sqr33_force_text = {"_id":231,"name":"sqr33","force_text":(540,640)}
sqr34_force_text = {"_id":232,"name":"sqr34","force_text":(640,640)}
sqr35_force_text = {"_id":233,"name":"sqr35","force_text":(740,640)}
stad0_force_text = {"_id":234,"name":"stad0","force_text":(260,120)}
stad1_force_text = {"_id":235,"name":"stad1","force_text":(355,115)}
stad2_force_text = {"_id":236,"name":"stad2","force_text":(445,115)}
stad3_force_text = {"_id":237,"name":"stad3","force_text":(535,115)}
stad4_force_text = {"_id":238,"name":"stad4","force_text":(625,115)}
stad5_force_text = {"_id":239,"name":"stad5","force_text":(720,120)}
stad6_force_text = {"_id":240,"name":"stad6","force_text":(180,190)}
stad7_force_text = {"_id":241,"name":"stad7","force_text":(250,225)}
stad8_force_text = {"_id":242,"name":"stad8","force_text":(285,200)}
stad9_force_text = {"_id":243,"name":"stad9","force_text":(355,205)}
stad10_force_text = {"_id":244,"name":"stad10","force_text":(445,205)}
stad11_force_text = {"_id":245,"name":"stad11","force_text":(535,205)}
stad12_force_text = {"_id":246,"name":"stad12","force_text":(625,205)}
stad13_force_text = {"_id":247,"name":"stad13","force_text":(690,190)}
stad14_force_text = {"_id":248,"name":"stad14","force_text":(720,225)}
stad15_force_text = {"_id":249,"name":"stad15","force_text":(790,200)}
stad16_force_text = {"_id":250,"name":"stad16","force_text":(180,300)}
stad17_force_text = {"_id":251,"name":"stad17","force_text":(250,270)}
stad18_force_text = {"_id":252,"name":"stad18","force_text":(285,300)}
stad19_force_text = {"_id":253,"name":"stad19","force_text":(355,295)}
stad20_force_text = {"_id":254,"name":"stad20","force_text":(445,295)}
stad21_force_text = {"_id":255,"name":"stad21","force_text":(535,295)}
stad22_force_text = {"_id":256,"name":"stad22","force_text":(625,295)}
stad23_force_text = {"_id":257,"name":"stad23","force_text":(690,300)}
stad24_force_text = {"_id":258,"name":"stad24","force_text":(720,270)}
stad25_force_text = {"_id":259,"name":"stad25","force_text":(785,300)}
stad26_force_text = {"_id":260,"name":"stad26","force_text":(250,375)}
stad27_force_text = {"_id":261,"name":"stad27","force_text":(355,385)}
stad28_force_text = {"_id":262,"name":"stad28","force_text":(445,385)}
stad29_force_text = {"_id":263,"name":"stad29","force_text":(535,385)}
stad30_force_text = {"_id":264,"name":"stad30","force_text":(625,385)}
stad31_force_text = {"_id":265,"name":"stad31","force_text":(720,375)}
kybrd0_force_text = {"_id":266,"name":"kybrd0","force_text":(60,60)}
kybrd1_force_text = {"_id":267,"name":"kybrd1","force_text":(160,60)}
kybrd2_force_text = {"_id":268,"name":"kybrd2","force_text":(210,60)}
kybrd3_force_text = {"_id":269,"name":"kybrd3","force_text":(260,60)}
kybrd4_force_text = {"_id":270,"name":"kybrd4","force_text":(310,60)}
kybrd5_force_text = {"_id":271,"name":"kybrd5","force_text":(388,60)}
kybrd6_force_text = {"_id":272,"name":"kybrd6","force_text":(438,60)}
kybrd7_force_text = {"_id":273,"name":"kybrd7","force_text":(488,60)}
kybrd8_force_text = {"_id":274,"name":"kybrd8","force_text":(538,60)}
kybrd9_force_text = {"_id":275,"name":"kybrd9","force_text":(617,60)}
kybrd10_force_text = {"_id":276,"name":"kybrd10","force_text":(667,60)}
kybrd11_force_text = {"_id":277,"name":"kybrd11","force_text":(717,60)}
kybrd12_force_text = {"_id":278,"name":"kybrd12","force_text":(767,60)}
kybrd13_force_text = {"_id":279,"name":"kybrd13","force_text":(845,60)}
kybrd14_force_text = {"_id":280,"name":"kybrd14","force_text":(895,60)}
kybrd15_force_text = {"_id":281,"name":"kybrd15","force_text":(945,60)}
kybrd16_force_text = {"_id":282,"name":"kybrd16","force_text":(60,160)}
kybrd17_force_text = {"_id":283,"name":"kybrd17","force_text":(110,160)}
kybrd18_force_text = {"_id":284,"name":"kybrd18","force_text":(160,160)}
kybrd19_force_text = {"_id":285,"name":"kybrd19","force_text":(210,160)}
kybrd20_force_text = {"_id":286,"name":"kybrd20","force_text":(260,160)}
kybrd21_force_text = {"_id":287,"name":"kybrd21","force_text":(310,160)}
kybrd22_force_text = {"_id":288,"name":"kybrd22","force_text":(360,160)}
kybrd23_force_text = {"_id":289,"name":"kybrd23","force_text":(410,160)}
kybrd24_force_text = {"_id":290,"name":"kybrd24","force_text":(460,160)}
kybrd25_force_text = {"_id":291,"name":"kybrd25","force_text":(510,160)}
kybrd26_force_text = {"_id":292,"name":"kybrd26","force_text":(560,160)}
kybrd27_force_text = {"_id":293,"name":"kybrd27","force_text":(610,160)}
kybrd28_force_text = {"_id":294,"name":"kybrd28","force_text":(660,160)}
kybrd29_force_text = {"_id":295,"name":"kybrd29","force_text":(739,160)}
kybrd30_force_text = {"_id":296,"name":"kybrd30","force_text":(845,160)}
kybrd31_force_text = {"_id":297,"name":"kybrd31","force_text":(895,160)}
kybrd32_force_text = {"_id":298,"name":"kybrd32","force_text":(945,160)}
kybrd33_force_text = {"_id":299,"name":"kybrd33","force_text":(1024,160)}
kybrd34_force_text = {"_id":300,"name":"kybrd34","force_text":(1074,160)}
kybrd35_force_text = {"_id":301,"name":"kybrd35","force_text":(1124,160)}
kybrd36_force_text = {"_id":302,"name":"kybrd36","force_text":(1174,160)}
kybrd37_force_text = {"_id":303,"name":"kybrd37","force_text":(75,210)}
kybrd38_force_text = {"_id":304,"name":"kybrd38","force_text":(135,210)}
kybrd39_force_text = {"_id":305,"name":"kybrd39","force_text":(185,210)}
kybrd40_force_text = {"_id":306,"name":"kybrd40","force_text":(235,210)}
kybrd41_force_text = {"_id":307,"name":"kybrd41","force_text":(285,210)}
kybrd42_force_text = {"_id":308,"name":"kybrd42","force_text":(335,210)}
kybrd43_force_text = {"_id":309,"name":"kybrd43","force_text":(385,210)}
kybrd44_force_text = {"_id":310,"name":"kybrd44","force_text":(435,210)}
kybrd45_force_text = {"_id":311,"name":"kybrd45","force_text":(485,210)}
kybrd46_force_text = {"_id":312,"name":"kybrd46","force_text":(535,210)}
kybrd47_force_text = {"_id":313,"name":"kybrd47","force_text":(585,210)}
kybrd48_force_text = {"_id":314,"name":"kybrd48","force_text":(635,210)}
kybrd49_force_text = {"_id":315,"name":"kybrd49","force_text":(685,210)}
kybrd50_force_text = {"_id":316,"name":"kybrd50","force_text":(755,230)}
kybrd51_force_text = {"_id":317,"name":"kybrd51","force_text":(845,210)}
kybrd52_force_text = {"_id":318,"name":"kybrd52","force_text":(895,210)}
kybrd53_force_text = {"_id":319,"name":"kybrd53","force_text":(945,210)}
kybrd54_force_text = {"_id":320,"name":"kybrd54","force_text":(1024,210)}
kybrd55_force_text = {"_id":321,"name":"kybrd55","force_text":(1074,210)}
kybrd56_force_text = {"_id":322,"name":"kybrd56","force_text":(1124,210)}
kybrd57_force_text = {"_id":323,"name":"kybrd57","force_text":(1174,235)}
kybrd58_force_text = {"_id":324,"name":"kybrd58","force_text":(78,260)}
kybrd59_force_text = {"_id":325,"name":"kybrd59","force_text":(145,260)}
kybrd60_force_text = {"_id":326,"name":"kybrd60","force_text":(195,260)}
kybrd61_force_text = {"_id":327,"name":"kybrd61","force_text":(245,260)}
kybrd62_force_text = {"_id":328,"name":"kybrd62","force_text":(295,260)}
kybrd63_force_text = {"_id":329,"name":"kybrd63","force_text":(345,260)}
kybrd64_force_text = {"_id":330,"name":"kybrd64","force_text":(395,260)}
kybrd65_force_text = {"_id":331,"name":"kybrd65","force_text":(445,260)}
kybrd66_force_text = {"_id":332,"name":"kybrd66","force_text":(495,260)}
kybrd67_force_text = {"_id":333,"name":"kybrd67","force_text":(545,260)}
kybrd68_force_text = {"_id":334,"name":"kybrd68","force_text":(595,260)}
kybrd69_force_text = {"_id":335,"name":"kybrd69","force_text":(645,260)}
kybrd70_force_text = {"_id":336,"name":"kybrd70","force_text":(695,260)}
kybrd71_force_text = {"_id":337,"name":"kybrd71","force_text":(1024,260)}
kybrd72_force_text = {"_id":338,"name":"kybrd72","force_text":(1074,260)}
kybrd73_force_text = {"_id":339,"name":"kybrd73","force_text":(1124,260)}
kybrd74_force_text = {"_id":340,"name":"kybrd74","force_text":(60,310)}
kybrd75_force_text = {"_id":341,"name":"kybrd75","force_text":(110,310)}
kybrd76_force_text = {"_id":342,"name":"kybrd76","force_text":(160,310)}
kybrd77_force_text = {"_id":343,"name":"kybrd77","force_text":(210,310)}
kybrd78_force_text = {"_id":344,"name":"kybrd78","force_text":(260,310)}
kybrd79_force_text = {"_id":345,"name":"kybrd79","force_text":(310,310)}
kybrd80_force_text = {"_id":346,"name":"kybrd80","force_text":(360,310)}
kybrd81_force_text = {"_id":347,"name":"kybrd81","force_text":(410,310)}
kybrd82_force_text = {"_id":348,"name":"kybrd82","force_text":(460,310)}
kybrd83_force_text = {"_id":349,"name":"kybrd83","force_text":(510,310)}
kybrd84_force_text = {"_id":350,"name":"kybrd84","force_text":(560,310)}
kybrd85_force_text = {"_id":351,"name":"kybrd85","force_text":(610,310)}
kybrd86_force_text = {"_id":352,"name":"kybrd86","force_text":(710,310)}
kybrd87_force_text = {"_id":353,"name":"kybrd87","force_text":(895,310)}
kybrd88_force_text = {"_id":354,"name":"kybrd88","force_text":(1024,310)}
kybrd89_force_text = {"_id":355,"name":"kybrd89","force_text":(1074,310)}
kybrd90_force_text = {"_id":356,"name":"kybrd90","force_text":(1124,310)}
kybrd91_force_text = {"_id":357,"name":"kybrd91","force_text":(1174,335)}
kybrd92_force_text = {"_id":358,"name":"kybrd92","force_text":(65,360)}
kybrd93_force_text = {"_id":359,"name":"kybrd93","force_text":(125,360)}
kybrd94_force_text = {"_id":360,"name":"kybrd94","force_text":(185,360)}
kybrd95_force_text = {"_id":361,"name":"kybrd95","force_text":(375,360)}
kybrd96_force_text = {"_id":362,"name":"kybrd96","force_text":(565,360)}
kybrd97_force_text = {"_id":363,"name":"kybrd97","force_text":(625,360)}
kybrd98_force_text = {"_id":364,"name":"kybrd98","force_text":(685,360)}
kybrd99_force_text = {"_id":365,"name":"kybrd99","force_text":(755,360)}
kybrd100_force_text = {"_id":366,"name":"kybrd100","force_text":(845,360)}
kybrd101_force_text = {"_id":367,"name":"kybrd101","force_text":(895,360)}
kybrd102_force_text = {"_id":368,"name":"kybrd102","force_text":(945,360)}
kybrd103_force_text = {"_id":369,"name":"kybrd103","force_text":(1050,360)}
kybrd104_force_text = {"_id":370,"name":"kybrd104","force_text":(1124,360)}
collection.insert_one(alaska_force_text)
collection.insert_one(north_west_territory_force_text)
collection.insert_one(alberta_force_text)
collection.insert_one(ontario_force_text)
collection.insert_one(quebec_force_text)
collection.insert_one(western_united_states_force_text)
collection.insert_one(eastern_united_states_force_text)
collection.insert_one(greenland_force_text)
collection.insert_one(mexico_force_text)
collection.insert_one(venezuela_force_text)
collection.insert_one(peru_force_text)
collection.insert_one(argentina_force_text)
collection.insert_one(brazil_force_text)
collection.insert_one(iceland_force_text)
collection.insert_one(scandinavia_force_text)
collection.insert_one(great_britain_force_text)
collection.insert_one(western_europe_force_text)
collection.insert_one(northern_europe_force_text)
collection.insert_one(southern_europe_force_text)
collection.insert_one(ukraine_force_text)
collection.insert_one(north_africa_force_text)
collection.insert_one(egypt_force_text)
collection.insert_one(sudan_force_text)
collection.insert_one(congo_force_text)
collection.insert_one(south_africa_force_text)
collection.insert_one(madagascar_force_text)
collection.insert_one(middle_east_force_text)
collection.insert_one(india_force_text)
collection.insert_one(siam_force_text)
collection.insert_one(china_force_text)
collection.insert_one(central_asia_force_text)
collection.insert_one(ural_force_text)
collection.insert_one(siberia_force_text)
collection.insert_one(yakutsk_force_text)
collection.insert_one(irkutsk_force_text)
collection.insert_one(kamtchatka_force_text)
collection.insert_one(mongolia_force_text)
collection.insert_one(japan_force_text)
collection.insert_one(indonesia_force_text)
collection.insert_one(papau_new_guinea_force_text)
collection.insert_one(western_australia_force_text)
collection.insert_one(eastern_australia_force_text)
collection.insert_one(hex0_force_text)
collection.insert_one(hex1_force_text)
collection.insert_one(hex2_force_text)
collection.insert_one(hex3_force_text)
collection.insert_one(hex4_force_text)
collection.insert_one(hex5_force_text)
collection.insert_one(hex6_force_text)
collection.insert_one(hex7_force_text)
collection.insert_one(hex8_force_text)
collection.insert_one(hex9_force_text)
collection.insert_one(hex10_force_text)
collection.insert_one(hex11_force_text)
collection.insert_one(hex12_force_text)
collection.insert_one(hex13_force_text)
collection.insert_one(hex14_force_text)
collection.insert_one(hex15_force_text)
collection.insert_one(hex16_force_text)
collection.insert_one(hex17_force_text)
collection.insert_one(hex18_force_text)
collection.insert_one(hex19_force_text)
collection.insert_one(hex20_force_text)
collection.insert_one(hex21_force_text)
collection.insert_one(hex22_force_text)
collection.insert_one(hex23_force_text)
collection.insert_one(hex24_force_text)
collection.insert_one(hex25_force_text)
collection.insert_one(hex26_force_text)
collection.insert_one(hex27_force_text)
collection.insert_one(hex28_force_text)

collection.insert_one(hex29_force_text)
collection.insert_one(hex30_force_text)
collection.insert_one(hex31_force_text)
collection.insert_one(hex32_force_text)
collection.insert_one(hex33_force_text)
collection.insert_one(hex34_force_text)
collection.insert_one(hex35_force_text)
collection.insert_one(hex36_force_text)
collection.insert_one(hex37_force_text)
collection.insert_one(hex38_force_text)
collection.insert_one(hex39_force_text)
collection.insert_one(hex40_force_text)
collection.insert_one(hex41_force_text)
collection.insert_one(hex42_force_text)
collection.insert_one(hex43_force_text)
collection.insert_one(hex44_force_text)
collection.insert_one(hex45_force_text)
collection.insert_one(hex46_force_text)
collection.insert_one(hex47_force_text)
collection.insert_one(hex48_force_text)
collection.insert_one(hex49_force_text)
collection.insert_one(hex50_force_text)
collection.insert_one(hex51_force_text)
collection.insert_one(hex52_force_text)
collection.insert_one(hex53_force_text)
collection.insert_one(hex54_force_text)
collection.insert_one(hex55_force_text)
collection.insert_one(pyr0_force_text)
collection.insert_one(pyr1_force_text)
collection.insert_one(pyr2_force_text)
collection.insert_one(pyr3_force_text)
collection.insert_one(pyr4_force_text)
collection.insert_one(pyr5_force_text)
collection.insert_one(pyr6_force_text)
collection.insert_one(pyr7_force_text)
collection.insert_one(pyr8_force_text)
collection.insert_one(pyr9_force_text)
collection.insert_one(pyr10_force_text)
collection.insert_one(pyr11_force_text)
collection.insert_one(pyr12_force_text)
collection.insert_one(pyr13_force_text)
collection.insert_one(pyr14_force_text)
collection.insert_one(pyr15_force_text)
collection.insert_one(pyr16_force_text)
collection.insert_one(pyr17_force_text)
collection.insert_one(pyr18_force_text)
collection.insert_one(pyr19_force_text)
collection.insert_one(pyr20_force_text)
collection.insert_one(pyr21_force_text)
collection.insert_one(pyr22_force_text)
collection.insert_one(pyr23_force_text)
collection.insert_one(pyr24_force_text)
collection.insert_one(pyr25_force_text)
collection.insert_one(pyr26_force_text)
collection.insert_one(pyr27_force_text)
collection.insert_one(pyr28_force_text)
collection.insert_one(pyr29_force_text)
collection.insert_one(pyr30_force_text)
collection.insert_one(pyr31_force_text)
collection.insert_one(pyr32_force_text)
collection.insert_one(pyr33_force_text)
collection.insert_one(pyr34_force_text)
collection.insert_one(pyr35_force_text)
collection.insert_one(pyr36_force_text)
collection.insert_one(pyr37_force_text)
collection.insert_one(pyr38_force_text)
collection.insert_one(pyr39_force_text)
collection.insert_one(pyr40_force_text)
collection.insert_one(pyr41_force_text)
collection.insert_one(pyr42_force_text)
collection.insert_one(pyr43_force_text)
collection.insert_one(pyr44_force_text)
collection.insert_one(pyr45_force_text)
collection.insert_one(pyr46_force_text)
collection.insert_one(pyr47_force_text)
collection.insert_one(pyr48_force_text)
collection.insert_one(pyr49_force_text)
collection.insert_one(pyr50_force_text)
collection.insert_one(pyr51_force_text)
collection.insert_one(pyr52_force_text)
collection.insert_one(pyr53_force_text)
collection.insert_one(pyr54_force_text)
collection.insert_one(pyr55_force_text)
collection.insert_one(pyr56_force_text)
collection.insert_one(pyr57_force_text)
collection.insert_one(pyr58_force_text)
collection.insert_one(pyr59_force_text)
collection.insert_one(pyr60_force_text)
collection.insert_one(pyr61_force_text)
collection.insert_one(pyr62_force_text)
collection.insert_one(pyr63_force_text)
collection.insert_one(qck0_force_text)
collection.insert_one(qck1_force_text)
collection.insert_one(qck2_force_text)
collection.insert_one(qck3_force_text)
collection.insert_one(srs0_force_text)
collection.insert_one(srs1_force_text)
collection.insert_one(srs2_force_text)
collection.insert_one(srs3_force_text)
collection.insert_one(srs4_force_text)
collection.insert_one(srs5_force_text)
collection.insert_one(srs6_force_text)
collection.insert_one(srs7_force_text)
collection.insert_one(srs8_force_text)
collection.insert_one(srs9_force_text)
collection.insert_one(srs10_force_text)
collection.insert_one(srs11_force_text)
collection.insert_one(srs12_force_text)
collection.insert_one(srs13_force_text)
collection.insert_one(srs14_force_text)
collection.insert_one(srs15_force_text)
collection.insert_one(srs16_force_text)
collection.insert_one(srs17_force_text)
collection.insert_one(srs18_force_text)
collection.insert_one(srs19_force_text)
collection.insert_one(srs20_force_text)
collection.insert_one(srs21_force_text)
collection.insert_one(srs22_force_text)
collection.insert_one(srs23_force_text)
collection.insert_one(srs24_force_text)
collection.insert_one(srs25_force_text)
collection.insert_one(srs26_force_text)
collection.insert_one(srs27_force_text)
collection.insert_one(srs28_force_text)
collection.insert_one(srs29_force_text)
collection.insert_one(srs30_force_text)
collection.insert_one(srs31_force_text)
collection.insert_one(sqr0_force_text)
collection.insert_one(sqr1_force_text)
collection.insert_one(sqr2_force_text)
collection.insert_one(sqr3_force_text)
collection.insert_one(sqr4_force_text)
collection.insert_one(sqr5_force_text)
collection.insert_one(sqr6_force_text)
collection.insert_one(sqr7_force_text)
collection.insert_one(sqr8_force_text)
collection.insert_one(sqr9_force_text)
collection.insert_one(sqr10_force_text)
collection.insert_one(sqr11_force_text)
collection.insert_one(sqr12_force_text)
collection.insert_one(sqr13_force_text)
collection.insert_one(sqr14_force_text)
collection.insert_one(sqr15_force_text)
collection.insert_one(sqr16_force_text)
collection.insert_one(sqr17_force_text)
collection.insert_one(sqr18_force_text)
collection.insert_one(sqr19_force_text)
collection.insert_one(sqr20_force_text)
collection.insert_one(sqr21_force_text)
collection.insert_one(sqr22_force_text)
collection.insert_one(sqr23_force_text)
collection.insert_one(sqr24_force_text)
collection.insert_one(sqr25_force_text)
collection.insert_one(sqr26_force_text)
collection.insert_one(sqr27_force_text)
collection.insert_one(sqr28_force_text)
collection.insert_one(sqr29_force_text)
collection.insert_one(sqr30_force_text)
collection.insert_one(sqr31_force_text)
collection.insert_one(sqr32_force_text)
collection.insert_one(sqr33_force_text)
collection.insert_one(sqr34_force_text)
collection.insert_one(sqr35_force_text)
collection.insert_one(stad0_force_text)
collection.insert_one(stad1_force_text)
collection.insert_one(stad2_force_text)
collection.insert_one(stad3_force_text)
collection.insert_one(stad4_force_text)
collection.insert_one(stad5_force_text)
collection.insert_one(stad6_force_text)
collection.insert_one(stad7_force_text)
collection.insert_one(stad8_force_text)
collection.insert_one(stad9_force_text)
collection.insert_one(stad10_force_text)
collection.insert_one(stad11_force_text)
collection.insert_one(stad12_force_text)
collection.insert_one(stad13_force_text)
collection.insert_one(stad14_force_text)
collection.insert_one(stad15_force_text)
collection.insert_one(stad16_force_text)
collection.insert_one(stad17_force_text)
collection.insert_one(stad18_force_text)
collection.insert_one(stad19_force_text)
collection.insert_one(stad20_force_text)
collection.insert_one(stad21_force_text)
collection.insert_one(stad22_force_text)
collection.insert_one(stad23_force_text)
collection.insert_one(stad24_force_text)
collection.insert_one(stad25_force_text)
collection.insert_one(stad26_force_text)
collection.insert_one(stad27_force_text)
collection.insert_one(stad28_force_text)
collection.insert_one(stad29_force_text)
collection.insert_one(stad30_force_text)
collection.insert_one(stad31_force_text)
collection.insert_one(kybrd0_force_text)
collection.insert_one(kybrd1_force_text)
collection.insert_one(kybrd2_force_text)
collection.insert_one(kybrd3_force_text)
collection.insert_one(kybrd4_force_text)
collection.insert_one(kybrd5_force_text)
collection.insert_one(kybrd6_force_text)
collection.insert_one(kybrd7_force_text)
collection.insert_one(kybrd8_force_text)
collection.insert_one(kybrd9_force_text)
collection.insert_one(kybrd10_force_text)
collection.insert_one(kybrd11_force_text)
collection.insert_one(kybrd12_force_text)
collection.insert_one(kybrd13_force_text)
collection.insert_one(kybrd14_force_text)
collection.insert_one(kybrd15_force_text)
collection.insert_one(kybrd16_force_text)

collection.insert_one(kybrd17_force_text)
collection.insert_one(kybrd18_force_text)
collection.insert_one(kybrd19_force_text)
collection.insert_one(kybrd20_force_text)
collection.insert_one(kybrd21_force_text)
collection.insert_one(kybrd22_force_text)
collection.insert_one(kybrd23_force_text)
collection.insert_one(kybrd24_force_text)
collection.insert_one(kybrd25_force_text)
collection.insert_one(kybrd26_force_text)
collection.insert_one(kybrd27_force_text)
collection.insert_one(kybrd28_force_text)
collection.insert_one(kybrd29_force_text)
collection.insert_one(kybrd30_force_text)
collection.insert_one(kybrd31_force_text)
collection.insert_one(kybrd32_force_text)
collection.insert_one(kybrd33_force_text)
collection.insert_one(kybrd34_force_text)
collection.insert_one(kybrd35_force_text)
collection.insert_one(kybrd36_force_text)
collection.insert_one(kybrd37_force_text)
collection.insert_one(kybrd38_force_text)
collection.insert_one(kybrd39_force_text)
collection.insert_one(kybrd40_force_text)
collection.insert_one(kybrd41_force_text)
collection.insert_one(kybrd42_force_text)
collection.insert_one(kybrd43_force_text)
collection.insert_one(kybrd44_force_text)
collection.insert_one(kybrd45_force_text)
collection.insert_one(kybrd46_force_text)
collection.insert_one(kybrd47_force_text)
collection.insert_one(kybrd48_force_text)
collection.insert_one(kybrd49_force_text)
collection.insert_one(kybrd50_force_text)
collection.insert_one(kybrd51_force_text)
collection.insert_one(kybrd52_force_text)
collection.insert_one(kybrd53_force_text)
collection.insert_one(kybrd54_force_text)
collection.insert_one(kybrd55_force_text)
collection.insert_one(kybrd56_force_text)
collection.insert_one(kybrd57_force_text)
collection.insert_one(kybrd58_force_text)
collection.insert_one(kybrd59_force_text)
collection.insert_one(kybrd60_force_text)
collection.insert_one(kybrd61_force_text)
collection.insert_one(kybrd62_force_text)
collection.insert_one(kybrd63_force_text)
collection.insert_one(kybrd64_force_text)
collection.insert_one(kybrd65_force_text)
collection.insert_one(kybrd66_force_text)
collection.insert_one(kybrd67_force_text)
collection.insert_one(kybrd68_force_text)
collection.insert_one(kybrd69_force_text)
collection.insert_one(kybrd70_force_text)
collection.insert_one(kybrd71_force_text)
collection.insert_one(kybrd72_force_text)
collection.insert_one(kybrd73_force_text)
collection.insert_one(kybrd74_force_text)
collection.insert_one(kybrd75_force_text)
collection.insert_one(kybrd76_force_text)
collection.insert_one(kybrd77_force_text)
collection.insert_one(kybrd78_force_text)
collection.insert_one(kybrd79_force_text)
collection.insert_one(kybrd80_force_text)
collection.insert_one(kybrd81_force_text)
collection.insert_one(kybrd82_force_text)
collection.insert_one(kybrd83_force_text)
collection.insert_one(kybrd84_force_text)
collection.insert_one(kybrd85_force_text)
collection.insert_one(kybrd86_force_text)
collection.insert_one(kybrd87_force_text)
collection.insert_one(kybrd88_force_text)
collection.insert_one(kybrd89_force_text)
collection.insert_one(kybrd90_force_text)
collection.insert_one(kybrd91_force_text)
collection.insert_one(kybrd92_force_text)
collection.insert_one(kybrd93_force_text)
collection.insert_one(kybrd94_force_text)
collection.insert_one(kybrd95_force_text)
collection.insert_one(kybrd96_force_text)
collection.insert_one(kybrd97_force_text)
collection.insert_one(kybrd98_force_text)
collection.insert_one(kybrd99_force_text)
collection.insert_one(kybrd100_force_text)
collection.insert_one(kybrd101_force_text)
collection.insert_one(kybrd102_force_text)
collection.insert_one(kybrd103_force_text)
collection.insert_one(kybrd104_force_text)