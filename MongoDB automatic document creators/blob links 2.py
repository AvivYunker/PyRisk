# alaska_link = {"name":"Alaska", "ids":(0),"strings":["(green)","(blue)","(yellow)","(red)"])
entire_string = ["alaska","north_west_territory","alberta","ontario","quebec","western_united_states","eastern_united_states","greenland","mexico","venezuela","peru","argentina","brazil","iceland","scandinavia","great_britain","western_europe","northern_europe","southern_europe","ukraine","north_africa","egypt","sudan","congo","south_africa","madagascar","middle_east","india","siam","china","central_asia","ural","siberia","yakutsk","irkutsk","kamtchatka","mongolia","japan","indonesia","papau_new_guinea","western_australia","eastern_australia","hexagon"," pyramid_lower"," pramid_upper","quick_northern","quick_western","quick_eastern","quick_southern","serious_1","serious_2","serious_3","serious_4","square","inner_arc_1","inner_arc_2","inner_arc_3","inner_arc_4","inner_arc_5","inner_arc_6","inner_arc_7","inner_arc_8","outer_arc_1","outer_arc_2","outer_arc_3","outer_arc_4","outer_arc_5","outer_arc_6","outer_arc_7","outer_arc_8","stadium_square","keyboard_button_1","keyboard_button_2","keyboard_button_3","keyboard_button_4","keyboard_button_5","keyboard_button_6","keyboard_button_7","keyboard_button_8","keyboard_button_9","keyboard_button_10","keyboard_button_11"]
color_list = [" (green)", " (blue)", " (yellow)", " (red)", " (orange)", " (purple)"]
blob_suffix = str(" - blob.png")
for cnt1 in range(0, 82, 1):
    print(str(entire_string[cnt1]) + '_blob_links = {"_id":' + str(cnt1) + ',"name":"' + str(str(entire_string[cnt1])) + '","strings": [', end="")
    #                         alaska_blob_links =         {"_id":"0",               "name":"alaska
    for cnt2 in range(0, 6, 1):
        print('"' + str(entire_string[cnt1]) + str(color_list[cnt2]) + str(blob_suffix), end='",')
    print("]}")


# collection.insert_one(alaska_blob_link)
for cnt1 in range(0, 82, 1):
    print("collection.insert_one(" + str(entire_string[cnt1]) + "_blob_links)")
