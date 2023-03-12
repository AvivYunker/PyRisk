import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_blob_links"]

alaska_blob_links = {"_id":0,"name":"alaska","valid_ids":[0],"strings": ["alaska (green) - blob.png","alaska (blue) - blob.png","alaska (yellow) - blob.png","alaska (red) - blob.png","alaska (orange) - blob.png","alaska (purple) - blob.png","alaska (grey) - blob.png"]}
north_west_territory_blob_links = {"_id":1,"name":"north_west_territory","valid_ids":[1],"strings": ["north_west_territory (green) - blob.png","north_west_territory (blue) - blob.png","north_west_territory (yellow) - blob.png","north_west_territory (red) - blob.png","north_west_territory (orange) - blob.png","north_west_territory (purple) - blob.png","north_west_territory (grey) - blob.png"]}
alberta_blob_links = {"_id":2,"name":"alberta","valid_ids":[2],"strings": ["alberta (green) - blob.png","alberta (blue) - blob.png","alberta (yellow) - blob.png","alberta (red) - blob.png","alberta (orange) - blob.png","alberta (purple) - blob.png","alberta (grey) - blob.png"]}
ontario_blob_links = {"_id":3,"name":"ontario","valid_ids":[3],"strings": ["ontario (green) - blob.png","ontario (blue) - blob.png","ontario (yellow) - blob.png","ontario (red) - blob.png","ontario (orange) - blob.png","ontario (purple) - blob.png","ontario (grey) - blob.png"]}
quebec_blob_links = {"_id":4,"name":"quebec","valid_ids":[4],"strings": ["quebec (green) - blob.png","quebec (blue) - blob.png","quebec (yellow) - blob.png","quebec (red) - blob.png","quebec (orange) - blob.png","quebec (purple) - blob.png","quebec (grey) - blob.png"]}
western_united_states_blob_links = {"_id":5,"name":"western_united_states","valid_ids":[5],"strings": ["western_united_states (green) - blob.png","western_united_states (blue) - blob.png","western_united_states (yellow) - blob.png","western_united_states (red) - blob.png","western_united_states (orange) - blob.png","western_united_states (purple) - blob.png","western_united_states (grey) - blob.png"]}
eastern_united_states_blob_links = {"_id":6,"name":"eastern_united_states","valid_ids":[6],"strings": ["eastern_united_states (green) - blob.png","eastern_united_states (blue) - blob.png","eastern_united_states (yellow) - blob.png","eastern_united_states (red) - blob.png","eastern_united_states (orange) - blob.png","eastern_united_states (purple) - blob.png","eastern_united_states (grey) - blob.png"]}
greenland_blob_links = {"_id":7,"name":"greenland","valid_ids":[7],"strings": ["greenland (green) - blob.png","greenland (blue) - blob.png","greenland (yellow) - blob.png","greenland (red) - blob.png","greenland (orange) - blob.png","greenland (purple) - blob.png","greenland (grey) - blob.png"]}
mexico_blob_links = {"_id":8,"name":"mexico","valid_ids":[8],"strings": ["mexico (green) - blob.png","mexico (blue) - blob.png","mexico (yellow) - blob.png","mexico (red) - blob.png","mexico (orange) - blob.png","mexico (purple) - blob.png","mexico (grey) - blob.png"]}
venezuela_blob_links = {"_id":9,"name":"venezuela","valid_ids":[9],"strings": ["venezuela (green) - blob.png","venezuela (blue) - blob.png","venezuela (yellow) - blob.png","venezuela (red) - blob.png","venezuela (orange) - blob.png","venezuela (purple) - blob.png","venezuela (grey) - blob.png"]}
peru_blob_links = {"_id":10,"name":"peru","valid_ids":[10],"strings": ["peru (green) - blob.png","peru (blue) - blob.png","peru (yellow) - blob.png","peru (red) - blob.png","peru (orange) - blob.png","peru (purple) - blob.png","peru (grey) - blob.png"]}
argentina_blob_links = {"_id":11,"name":"argentina","valid_ids":[11],"strings": ["argentina (green) - blob.png","argentina (blue) - blob.png","argentina (yellow) - blob.png","argentina (red) - blob.png","argentina (orange) - blob.png","argentina (purple) - blob.png","argentina (grey) - blob.png"]}
brazil_blob_links = {"_id":12,"name":"brazil","valid_ids":[12],"strings": ["brazil (green) - blob.png","brazil (blue) - blob.png","brazil (yellow) - blob.png","brazil (red) - blob.png","brazil (orange) - blob.png","brazil (purple) - blob.png","brazil (grey) - blob.png"]}
iceland_blob_links = {"_id":13,"name":"iceland","valid_ids":[13],"strings": ["iceland (green) - blob.png","iceland (blue) - blob.png","iceland (yellow) - blob.png","iceland (red) - blob.png","iceland (orange) - blob.png","iceland (purple) - blob.png","iceland (grey) - blob.png"]}
scandinavia_blob_links = {"_id":14,"name":"scandinavia","valid_ids":[14],"strings": ["scandinavia (green) - blob.png","scandinavia (blue) - blob.png","scandinavia (yellow) - blob.png","scandinavia (red) - blob.png","scandinavia (orange) - blob.png","scandinavia (purple) - blob.png","scandinavia (grey) - blob.png"]}
great_britain_blob_links = {"_id":15,"name":"great_britain","valid_ids":[15],"strings": ["great_britain (green) - blob.png","great_britain (blue) - blob.png","great_britain (yellow) - blob.png","great_britain (red) - blob.png","great_britain (orange) - blob.png","great_britain (purple) - blob.png","great_britain (grey) - blob.png"]}
western_europe_blob_links = {"_id":16,"name":"western_europe","valid_ids":[16],"strings": ["western_europe (green) - blob.png","western_europe (blue) - blob.png","western_europe (yellow) - blob.png","western_europe (red) - blob.png","western_europe (orange) - blob.png","western_europe (purple) - blob.png","western_europe (grey) - blob.png"]}
northern_europe_blob_links = {"_id":17,"name":"northern_europe","valid_ids":[17],"strings": ["northern_europe (green) - blob.png","northern_europe (blue) - blob.png","northern_europe (yellow) - blob.png","northern_europe (red) - blob.png","northern_europe (orange) - blob.png","northern_europe (purple) - blob.png","northern_europe (grey) - blob.png"]}
southern_europe_blob_links = {"_id":18,"name":"southern_europe","valid_ids":[18],"strings": ["southern_europe (green) - blob.png","southern_europe (blue) - blob.png","southern_europe (yellow) - blob.png","southern_europe (red) - blob.png","southern_europe (orange) - blob.png","southern_europe (purple) - blob.png","southern_europe (grey) - blob.png"]}
ukraine_blob_links = {"_id":19,"name":"ukraine","valid_ids":[19],"strings": ["ukraine (green) - blob.png","ukraine (blue) - blob.png","ukraine (yellow) - blob.png","ukraine (red) - blob.png","ukraine (orange) - blob.png","ukraine (purple) - blob.png","ukraine (grey) - blob.png"]}
north_africa_blob_links = {"_id":20,"name":"north_africa","valid_ids":[20],"strings": ["north_africa (green) - blob.png","north_africa (blue) - blob.png","north_africa (yellow) - blob.png","north_africa (red) - blob.png","north_africa (orange) - blob.png","north_africa (purple) - blob.png","north_africa (grey) - blob.png"]}
egypt_blob_links = {"_id":21,"name":"egypt","valid_ids":[21],"strings": ["egypt (green) - blob.png","egypt (blue) - blob.png","egypt (yellow) - blob.png","egypt (red) - blob.png","egypt (orange) - blob.png","egypt (purple) - blob.png","egypt (grey) - blob.png"]}
sudan_blob_links = {"_id":22,"name":"sudan","valid_ids":[22],"strings": ["sudan (green) - blob.png","sudan (blue) - blob.png","sudan (yellow) - blob.png","sudan (red) - blob.png","sudan (orange) - blob.png","sudan (purple) - blob.png","sudan (grey) - blob.png"]}
congo_blob_links = {"_id":23,"name":"congo","valid_ids":[23],"strings": ["congo (green) - blob.png","congo (blue) - blob.png","congo (yellow) - blob.png","congo (red) - blob.png","congo (orange) - blob.png","congo (purple) - blob.png","congo (grey) - blob.png"]}
south_africa_blob_links = {"_id":24,"name":"south_africa","valid_ids":[24],"strings": ["south_africa (green) - blob.png","south_africa (blue) - blob.png","south_africa (yellow) - blob.png","south_africa (red) - blob.png","south_africa (orange) - blob.png","south_africa (purple) - blob.png","south_africa (grey) - blob.png"]}
madagascar_blob_links = {"_id":25,"name":"madagascar","valid_ids":[25],"strings": ["madagascar (green) - blob.png","madagascar (blue) - blob.png","madagascar (yellow) - blob.png","madagascar (red) - blob.png","madagascar (orange) - blob.png","madagascar (purple) - blob.png","madagascar (grey) - blob.png"]}
middle_east_blob_links = {"_id":26,"name":"middle_east","valid_ids":[26],"strings": ["middle_east (green) - blob.png","middle_east (blue) - blob.png","middle_east (yellow) - blob.png","middle_east (red) - blob.png","middle_east (orange) - blob.png","middle_east (purple) - blob.png","middle_east (grey) - blob.png"]}
india_blob_links = {"_id":27,"name":"india","valid_ids":[27],"strings": ["india (green) - blob.png","india (blue) - blob.png","india (yellow) - blob.png","india (red) - blob.png","india (orange) - blob.png","india (purple) - blob.png","india (grey) - blob.png"]}
siam_blob_links = {"_id":28,"name":"siam","valid_ids":[28],"strings": ["siam (green) - blob.png","siam (blue) - blob.png","siam (yellow) - blob.png","siam (red) - blob.png","siam (orange) - blob.png","siam (purple) - blob.png","siam (grey) - blob.png"]}
china_blob_links = {"_id":29,"name":"china","valid_ids":[29],"strings": ["china (green) - blob.png","china (blue) - blob.png","china (yellow) - blob.png","china (red) - blob.png","china (orange) - blob.png","china (purple) - blob.png","china (grey) - blob.png"]}
central_asia_blob_links = {"_id":30,"name":"central_asia","valid_ids":[30],"strings": ["central_asia (green) - blob.png","central_asia (blue) - blob.png","central_asia (yellow) - blob.png","central_asia (red) - blob.png","central_asia (orange) - blob.png","central_asia (purple) - blob.png","central_asia (grey) - blob.png"]}
ural_blob_links = {"_id":31,"name":"ural","valid_ids":[31],"strings": ["ural (green) - blob.png","ural (blue) - blob.png","ural (yellow) - blob.png","ural (red) - blob.png","ural (orange) - blob.png","ural (purple) - blob.png","ural (grey) - blob.png"]}
siberia_blob_links = {"_id":32,"name":"siberia","valid_ids":[32],"strings": ["siberia (green) - blob.png","siberia (blue) - blob.png","siberia (yellow) - blob.png","siberia (red) - blob.png","siberia (orange) - blob.png","siberia (purple) - blob.png","siberia (grey) - blob.png"]}
yakutsk_blob_links = {"_id":33,"name":"yakutsk","valid_ids":[33],"strings": ["yakutsk (green) - blob.png","yakutsk (blue) - blob.png","yakutsk (yellow) - blob.png","yakutsk (red) - blob.png","yakutsk (orange) - blob.png","yakutsk (purple) - blob.png","yakutsk (grey) - blob.png"]}
irkutsk_blob_links = {"_id":34,"name":"irkutsk","valid_ids":[34],"strings": ["irkutsk (green) - blob.png","irkutsk (blue) - blob.png","irkutsk (yellow) - blob.png","irkutsk (red) - blob.png","irkutsk (orange) - blob.png","irkutsk (purple) - blob.png","irkutsk (grey) - blob.png"]}
kamtchatka_blob_links = {"_id":35,"name":"kamtchatka","valid_ids":[35],"strings": ["kamtchatka (green) - blob.png","kamtchatka (blue) - blob.png","kamtchatka (yellow) - blob.png","kamtchatka (red) - blob.png","kamtchatka (orange) - blob.png","kamtchatka (purple) - blob.png","kamtchatka (grey) - blob.png"]}
mongolia_blob_links = {"_id":36,"name":"mongolia","valid_ids":[36],"strings": ["mongolia (green) - blob.png","mongolia (blue) - blob.png","mongolia (yellow) - blob.png","mongolia (red) - blob.png","mongolia (orange) - blob.png","mongolia (purple) - blob.png","mongolia (grey) - blob.png"]}
japan_blob_links = {"_id":37,"name":"japan","valid_ids":[37],"strings": ["japan (green) - blob.png","japan (blue) - blob.png","japan (yellow) - blob.png","japan (red) - blob.png","japan (orange) - blob.png","japan (purple) - blob.png","japan (grey) - blob.png"]}
indonesia_blob_links = {"_id":38,"name":"indonesia","valid_ids":[38],"strings": ["indonesia (green) - blob.png","indonesia (blue) - blob.png","indonesia (yellow) - blob.png","indonesia (red) - blob.png","indonesia (orange) - blob.png","indonesia (purple) - blob.png","indonesia (grey) - blob.png"]}
papau_new_guinea_blob_links = {"_id":39,"name":"papau_new_guinea","valid_ids":[39],"strings": ["papau_new_guinea (green) - blob.png","papau_new_guinea (blue) - blob.png","papau_new_guinea (yellow) - blob.png","papau_new_guinea (red) - blob.png","papau_new_guinea (orange) - blob.png","papau_new_guinea (purple) - blob.png","papau_new_guinea (grey) - blob.png"]}
western_australia_blob_links = {"_id":40,"name":"western_australia","valid_ids":[40],"strings": ["western_australia (green) - blob.png","western_australia (blue) - blob.png","western_australia (yellow) - blob.png","western_australia (red) - blob.png","western_australia (orange) - blob.png","western_australia (purple) - blob.png","western_australia (grey) - blob.png"]}
eastern_australia_blob_links = {"_id":41,"name":"eastern_australia","valid_ids":[41],"strings": ["eastern_australia (green) - blob.png","eastern_australia (blue) - blob.png","eastern_australia (yellow) - blob.png","eastern_australia (red) - blob.png","eastern_australia (orange) - blob.png","eastern_australia (purple) - blob.png","eastern_australia (grey) - blob.png"]}
hexagon_blob_links = {"_id":42,"name":"hexagon","valid_ids":[42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,],"strings": ["hexagon (green) - blob.png","hexagon (blue) - blob.png","hexagon (yellow) - blob.png","hexagon (red) - blob.png","hexagon (orange) - blob.png","hexagon (purple) - blob.png","hexagon (grey) - blob.png"]}
pyramid_upper_blob_links = {"_id":43,"name":"pyramid_upper","valid_ids":[98,99,101,102,104,106,107,109,111,113,114,116,118,120,122,123,125,127,129,131,133,134,136,138,140,142,144,146,147,149,151,153,155,157,159,161],"strings": ["pyramid_upper (green) - blob.png","pyramid_upper (blue) - blob.png","pyramid_upper (yellow) - blob.png","pyramid_upper (red) - blob.png","pyramid_upper (orange) - blob.png","pyramid_upper (purple) - blob.png","pyramid_upper (grey) - blob.png"]}
pyramid_lower_blob_links = {"_id":44,"name":"pyramid_lower","valid_ids":[100,103,105,108,110,112,115,117,119,121,124,126,128,130,132,135,137,139,141,143,145,148,150,152,154,156,158,160,],"strings": ["pyramid_lower (green) - blob.png","pyramid_lower (blue) - blob.png","pyramid_lower (yellow) - blob.png","pyramid_lower (red) - blob.png","pyramid_lower (orange) - blob.png","pyramid_lower (purple) - blob.png","pyramid_lower (grey) - blob.png"]}
quick_northern_blob_links = {"_id":45,"name":"quick_northern","valid_ids":[162],"strings": ["quick_northern (green) - blob.png","quick_northern (blue) - blob.png","quick_northern (yellow) - blob.png","quick_northern (red) - blob.png","quick_northern (orange) - blob.png","quick_northern (purple) - blob.png","quick_northern (grey) - blob.png"]}
quick_western_blob_links = {"_id":46,"name":"quick_western","valid_ids":[163],"strings": ["quick_western (green) - blob.png","quick_western (blue) - blob.png","quick_western (yellow) - blob.png","quick_western (red) - blob.png","quick_western (orange) - blob.png","quick_western (purple) - blob.png","quick_western (grey) - blob.png"]}
quick_eastern_blob_links = {"_id":47,"name":"quick_eastern","valid_ids":[164],"strings": ["quick_eastern (green) - blob.png","quick_eastern (blue) - blob.png","quick_eastern (yellow) - blob.png","quick_eastern (red) - blob.png","quick_eastern (orange) - blob.png","quick_eastern (purple) - blob.png","quick_eastern (grey) - blob.png"]}
quick_southern_blob_links = {"_id":48,"name":"quick_southern","valid_ids":[165],"strings": ["quick_southern (green) - blob.png","quick_southern (blue) - blob.png","quick_southern (yellow) - blob.png","quick_southern (red) - blob.png","quick_southern (orange) - blob.png","quick_southern (purple) - blob.png","quick_southern (grey) - blob.png"]}
serious_1_blob_links = {"_id":49,"name":"serious_1","valid_ids":[166,170,176,180,182,186,192,196],"strings": ["serious_1 (green) - blob.png","serious_1 (blue) - blob.png","serious_1 (yellow) - blob.png","serious_1 (red) - blob.png","serious_1 (orange) - blob.png","serious_1 (purple) - blob.png","serious_1 (grey) - blob.png"]}
serious_2_blob_links = {"_id":50,"name":"serious_2","valid_ids":[167,171,177,181,183,187,193,197],"strings": ["serious_2 (green) - blob.png","serious_2 (blue) - blob.png","serious_2 (yellow) - blob.png","serious_2 (red) - blob.png","serious_2 (orange) - blob.png","serious_2 (purple) - blob.png","serious_2 (grey) - blob.png"]}
serious_3_blob_links = {"_id":51,"name":"serious_3","valid_ids":[168,172,174,178,184,188,190,194],"strings": ["serious_3 (green) - blob.png","serious_3 (blue) - blob.png","serious_3 (yellow) - blob.png","serious_3 (red) - blob.png","serious_3 (orange) - blob.png","serious_3 (purple) - blob.png","serious_3 (grey) - blob.png"]}
serious_4_blob_links = {"_id":52,"name":"serious_4","valid_ids":[169,173,175,179,185,189,191,195],"strings": ["serious_4 (green) - blob.png","serious_4 (blue) - blob.png","serious_4 (yellow) - blob.png","serious_4 (red) - blob.png","serious_4 (orange) - blob.png","serious_4 (purple) - blob.png","serious_4 (grey) - blob.png"]}
square_blob_links = {"_id":53,"name":"square","valid_ids":[198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233],"strings": ["square (green) - blob.png","square (blue) - blob.png","square (yellow) - blob.png","square (red) - blob.png","square (orange) - blob.png","square (purple) - blob.png","square (grey) - blob.png"]}
inner_arc_1_blob_links = {"_id":54,"name":"inner_arc_1","valid_ids":[242],"strings": ["inner_arc_1 (green) - blob.png","inner_arc_1 (blue) - blob.png","inner_arc_1 (yellow) - blob.png","inner_arc_1 (red) - blob.png","inner_arc_1 (orange) - blob.png","inner_arc_1 (purple) - blob.png","inner_arc_1 (grey) - blob.png"]}
inner_arc_2_blob_links = {"_id":55,"name":"inner_arc_2","valid_ids":[241],"strings": ["inner_arc_2 (green) - blob.png","inner_arc_2 (blue) - blob.png","inner_arc_2 (yellow) - blob.png","inner_arc_2 (red) - blob.png","inner_arc_2 (orange) - blob.png","inner_arc_2 (purple) - blob.png","inner_arc_2 (grey) - blob.png"]}
inner_arc_3_blob_links = {"_id":56,"name":"inner_arc_3","valid_ids":[251],"strings": ["inner_arc_3 (green) - blob.png","inner_arc_3 (blue) - blob.png","inner_arc_3 (yellow) - blob.png","inner_arc_3 (red) - blob.png","inner_arc_3 (orange) - blob.png","inner_arc_3 (purple) - blob.png","inner_arc_3 (grey) - blob.png"]}
inner_arc_4_blob_links = {"_id":57,"name":"inner_arc_4","valid_ids":[252],"strings": ["inner_arc_4 (green) - blob.png","inner_arc_4 (blue) - blob.png","inner_arc_4 (yellow) - blob.png","inner_arc_4 (red) - blob.png","inner_arc_4 (orange) - blob.png","inner_arc_4 (purple) - blob.png","inner_arc_4 (grey) - blob.png"]}
inner_arc_5_blob_links = {"_id":58,"name":"inner_arc_5","valid_ids":[247],"strings": ["inner_arc_5 (green) - blob.png","inner_arc_5 (blue) - blob.png","inner_arc_5 (yellow) - blob.png","inner_arc_5 (red) - blob.png","inner_arc_5 (orange) - blob.png","inner_arc_5 (purple) - blob.png","inner_arc_5 (grey) - blob.png"]}
inner_arc_6_blob_links = {"_id":59,"name":"inner_arc_6","valid_ids":[248],"strings": ["inner_arc_6 (green) - blob.png","inner_arc_6 (blue) - blob.png","inner_arc_6 (yellow) - blob.png","inner_arc_6 (red) - blob.png","inner_arc_6 (orange) - blob.png","inner_arc_6 (purple) - blob.png","inner_arc_6 (grey) - blob.png"]}
inner_arc_7_blob_links = {"_id":60,"name":"inner_arc_7","valid_ids":[258],"strings": ["inner_arc_7 (green) - blob.png","inner_arc_7 (blue) - blob.png","inner_arc_7 (yellow) - blob.png","inner_arc_7 (red) - blob.png","inner_arc_7 (orange) - blob.png","inner_arc_7 (purple) - blob.png","inner_arc_7 (grey) - blob.png"]}
inner_arc_8_blob_links = {"_id":61,"name":"inner_arc_8","valid_ids":[257],"strings": ["inner_arc_8 (green) - blob.png","inner_arc_8 (blue) - blob.png","inner_arc_8 (yellow) - blob.png","inner_arc_8 (red) - blob.png","inner_arc_8 (orange) - blob.png","inner_arc_8 (purple) - blob.png","inner_arc_8 (grey) - blob.png"]}
outer_arc_1_blob_links = {"_id":62,"name":"outer_arc_1","valid_ids":[234],"strings": ["outer_arc_1 (green) - blob.png","outer_arc_1 (blue) - blob.png","outer_arc_1 (yellow) - blob.png","outer_arc_1 (red) - blob.png","outer_arc_1 (orange) - blob.png","outer_arc_1 (purple) - blob.png","outer_arc_1 (grey) - blob.png"]}
outer_arc_2_blob_links = {"_id":63,"name":"outer_arc_2","valid_ids":[240],"strings": ["outer_arc_2 (green) - blob.png","outer_arc_2 (blue) - blob.png","outer_arc_2 (yellow) - blob.png","outer_arc_2 (red) - blob.png","outer_arc_2 (orange) - blob.png","outer_arc_2 (purple) - blob.png","outer_arc_2 (grey) - blob.png"]}
outer_arc_3_blob_links = {"_id":64,"name":"outer_arc_3","valid_ids":[250],"strings": ["outer_arc_3 (green) - blob.png","outer_arc_3 (blue) - blob.png","outer_arc_3 (yellow) - blob.png","outer_arc_3 (red) - blob.png","outer_arc_3 (orange) - blob.png","outer_arc_3 (purple) - blob.png","outer_arc_3 (grey) - blob.png"]}
outer_arc_4_blob_links = {"_id":65,"name":"outer_arc_4","valid_ids":[260],"strings": ["outer_arc_4 (green) - blob.png","outer_arc_4 (blue) - blob.png","outer_arc_4 (yellow) - blob.png","outer_arc_4 (red) - blob.png","outer_arc_4 (orange) - blob.png","outer_arc_4 (purple) - blob.png","outer_arc_4 (grey) - blob.png"]}
outer_arc_5_blob_links = {"_id":66,"name":"outer_arc_5","valid_ids":[239],"strings": ["outer_arc_5 (green) - blob.png","outer_arc_5 (blue) - blob.png","outer_arc_5 (yellow) - blob.png","outer_arc_5 (red) - blob.png","outer_arc_5 (orange) - blob.png","outer_arc_5 (purple) - blob.png","outer_arc_5 (grey) - blob.png"]}
outer_arc_6_blob_links = {"_id":67,"name":"outer_arc_6","valid_ids":[249],"strings": ["outer_arc_6 (green) - blob.png","outer_arc_6 (blue) - blob.png","outer_arc_6 (yellow) - blob.png","outer_arc_6 (red) - blob.png","outer_arc_6 (orange) - blob.png","outer_arc_6 (purple) - blob.png","outer_arc_6 (grey) - blob.png"]}
outer_arc_7_blob_links = {"_id":68,"name":"outer_arc_7","valid_ids":[259],"strings": ["outer_arc_7 (green) - blob.png","outer_arc_7 (blue) - blob.png","outer_arc_7 (yellow) - blob.png","outer_arc_7 (red) - blob.png","outer_arc_7 (orange) - blob.png","outer_arc_7 (purple) - blob.png","outer_arc_7 (grey) - blob.png"]}
outer_arc_8_blob_links = {"_id":69,"name":"outer_arc_8","valid_ids":[265],"strings": ["outer_arc_8 (green) - blob.png","outer_arc_8 (blue) - blob.png","outer_arc_8 (yellow) - blob.png","outer_arc_8 (red) - blob.png","outer_arc_8 (orange) - blob.png","outer_arc_8 (purple) - blob.png","outer_arc_8 (grey) - blob.png"]}
stadium_square_blob_links = {"_id":70,"name":"stadium_square","valid_ids":[235,236,237,238,243,244,245,246,253,254,255,256,261,262,263,264],"strings": ["stadium_square (green) - blob.png","stadium_square (blue) - blob.png","stadium_square (yellow) - blob.png","stadium_square (red) - blob.png","stadium_square (orange) - blob.png","stadium_square (purple) - blob.png","stadium_square (grey) - blob.png"]}
keyboard_button_1_blob_links = {"_id":71,"name":"keyboard_button_1","valid_ids":[266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,296,297,298,299,300,301,302,304,305,306,307,308,309,310,311,312,313,314,315,317,318,319,320,321,322,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,353,354,355,356,366,367,368,370],"strings": ["keyboard_button_1 (green) - blob.png","keyboard_button_1 (blue) - blob.png","keyboard_button_1 (yellow) - blob.png","keyboard_button_1 (red) - blob.png","keyboard_button_1 (orange) - blob.png","keyboard_button_1 (purple) - blob.png","keyboard_button_1 (grey) - blob.png"]}
keyboard_button_2_blob_links = {"_id":72,"name":"keyboard_button_2","valid_ids":[295],"strings": ["keyboard_button_2 (green) - blob.png","keyboard_button_2 (blue) - blob.png","keyboard_button_2 (yellow) - blob.png","keyboard_button_2 (red) - blob.png","keyboard_button_2 (orange) - blob.png","keyboard_button_2 (purple) - blob.png","keyboard_button_2 (grey) - blob.png"]}
keyboard_button_3_blob_links = {"_id":73,"name":"keyboard_button_3","valid_ids":[303],"strings": ["keyboard_button_3 (green) - blob.png","keyboard_button_3 (blue) - blob.png","keyboard_button_3 (yellow) - blob.png","keyboard_button_3 (red) - blob.png","keyboard_button_3 (orange) - blob.png","keyboard_button_3 (purple) - blob.png","keyboard_button_3 (grey) - blob.png"]}
keyboard_button_4_blob_links = {"_id":74,"name":"keyboard_button_4","valid_ids":[316],"strings": ["keyboard_button_4 (green) - blob.png","keyboard_button_4 (blue) - blob.png","keyboard_button_4 (yellow) - blob.png","keyboard_button_4 (red) - blob.png","keyboard_button_4 (orange) - blob.png","keyboard_button_4 (purple) - blob.png","keyboard_button_4 (grey) - blob.png"]}
keyboard_button_5_blob_links = {"_id":75,"name":"keyboard_button_5","valid_ids":[323,357],"strings": ["keyboard_button_5 (green) - blob.png","keyboard_button_5 (blue) - blob.png","keyboard_button_5 (yellow) - blob.png","keyboard_button_5 (red) - blob.png","keyboard_button_5 (orange) - blob.png","keyboard_button_5 (purple) - blob.png","keyboard_button_5 (grey) - blob.png"]}
keyboard_button_6_blob_links = {"_id":76,"name":"keyboard_button_6","valid_ids":[324],"strings": ["keyboard_button_6 (green) - blob.png","keyboard_button_6 (blue) - blob.png","keyboard_button_6 (yellow) - blob.png","keyboard_button_6 (red) - blob.png","keyboard_button_6 (orange) - blob.png","keyboard_button_6 (purple) - blob.png","keyboard_button_6 (grey) - blob.png"]}
keyboard_button_7_blob_links = {"_id":77,"name":"keyboard_button_7","valid_ids":[352],"strings": ["keyboard_button_7 (green) - blob.png","keyboard_button_7 (blue) - blob.png","keyboard_button_7 (yellow) - blob.png","keyboard_button_7 (red) - blob.png","keyboard_button_7 (orange) - blob.png","keyboard_button_7 (purple) - blob.png","keyboard_button_7 (grey) - blob.png"]}
keyboard_button_8_blob_links = {"_id":78,"name":"keyboard_button_8","valid_ids":[358,359,360,362,363,364],"strings": ["keyboard_button_8 (green) - blob.png","keyboard_button_8 (blue) - blob.png","keyboard_button_8 (yellow) - blob.png","keyboard_button_8 (red) - blob.png","keyboard_button_8 (orange) - blob.png","keyboard_button_8 (purple) - blob.png","keyboard_button_8 (grey) - blob.png"]}
keyboard_button_9_blob_links = {"_id":79,"name":"keyboard_button_9","valid_ids":[361],"strings": ["keyboard_button_9 (green) - blob.png","keyboard_button_9 (blue) - blob.png","keyboard_button_9 (yellow) - blob.png","keyboard_button_9 (red) - blob.png","keyboard_button_9 (orange) - blob.png","keyboard_button_9 (purple) - blob.png","keyboard_button_9 (grey) - blob.png"]}
keyboard_button_10_blob_links = {"_id":80,"name":"keyboard_button_10","valid_ids":[365],"strings": ["keyboard_button_10 (green) - blob.png","keyboard_button_10 (blue) - blob.png","keyboard_button_10 (yellow) - blob.png","keyboard_button_10 (red) - blob.png","keyboard_button_10 (orange) - blob.png","keyboard_button_10 (purple) - blob.png","keyboard_button_10 (grey) - blob.png"]}
keyboard_button_11_blob_links = {"_id":81,"name":"keyboard_button_11","valid_ids":[369],"strings": ["keyboard_button_11 (green) - blob.png","keyboard_button_11 (blue) - blob.png","keyboard_button_11 (yellow) - blob.png","keyboard_button_11 (red) - blob.png","keyboard_button_11 (orange) - blob.png","keyboard_button_11 (purple) - blob.png","keyboard_button_11 (grey) - blob.png"]}

collection.insert_one(alaska_blob_links)
collection.insert_one(north_west_territory_blob_links)
collection.insert_one(alberta_blob_links)
collection.insert_one(ontario_blob_links)
collection.insert_one(quebec_blob_links)
collection.insert_one(western_united_states_blob_links)
collection.insert_one(eastern_united_states_blob_links)
collection.insert_one(greenland_blob_links)
collection.insert_one(mexico_blob_links)
collection.insert_one(venezuela_blob_links)
collection.insert_one(peru_blob_links)
collection.insert_one(argentina_blob_links)
collection.insert_one(brazil_blob_links)
collection.insert_one(iceland_blob_links)
collection.insert_one(scandinavia_blob_links)
collection.insert_one(great_britain_blob_links)
collection.insert_one(western_europe_blob_links)
collection.insert_one(northern_europe_blob_links)
collection.insert_one(southern_europe_blob_links)
collection.insert_one(ukraine_blob_links)
collection.insert_one(north_africa_blob_links)
collection.insert_one(egypt_blob_links)
collection.insert_one(sudan_blob_links)
collection.insert_one(congo_blob_links)
collection.insert_one(south_africa_blob_links)
collection.insert_one(madagascar_blob_links)
collection.insert_one(middle_east_blob_links)
collection.insert_one(india_blob_links)
collection.insert_one(siam_blob_links)
collection.insert_one(china_blob_links)
collection.insert_one(central_asia_blob_links)
collection.insert_one(ural_blob_links)
collection.insert_one(siberia_blob_links)
collection.insert_one(yakutsk_blob_links)
collection.insert_one(irkutsk_blob_links)
collection.insert_one(kamtchatka_blob_links)
collection.insert_one(mongolia_blob_links)
collection.insert_one(japan_blob_links)
collection.insert_one(indonesia_blob_links)
collection.insert_one(papau_new_guinea_blob_links)
collection.insert_one(western_australia_blob_links)
collection.insert_one(eastern_australia_blob_links)
collection.insert_one(hexagon_blob_links)
collection.insert_one(pyramid_lower_blob_links)
collection.insert_one(pyramid_upper_blob_links)
collection.insert_one(quick_northern_blob_links)
collection.insert_one(quick_western_blob_links)
collection.insert_one(quick_eastern_blob_links)
collection.insert_one(quick_southern_blob_links)
collection.insert_one(serious_1_blob_links)
collection.insert_one(serious_2_blob_links)
collection.insert_one(serious_3_blob_links)
collection.insert_one(serious_4_blob_links)
collection.insert_one(square_blob_links)
collection.insert_one(inner_arc_1_blob_links)
collection.insert_one(inner_arc_2_blob_links)
collection.insert_one(inner_arc_3_blob_links)
collection.insert_one(inner_arc_4_blob_links)
collection.insert_one(inner_arc_5_blob_links)
collection.insert_one(inner_arc_6_blob_links)
collection.insert_one(inner_arc_7_blob_links)
collection.insert_one(inner_arc_8_blob_links)
collection.insert_one(outer_arc_1_blob_links)
collection.insert_one(outer_arc_2_blob_links)
collection.insert_one(outer_arc_3_blob_links)
collection.insert_one(outer_arc_4_blob_links)
collection.insert_one(outer_arc_5_blob_links)
collection.insert_one(outer_arc_6_blob_links)
collection.insert_one(outer_arc_7_blob_links)
collection.insert_one(outer_arc_8_blob_links)
collection.insert_one(stadium_square_blob_links)
collection.insert_one(keyboard_button_1_blob_links)
collection.insert_one(keyboard_button_2_blob_links)
collection.insert_one(keyboard_button_3_blob_links)
collection.insert_one(keyboard_button_4_blob_links)
collection.insert_one(keyboard_button_5_blob_links)
collection.insert_one(keyboard_button_6_blob_links)
collection.insert_one(keyboard_button_7_blob_links)
collection.insert_one(keyboard_button_8_blob_links)
collection.insert_one(keyboard_button_9_blob_links)
collection.insert_one(keyboard_button_10_blob_links)
collection.insert_one(keyboard_button_11_blob_links)