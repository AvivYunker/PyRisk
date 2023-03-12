import pygame # import the PyGame library.
pygame.init() # initialize the PyGame library.
from button_class import Button # import the "Button" class.
from territory_class import Territory # import the "Territory" class.
from player_class import Player # import the "Player" class.
from textbox_class import textBox # import the "textBox" class.
from game_saver import * # import all the functions from the 'game_saver' file
from gui_dice import * # import all the functions from 'gui_dice' file

import math # import the 'math' module.
import random # import the 'random' module.
import time # import the 'time' module.
import timeit # import the 'timeit' module

# back_mode, cnt, arr_players, arr_territories, totals, fortify_cnt, gui_text_levels, lv4_gt

def deter_init_cnt (arr_territories, arr_players, neutrals): # method for determining the initial count of players.
    if (neutrals == int(1)): # if the 'neutrals' option has been selected, then...
        arr_players[len(arr_players)-1].cnt_init = int(generate_neutral_count (arr_territories)) # generate the count of neutral zones (through the function)
        ttl = len(arr_territories) - (arr_players[len(arr_players)-1].cnt_init) # 'total' - the total amount of territories.
        edge_1 = math.ceil((len(arr_territories) - (arr_players[len(arr_players)-1].cnt_init)) / (len(arr_players)-1)) # the maximum amount of territories that a player can get.
        edge_2 = math.floor((len(arr_territories) - (arr_players[len(arr_players)-1].cnt_init)) / (len(arr_players)-1)) # the minimum amount of territories that a player can get.
    else: # otherwise - if 'neutrals' has NOT been selected, then...
        ttl = len(arr_territories) # 'total' - the total amount of territories.
        edge_1 = math.ceil(len(arr_territories) / len(arr_players)) # the maximum amount of territories that a player can get.
        edge_2 = math.floor(len(arr_territories) / len(arr_players)) # the minimum amount of territories that a player can get.
    #print("ttl is: " + str(ttl)) # debug print
    temp_list = [] # 'temporary-list' - 
    while (ttl > 0): # while there are at-least 1 territories that are available
        if (ttl % edge_1 == int(0)): # if we CAN give off maximum-count of territories, then...
            temp_list.append(edge_1) # we'll give that maximum number of territories.
            ttl = int(ttl - edge_1) # we must subtract that maximum number of territories from the amount of territories that is remaining.
        else: # in case that we cannot afford to subtract the 'maximum-count' of territories, but only the minimum amount of territories, then...
            temp_list.append(edge_2) # we';; give that minimum number of territories.
            ttl = int(ttl - edge_2) # we must subtract that minimum number of territories.
    #print("temp list is: " + str(temp_list)) # debug print
    if (neutrals == int(1)): # if the 'neutrals' option has been selected, then...
        lim = int(len(arr_players)-1) # the length will be '-1' the original length - because the 'neutrals' don't account for a real player
    else: # otherwise - if 'neutrals' has NOT been selected, then...
        lim = int(len(arr_players)) # the length will be the original - because all players are 'real' players (none-neutral).
    for cnt in range(0, lim, 1): # go through all the players...
        #print("Iteration no." + str(cnt)) # debug print.
        indx = random.randrange(0, len(temp_list)) # 'indx' is a random selection of a player.
        arr_players[cnt].cnt_init = int(temp_list[indx]) # assign the number that represents the initial count of territories of the selected player.
        temp_list.pop(indx) # remove the territory-amount number from the list - because it has already been assigned to a player (1 line above).
    

def auto_assign_all (arr_territories, arr_players, arr_assign, totals): # method for assigning all territories to all players
    #totals_0 = int(arr_territories[0].id_num) # irrelevant
    for cnt in range(0, len(arr_players), 1): # looping over the list of player-objects.
        while (arr_players[cnt].cnt_init > 0): # if the player still has some 'count' of territories to claim, then...
            pygame.display.update() ######
            indx = random.randrange(0, len(arr_assign)) # select a random territory from the list of available territories (unclaimed territories)
            arr_territories[arr_assign[indx] - totals[0]].controller = int(arr_players[cnt].id_num) # update the territory-attribute about the new controller of the territory.
            arr_territories[arr_assign[indx] - totals[0]].force_no = int(3) # assign a default of 3 forces to the randomly selected territory that has been claimed automatically.
            arr_players[cnt].trr_and_frc.update({str(arr_assign[indx]):3}) # assign the key-value pair to the dictionary of 'territory and force' of the player.
            arr_assign.pop(indx) # remove the randomly-selected-territory from the list of available territories, because this territory has just been assigned to a player and is no longer available.
            arr_players[cnt].cnt_init -= 1 # decrease the count of territories to be claimed (of the user) by 1.
      
def fill_arr_assign (arr_territories, arr_assign): # method for filling the available territories into a list (territories that have NOT been assigned to any player yet).
    for cnt in range(0,len(arr_territories), 1): # go through all of the territories...
        if (arr_territories[cnt].controller == int(-1)): # if the territory is NOT assigned to any player yet, then...
            arr_assign.append(arr_territories[cnt].id_num) # add the territory to the list of available territories.

def generate_neutral_count (arr_territories): # method for generating the number of territories that are neutral (only activated when the 'neutrals' option is positive).
    neut_cnt = int(len(arr_territories) / 4) # defines the maximum range of neutral territories count.
    return neut_cnt # return the count of neutrals zones.

def load_resolutions (res_arr, res_doc, selected_map): # method for getting the map-resolutions from the database.
    #print("selected map is: " + str(selected_map))
    RES = res_doc.find_one({"_id":(selected_map-1)}) # locate the matching "object" according to the map number.
    res_arr[0] = RES["res"][0] # 'X' of arr_res is 'X' of resolutions of located "object".
    res_arr[1] = RES["res"][1] # 'Y' of arr_res is 'Y' of resolutions of located "object".

def load_totals (ttl_arr, total_doc, selected_map): # method for getting all the ID-numbers (of territories) from the database.
    TOTAL = total_doc.find_one({"_id":(selected_map-1)}) # locate the metching "object" according to the map number.
    ttl_arr[0] = TOTAL["total"][0] # the ID-number of the first territory of the game-map.
    ttl_arr[1] = TOTAL["total"][1] # the ID-number of the last territory of the game-map.

def load_init_territories (arr_territories, totals, selected_map, screen): # method for loading all territories of the game-map
    for cnt in range(totals[0], totals[1]+1, 1): # go through the 'totals' (the ranges of ID-numbers of territories - for the specified map).
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
        arr_territories.append(Territory(cnt,0,0,0,0,0,0,0,0,0,0,screen)) # append to the list-of-territories the territory objects, with an incrementing ID-number.
    for cnt in range(0, len(arr_territories), 1): # go through the list of territories
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
        arr_territories[cnt].init_territory(selected_map) # initialize each of the territory-objects from the list of territories, one territory-object at a time.
    #print("Printing arr_territories:") # debug function.
    #for cnt in range(0, len(arr_territories), 1): # go through the list of territories # debug print
        #print(arr_territories[cnt].controller) # debug function (print the ID-number of the contoller of the territory).
    #print("finished printing arr territories") # debug function.


def print_arr_players (arr_players): # DEBUG FUNCITON
    print("BELOW IS ARR_PLAYERS:") # signify what we'll be looking at below...
    for cnt in range(0, len(arr_players), 1): # loop over the list of players.
        print("(", end="") # print a single round-bracket, DO NOT move to the next line.
        print(str(arr_players[cnt].id_num), end=",") # print the 'ID-number' attribute of the player-object.
        print(str(arr_players[cnt].color), end=",") # print the 'color' attribute of the player-object.
        print(str(arr_players[cnt].name), end=",") # print the 'name' attribute of the player-object.
        print(str(arr_players[cnt].typed), end=",") # print the 'typed' attribute of the player-object (whether computer-0 / human-1).
        print(str(arr_players[cnt].cnt_init), end=",") # print the 'cnt_init' attribute of the player-object ()
        print(str(arr_players[cnt].trr_and_frc), end=",") # print the 'territory and force' attribute of the player object ("territory_ID":"no_forces").
        print(str(arr_players[cnt].allies) + ")") # print the 'allies' attribute of the player-object (the ID-numbers of the allied-players).
    print("----") # separate from the next thing to be printed.


def print_arr_territories (arr_territories): # DEBUG FUNCTION
    print("BELOW IS ARR_TERRITORIES:") # signify what we'll be looking at below...
    for cnt in range(0, len(arr_territories), 1): # go through all of the territories, in the list of territories.
        print("(", end="") # print a single round-bracket, DO NOT move to the next line.
        print(str(arr_territories[cnt].id_num), end=",") # print the "ID-number" attribute of the territory-object.
        print(str(arr_territories[cnt].name), end=",") # print the 'name' (human-friendly) attribute of the territory-object.
        print(str(arr_territories[cnt].controller) + ")") # print the 'controller' attribute of the territory-object.



def init_players_arr(arr_players, arr_colors, arr_names, player_select, allies): # method for loading all players of the game
    human = int(player_select[0]) # the number of 'human' players is located in the 1st-cell of the 'player-select' list.
    comp = int(player_select[1]) # the number of 'computer' players is located in the 2nd-cell of the 'computer-select' list.
    #print("length of ARR_COLORS is: " + str(len(arr_colors)))
    for cnt in range(0, len(arr_colors), 1): # loop over the list of colors
        if (human > 0): # while there is still a count for 'human' players, then...
            arr_players.append(Player(arr_colors[cnt], 0, "", 1, 0, 0, 0)) # append to the list of players a 'human'-player object.
            human = int(human - 1) # we now have 1 less human player to create.
        else: # if we have no more 'human'-player objects to create, we'll create 'computer'-player objcets.
            arr_players.append(Player(arr_colors[cnt], 0, "", 0, 0, 0, 0)) # append to the list of players a 'computer'-player object.
            comp = int(comp - 1) # we now have 1 less computer player to create.
    #print("allies is: " + str(allies)) # debug print
    for cnt in range(0, len(arr_players), 1): # loop through the newly 'arr_players' that we've created.
        arr_players[cnt].assign_rgb() # give the player their colors, according to the specified order.
        arr_players[cnt].give_name(arr_names[cnt]) # use the 'give_name' class-method to assign the string as the name of the player.
        if (str(arr_players[cnt].id_num) in allies[0]): # if the id-number of the player was found in the first allies-group, then...
            #print("IN-1")
            arr_players[cnt].allies = allies[0] # assign the allies-numbering to the allies-attribute of the player-object.
        elif (str(arr_players[cnt].id_num) in allies[1]): # if the id-number of the player was found in the second allies-group, then...
            #print("IN-2")
            arr_players[cnt].allies = allies[1] # assign the allies-numbering to the allies-attribute of the player-object.
        elif (str(arr_players[cnt].id_num) in allies[2]):
            #print("IN-3")
            arr_players[cnt].allies = allies[2] # assign the allies-numbering to the allies-attribute of the player-object.
        else:
            #print("NOT IN :(")
            arr_players[cnt].allies.append(str(arr_players[cnt].id_num)) # append to the allies-list the id-num of the player (that's joining the allies)
    #print_arr_players(arr_players) # debug function


        

def print_arr_assign (arr_assign): # DEBUG FUNCTION
    print("BELOW IS ARR_ASSIGN:") # signify what we'll be looking at below...
    for cnt in range(0, len(arr_assign), 1): # loop over the list of available free-territories (territories that have YET to be assigned).
        print(arr_assign[cnt], end=",") # print the ID-number of the territory in the list of free-territories.
    print("----") # separate from the next thing to be printed.

def distance_two_dots(dot1, dot2): # method for calculating the distance between 2 dots.
    part1 = pow(dot2[1]-dot1[1], 2) # y2 - y1 # the subtraction between 'y' coordinates.
    part2 = pow(dot2[0]-dot1[0], 2) # x2 - x1 # the subtraction between 'x' coordinates.
    res = pow(part1 + part2, 0.5) # the actual distance between the dots.
    return res # return the actual distance between the dots.

def shortest_distance(my_dot, arr_territories): # method for determining the shortest distance between dots, and returns the ID number of the territory with shortest distance between the dots.
    selected = int(0) # the ID-of the selected territory is YET to be determined.
    dist = 10000 # the distance is initially set to be longer than possible (can only decrease from this number).
    for cnt1 in range(0, len(arr_territories), 1): # loop through the list of territories.
        for cnt2 in range(0, len(arr_territories[cnt1].dots), 1): # loop through the list of dots of a single territory-object
            temp = distance_two_dots((my_dot[0],my_dot[1]),(arr_territories[cnt1].dots[cnt2][0],arr_territories[cnt1].dots[cnt2][1])) # calculate the distance between the dot-of-mouse to the dot-of territory.
            if (temp < dist): # if the distance we've calcuated is shorted than that of the 'dist', then...
                dist = int(temp) # 'dist' gets the new distance, and the 'dist' can only get smaller (can only receive short distances).
                selected = (arr_territories[cnt1].id_num) # for now - get the ID-number of the territory whos' dot has (currently) the shortest distance.
                #print("ID IS: " + str(selected))
    return selected # return the ID-number of the territory with the shortest distance to where we've clicked with the mouse.

def all_colors_taken (arr_territories): # method for deterimining if all colors have been taken.
    for cnt in range(0, len(arr_territories), 1): # loop through all the territory-objects of the territory-list.
        if (arr_territories[cnt].controller == int(-1)): # if the territory has NOT been taken by any player yet, then...
            return 0 # return 0 - which means that we still need to assign some territories to players.
    return 1 # return 1 - if we scanned through the entire list, and all territories are assigned to players.

def one_comp_assign_color (arr_territories, arr_players, back_mode, screen, totals, cnt, lv2_gt, lv4_gt): # auto-assign one territory.
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
    lv2_gt.change_text(str(arr_players[cnt].name) + " is claiming territory") # change the text-value of the text-object (gui_text)
    lv2_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    lv4_gt.change_text(str(arr_players[cnt].cnt_init) + " remaining") # change the text-value of the text-object (gui_text)
    lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    rndm = random.randrange(totals[0], totals[1]+1) # randomly pick a territory from the list of all ID-numbers of all territories in the game-map.
    while (arr_territories[rndm-totals[0]].controller != int(-1)): # if the territory is already affiliated to a player.
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) ######
        rndm = random.randrange(totals[0], totals[1]+1) # 'rndm' is selected within the range of all territories
    arr_territories[rndm - totals[0]].controller = arr_players[cnt].id_num # the 'controller' attribute of the territory  gets the ID-number of the player.
    #print("in auto its: " + str(arr_territories[rndm - totals[0]].controller)) # debug function.
    arr_territories[rndm - totals[0]].force_no = int(1) # by default - a territory must have 1-force, in order to be claimed by some player.
    x = {str(rndm): 1} # the territory ('rndm') will have '1' force by default.
    arr_players[cnt].trr_and_frc.update(x) # add the new pair of key-value to the dictionary of "territories and forces".
    arr_territories[rndm - totals[0]].stick_blob() # apply the colored-PNG to the PyGame window.
    arr_territories[rndm - totals[0]].stick_force_no(0) # apply the text of number-of-forces onto the PyGame window.
    time.sleep(1) # make the program hold for 0.5 seconds
    lv2_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it) ######
    lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)

def one_human_assign_color (arr_territories, arr_players, back_mode, screen, totals, cnt, valid_color, lv2_gt, lv4_gt, lv7_gt): # single-manual assign of territory for a 'human' player.
    finished = int(0) # determines if the manual assign is finished.
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze) # clearing the event-cache (preventing from the PyGame window to freeze)
    lv2_gt.change_text(str(arr_players[cnt].name) + ",claim a territory") # change the text-value of the text-object (gui_text)
    lv2_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    lv4_gt.change_text(str(arr_players[cnt].cnt_init) + " remaining") # change the text-value of the text-object (gui_text)
    lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    while (finished == int(0)): # while we're not finished with the manual assignment.
        for event in pygame.event.get(): # get the pygame event.
            mouse = pygame.mouse.get_pos() # get the position (x,y) coordinates of the mouse.
            click = pygame.mouse.get_pressed() # get the boolean value for mouse-click.
            # click = list(click) # this idea has been dropped.
            color = screen.get_at(mouse) # get the RGB values in the position of the mouse.
            # x = pygame.mouse.get_rel()[0] # this idea has been dropped.
            # y = pygame.mouse.get_rel()[1] # this idea has been dropped.
            if (click[0] == int(1) and ((color[0] == valid_color[0]) and (color[1] == valid_color[1]) and (color[2] == valid_color[2]))): # if we've selected a territory - and NOT anywhere else in the background.
                id_selected = shortest_distance((mouse[0],mouse[1]),arr_territories) # get the ID of the selected territory (dots system).
                if (arr_territories[int(id_selected) - totals[0]].controller == int(-1)): # if the territory's controller is '-1' (not yet contolled by any player).
                    arr_territories[int(id_selected) - totals[0]].controller = arr_players[cnt].id_num # assign the controller of the territory to be the ID-number of the 'human'-player.
                    arr_territories[int(id_selected) - totals[0]].force_no = int(1) # the minimum forces requied for a player to control the territory is: 1 forces.
                    arr_players[cnt].trr_and_frc.update({str(id_selected): 1}) # update the dictionary of "territory and force" of the player - key:ID-of-territory, value:'1' forces.
                    arr_territories[int(id_selected) - totals[0]].stick_blob() # apply the colored PNG (blob) onto the PyGame window.
                    arr_territories[int(id_selected) - totals[0]].stick_force_no(0) # apply the number-of-forces text onto the screen.
                    finished = int(1) # we've finished the single manual assign
                    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()
                exit(0)
    lv2_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    pygame.display.update() # refresh the PyGame window.


def comp_manual_assign_one(arr_territories, arr_players, totals, cnt, lv2_gt, lv4_gt): # method for assigning a single force for a 'computer' player automatically (cannot be manual!)
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
    if (arr_players[cnt].cnt_init > 0): # while there are at-least 1 initial forces for the 'computer'-player.
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
        lv2_gt.change_text(str(arr_players[cnt].name) + " is deploying a territory") # change the text-value of the text-object (gui_text)
        lv2_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        lv4_gt.change_text(str(arr_players[cnt].cnt_init) + " remaining") # change the text-value of the text-object (gui_text)
        lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        id_selected = random.choice(list(arr_players[cnt].trr_and_frc.keys())) # from the dictionary of "territories and force", select a random territory, and assign it to "id_selected".
        arr_players[cnt].trr_and_frc[str(id_selected)] += 1 # add 1 force to the selected dictionary of "territories and forces".
        arr_players[cnt].cnt_init -= 1 # decrease the number of initial forces by 1, because 1 force had just been assigned.
        #print("arr_players[cnt].cnt_init: " + str(arr_players[cnt].cnt_init)) # debug function
        arr_territories[int(id_selected) - totals[0]].force_no += 1 # increase the number of forces of the selected territory by 1.
        arr_territories[int(id_selected) - totals[0]].stick_blob() # re-apply the colored blob of the owned territory.
        arr_territories[int(id_selected) - totals[0]].stick_force_no(0) # re-apply the text of the number-of-forces of the territory.
        time.sleep(1) # make the program hold for 0.5 seconds
        lv2_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)


def human_manual_assign_one(arr_territories, arr_players, totals, cnt, screen,lv2_gt,lv4_gt): # method for assigning a single force for a 'human' player manually ('human' players should assgin manually).
    if (arr_players[cnt].cnt_init > 0): # while there are at-least 1 initial forces for the 'human'-player.
        lv2_gt.change_text(str(arr_players[cnt].name) + ", deploy a territory") # change the text-value of the text-object (gui_text)
        lv2_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        lv4_gt.change_text(str(arr_players[cnt].cnt_init) + " remaining") # change the text-value of the text-object (gui_text)
        lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        #print("You have: " + str(arr_players[cnt].cnt_init) + "forces left.") # print-to-CLI how many initial forces are left to manually assign.
        finished = int(0) # determines if the manual assign is finished.
        while (finished == int(0)): # while we're not finished with the manual assignment.
            for event in pygame.event.get(): # get the PyGame event.
                mouse = pygame.mouse.get_pos() # get the mouse positions.
                click = pygame.mouse.get_pressed() # get the boolean value for mouse-click.
                color = screen.get_at(mouse) # get the RGB value of the pixel of the position of the mouse.
                y = screen.get_size()[1] # get the length of the PyGame window
                # print("the color is: " + str(color)) # debug print
                if (click[0] == int(1) and (color[2] != 0) and (color[2] != 255) and (mouse[1] < (y-200))): # if we've clicked the left-mouse button, then...
                    id_selected = shortest_distance((mouse[0],mouse[1]),arr_territories) # get the ID of the selected territory (dots system).
                    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
                    if (str(id_selected) in arr_players[cnt].trr_and_frc): # if id_selected exists in that dictionary...
                        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
                        #print("id_selected is: " + str(id_selected)) # debug print
                        for run in range(0, len(arr_players), 1): # loop over the list of player-objects
                            if (str(id_selected) in arr_players[run].trr_and_frc):
                                arr_players[run].trr_and_frc[str(id_selected)] += 1
                        arr_players[cnt].trr_and_frc[str(id_selected)] += 1 # in the dictionary of "territory and force" - in the pair of the selected territory - increment the number of forces by 1.
                        arr_territories[int(id_selected)-totals[0]].force_no += 1 # in the 'force-no' attribute of the territory-object - increment the number of forces by 1.
                        arr_territories[int(id_selected)-totals[0]].stick_blob() # re-apply the colored-PNG (blob) onto the PyGame window.
                        arr_territories[int(id_selected)-totals[0]].stick_force_no(1) # re-apply the force-number text onto the PyGame window.
                        arr_territories[int(id_selected)-totals[0]].controller = int(arr_players[cnt].id_num)
                        arr_players[cnt].cnt_init -= 1 # decrease the initial-forces by one (because a force has just been used).
                        finished = int(1) # we've finished the single manual assign
                        time.sleep(1) # make the program hold for 0.3 seconds
                        arr_territories[int(id_selected)-totals[0]].stick_blob() # re-apply the colored-PNG (blob) onto the PyGame window.
                        arr_territories[int(id_selected)-totals[0]].stick_force_no(0) # re-apply the force-number text onto the PyGame window.
                if (event.type == pygame.QUIT):
                    pygame.display.quit()
                    pygame.quit()
                    exit(0)
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
        time.sleep(1) # make the program hold for 0.5 seconds
        lv2_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)



def manual_assign_colors (arr_territories, arr_players, back_mode, screen, totals, gui_text_levels, lv1_gt, lv2_gt, lv4_gt, lv7_gt): # method for manually assigning the territories to ALL player ('humans' and 'computers').
    cont = finished_manual_color_assign(arr_territories) # determines if should continue with the manual assign.
    valid_color = valid_click_color_assign(back_mode) # determine the valid color with the function 'valid_click_color_assign'.
    while (cont == int(1)): # while we can still continue with the manual assign.
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
        for cnt in range(0, len(arr_players), 1): # loop over all players in the player-list
            if (arr_players[cnt].cnt_init > 0): # if the count of initial-forces is more than 0, then...
                lv1_gt.change_text("CLAIM") # change the text-value of the text-object (gui_text)
                lv1_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                if (arr_players[cnt].typed == int(0)): # 0=COMP
                    one_comp_assign_color(arr_territories, arr_players, back_mode, screen, totals, cnt, lv2_gt, lv4_gt) # assign a single initial-territory to a computer-player (automatically)
                    arr_players[cnt].cnt_init -= 1 # decrease the count of initial-territories to claim by 1
                else: # 1=HUMAN
                    one_human_assign_color(arr_territories, arr_players, back_mode, screen, totals, cnt, valid_color, lv2_gt, lv4_gt, lv7_gt) # assign a single initial-territory to a human-player (manually)
                    arr_players[cnt].cnt_init -= 1 # decrease the count of initial-territories to claim by 1
                lv1_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        cont = finished_manual_color_assign(arr_territories) # determine if all territories have been assigned
        lv1_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                

                        
def manual_assign_init_forces (arr_territories, arr_players, back_mode, screen, totals, gui_text_levels, lv1_gt, lv2_gt, lv4_gt): # method for manually assignint initial forces.
    cont = int(1) # determines if the function shoudl continue.
    while (cont == int(1)): # while we can still manually assign forces, then...
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
        for cnt in range(0, len(arr_players), 1): # loop over the list of players.
            # print("The type is: " + str(arr_players[cnt].typed)) # debug print
            if (arr_players[cnt].cnt_init > 0): # if the count of the initial-force-count is greater than 0, then...
                lv1_gt.change_text("DEPLOY") # change the text-value of the text-object (gui_text)
                lv1_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                if (arr_players[cnt].typed == int(0)): # 0 = COMP # if the player-type is "computer", then...
                    comp_manual_assign_one(arr_territories, arr_players, totals, cnt, lv2_gt, lv4_gt) # call "auto-assign" method.
                    # print("finished comp single-manual-assign") # debug print
                else: # 1 = HUMAN # if the player-type is 'human', then...
                    human_manual_assign_one(arr_territories, arr_players, totals, cnt, screen, lv2_gt, lv4_gt) # call "manual-assign" method.)
                cont = finished_manual_force_assign(arr_players) # determine if 'manual-assign' should continue.
                lv1_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                    # print("finished human single-manual-assign") # debug print
                # print("The 'cont' is: " + str(cont)) # debug print

def valid_click_color_assign (back_mode): # function to determine the valid color of an empty territory (a territory that has not been claimed yet)
    if (back_mode == int(0)): #0=DARK
        return (0,0,1) # a color that's very close to be 'pure-black', but isn't actually pure-black
    else: # 1=LIGHT
        return (255,255,254) # a color that very close to be 'pure-white', but itn't actually pure-white
    

def finished_manual_color_assign (arr_territories): # method to determine if all territories have been claimed by players (in start of the game)
    for cnt in range(0, len(arr_territories), 1): # loop through all the territories.
        if (arr_territories[cnt].controller == int(-1)): # if we found a territory that is YET to be assigned to a player, then...
            # print("The returned is: 1") # debug print
            return 1 # yes - we shall continue manual assign, because not all territories belong to players.
    #for cnt in range(0, len(arr_territories), 1): # looop through all the territories
        #print(str(arr_territories[cnt].controller), end=",") # debug print
    # print("The returned is: 0") # debug print
    return 0 # all territories are controlled by players - so finished manual assign of colors.

def finished_manual_force_assign (arr_players): # method to determine if all players have finished assigning their initial count of forces.
    for cnt in range(0, len(arr_players), 1): # loop over the list of players.
        if (arr_players[cnt].cnt_init > int(0)): # if at-least one player DID-NOT finish assigning their initial count of forces.
            return 1 # return 1 - we have to continue to allow the players to manual assign initial forces.
    return 0 # otherwise - if all players finished assigning their initial forces - return 0.

def define_init_cnt(arr_players): # define the intial count of forces of each of the players.
    for cnt in range(0, len(arr_players), 1): # loop over the list of players.
        arr_players[cnt].get_cnt_init() # call the method for receiving the initial count.

def comp_fortify_one (cnt, arr_players, arr_territories, totals, fortify_cnt, lv4_gt): # function to allow a computer-player to fortify a single force onto a random owned-territory
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
    cnt = int(cnt) # stabilize the 'cnt' value to be an integer
    id_selected = random.choice(list(arr_players[cnt].trr_and_frc.keys())) # select a random territory from the dictionary of owned territories
    for run in range(0, len(arr_players), 1): # 
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
        if (str(id_selected) in arr_players[run].trr_and_frc):
            arr_players[cnt].trr_and_frc[str(id_selected)] += 1 # add 1 force to the dictionary of "territories and forces" with the matching id-number of the selected territory
    #arr_players[cnt].cnt_init -= 1
    arr_territories[int(id_selected) - totals[0]].force_no += 1 # increase the force-count (this time - in the 'territory' class).
    arr_territories[int(id_selected) - totals[0]].stick_blob() # apply the 'blob' (colored PNG) onto the PyGame window.
    arr_territories[int(id_selected) - totals[0]].stick_force_no(1) # apply the force-number onto the PyGame window.
    time.sleep(1) # make the program hold for 0.5 seconds
    fortify_cnt = int(fortify_cnt - 1) # decrease number of fortify-forces by 1 (because the computer-player had just utilized a single force).
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
    time.sleep(1)
    arr_territories[int(id_selected) - totals[0]].stick_blob() # apply the 'blob' (colored PNG) onto the PyGame window.
    arr_territories[int(id_selected) - totals[0]].stick_force_no(0) # apply the force-number onto the PyGame window.
    return fortify_cnt # return the new count of forces remaining for fortification

def human_auto_fortify (cnt, arr_players, arr_territories, totals, fortify_cnt, lv4_gt, screen): # function to automatically fortify all forces for a human-player
    #print("HUMAN FORTIFY CNT") # debug print
    while (fortify_cnt > 0): # while there are some forces remaining for fortification, then...
        rndm = random.choice(list(arr_players[cnt].trr_and_frc.keys())) # select a random territory from the dictionary of "territory and forces" of the human-player
        arr_territories[int(rndm) - totals[0]].force_no += 1 # add a single force(in the 'territory' class)
        arr_players[cnt].trr_and_frc[str(rndm)] += 1 # add a single force to the dictionary of "territory and force" (where the ID matches the random selection)
        arr_territories[int(rndm) - totals[0]].stick_blob() # apply the 'blob' (colored PNG) onto the PyGame window.
        arr_territories[int(rndm) - totals[0]].stick_force_no(1) # apply the 'force-no' onto the PyGame window.
        lv4_gt.remove_gui_text()
        lv4_gt.change_text(str(fortify_cnt) + " remaining")
        lv4_gt.insert_gui_text(arr_players[cnt].color)
        fortify_cnt -= 1 # decrease the amount of forces to fortify by 1 (because 1 force was previously utilized).
        time.sleep(0.85)
        arr_territories[int(rndm) - totals[0]].stick_blob() # apply the 'blob' (colored PNG) onto the PyGame window.
        arr_territories[int(rndm) - totals[0]].stick_force_no(0) # apply the 'force-no' onto the PyGame window.
    return fortify_cnt # return the number of forces (will always be 0 - because it's after the end of the while-loop)



def human_fortify_one (back_mode, cnt, arr_players, arr_territories, totals, fortify_cnt, screen, gui_text_levels, lv4_gt, lv7_gt):
    pygame.display.update()
    #print("I'm in... human_fortify_one")
    cnt = int(cnt) # stabilize the value of 'cnt' to be an integer
    finished = int(0) # while we did not finished yet
    while (finished == int(0)): # while the fortification is not finished yet, then...
        auto_button = Button(1, "AUTO", back_mode, (gui_text_levels[12][0],gui_text_levels[12][1],140,50), 5, 1, 0, screen) # create an 'AUTO' button (for automatic fortification)
        for event in pygame.event.get(): # get the PyGame event
            mouse = pygame.mouse.get_pos() # get the mouse position
            click = pygame.mouse.get_pressed() # get the click Boolean value
            color = screen.get_at(mouse) # get the color of the pixel that is currently being pointed by the mouse
            y = screen.get_size()[1] # get the length of the PyGame window.
            finished = auto_button.button_functional(finished) # initialize functionality of the "AUTO"-button.
            if (finished == int(1) and fortify_cnt > 0): # if the 'AUTO' button has been pressed, and there are some forces left for fortification, then...
                fortify_cnt = human_auto_fortify(cnt, arr_players, arr_territories, totals, fortify_cnt, lv4_gt, screen) #auto fortify all remaining forces for fortification
                return fortify_cnt # return the amount of forces left for fortification
            if (click[0] == int(1) and (color[2] != 0) and (color[2] != 255) and (mouse[1] < (y-200))): # if there was a left mouse click AND the blue value is niether 0 nor 255 AND the position of the mouse is somewhere above the communication panel, then...
                #print("Still alive!   4") # debug function
                id_selected = shortest_distance((mouse[0],mouse[1]),arr_territories) # determine the clicked territory with the "dot-system".
                #print("id_selected is: " + str(id_selected)) # debug function
                pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
                if (str(id_selected) in arr_players[cnt].trr_and_frc): # if the id-number of the selected territory is within the dictionary of "territory and force" of the current-player, then...
                    arr_players[cnt].trr_and_frc[str(id_selected)] += 1 # add 1 force to the dictionary of "territory and force" of the current-player.
                    #arr_players[cnt].trr_and_frc[id_selected] += 1 # in the dictionary of "territory and force" - in the pair of the selected territory - increment the number of forces by 1.
                    #print("id_selected is: " + str(id_selected))
                    arr_territories[int(id_selected)-totals[0]].force_no += 1 # in the 'force-no' attribute of the territory-object - increment the number of forces by 1.
                    arr_territories[int(id_selected)-totals[0]].stick_blob() # re-apply the colored-PNG (blob) onto the PyGame window.
                    arr_territories[int(id_selected)-totals[0]].stick_force_no(1) # re-apply the force-number text onto the PyGame window.
                    #arr_players[cnt].cnt_init -= 1 # decrease the initial-forces by one (because a force has just been used).
                    fortify_cnt = int(fortify_cnt - 1) # decrease the number of remaining forces to fortify by 1
                    time.sleep(0.75) # make the program hold for 0.65 seconds
                    lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                    finished = int(1) # we've finished the single manual assign
                    arr_territories[int(id_selected)-totals[0]].stick_blob() # re-apply the colored-PNG (blob) onto the PyGame window.
                    arr_territories[int(id_selected)-totals[0]].stick_force_no(0) # re-apply the force-number text onto the PyGame window.
                    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
                elif (str(id_selected) not in arr_players[cnt].trr_and_frc):
                    lv7_gt.change_text("cannot fortify to foreign territory!")
                    lv7_gt.insert_gui_text(back_mode)
                    time.sleep(1)
                    lv7_gt.remove_gui_text()
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()
                exit(0)
    return fortify_cnt # return the amount of forces to fortify that are remaining.


def fortify (back_mode, cnt, arr_players, arr_territories, totals, gui_text_levels, screen, lv1_gt, lv2_gt, lv4_gt, lv7_gt): # function for fortifying forces of player. It serves both human-players AND computer-players.
    lv1_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv2_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    #print("Before gui_text") # debug print
    fortify_cnt = calculate_fortify (cnt, arr_players, totals) # method for calculating how many forces can this player fortify, with the given circumstances.
    lv1_gt.change_text("FORTIFY") # change the text-value of the text-object (gui_text)
    if (arr_players[cnt].typed == int(0)): # 0=COMP
        lv2_gt.change_text(str(arr_players[cnt].name) + " is fortifying territories") # change the text-value of the text-object (gui_text)
    else: # 1=HUMAN
        lv2_gt.change_text(str(arr_players[cnt].name) + ", fortify owned territories") # change the text-value of the text-object (gui_text)
    lv4_gt.change_text(str(fortify_cnt) + " remaining") # change the text-value of the text-object (gui_text)

    lv1_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    lv2_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.

    cnt = int(cnt) # stabilize the 'cnt' variable into an integer.
    while (fortify_cnt > 0): # while there are still forces to fortify, then...
        #print("The type is: " + str(arr_players[cnt].typed))
        if (arr_players[cnt].typed == int(0)): # 0=COMP
            #print("GOT TO: fortify_computer") # debug print
            fortify_cnt = comp_fortify_one(cnt, arr_players, arr_territories, totals, fortify_cnt, lv4_gt) # the "fortification-function" for computer-players
            lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
            lv4_gt.change_text(str(fortify_cnt) + " remaining") # change the text-value of the text-object (gui_text)
            lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        else: # 1=HUMAN
            #print("GOT TO: fortify_human") # debug print
            fortify_cnt = human_fortify_one(back_mode, cnt, arr_players, arr_territories, totals, fortify_cnt, screen, gui_text_levels, lv4_gt, lv7_gt) # the "fortification-function" for human-players
            #print_arr_players(arr_players) # debug print
            lv4_gt.change_text(str(fortify_cnt) + " remaining") # change the text-value of the text-object (gui_text)
            lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    lv1_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv2_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)

def comp_attack (back_mode, cnt, arr_players, arr_territories, totals, screen, gui_text_levels,lv2_gt, lv3_gt, lv5_gt, lv6_gt, lv7_gt, lv8_gt, lv9_gt): # function to allow the computer-players to attack
    pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
    if (able_attack(arr_players, cnt)): # of the computer is able to attack (validation from the 'able_attack' function is required), then...
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
        attack_type = int(0) # the attack_type (either single / auto), '0' = 'not yet selected'
        id_src = int(-1) # the attacking territory is not yet selected, no ID is ever equal to '-1'.
        id_dst = int(-1) # the attacked territory is not yet selected, not ID is ever equal to '-1'.
        lv3_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv3_gt.change_text(str(arr_players[cnt].name) + " is slct. attacking territory!") # change the text-value of the text-object (gui_text)
        lv3_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        while (id_src == int(-1)): # while the attakcing territory is NOT yet selected, then...
            pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
            id_src = random.choice(list(arr_players[cnt].trr_and_frc)) # select a random ID number from the dictionary of "territory and force" of the current player
            while (arr_territories[int(id_src) - totals[0]].force_no == int(1)): # if the number of forces in the selected-attacking territory is 1, it's NOT valid, therefore - need to reselect
                pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
                id_src = random.choice(list(arr_players[cnt].trr_and_frc)) # reselecting a territory (because the previous selected territory had only 1 force - not enough to conduct an attack)
        lv6_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv6_gt.change_text("ATTACKER: " + str(arr_territories[int(id_src) - totals[0]].name))
        lv6_gt.insert_gui_text(arr_players[cnt].color)
        lv5_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv5_gt.change_text(str(arr_players[cnt].name) + " is slct. attacked territory!") # change the text-value of the text-object (gui_text)
        lv5_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        while (id_dst == int(-1)):  # while the attacked territory is NOT yet selected, then...
            pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
            id_dst = random.choice(arr_territories[int(id_src) - totals[0]].borders) # select a random ID number from the list of of territory-objects
            while (str(arr_territories[int(id_dst) - totals[0]].controller) in arr_players[cnt].allies): # while the selected territory belongs to an allied player, then it's not a good selection, therefore needs to be reselected.
                pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
                id_dst = str(random.choice(arr_territories[int(id_src) - totals[0]].borders)) # reselecting an attacked territory
                if (random.randint(0,100) < 7): # 30% change it'll quit the function
                    continue_attack = int(0) # discontinue the attack
                    return continue_attack # return the value of the 'continue_attack' (specifically - to discontinue attack)
        lv9_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv9_gt.change_text("ATTACKED: " + str(arr_territories[int(id_dst) - totals[0]].name)) # change the text-value of the text-object (gui_text)
        lv9_gt.insert_gui_text(determine_color(arr_territories[int(id_dst) - totals[0]].controller)) # PROBLEM
        attack_type = random.randrange(2, 3) # selection between a single-attack and an auto-attack
        if (attack_type == int(1)): # if the attack_type is 'single-attack', then...
            single_attack(back_mode, id_src, id_dst, cnt, arr_players, arr_territories, totals, screen, gui_text_levels)
        elif (attack_type == int(2)): # if the attack_type is 'auto-attack', then...
            #print("Before auto attack:")
            #print_arr_players(arr_players)
            auto_attack(back_mode, id_src, id_dst, cnt, arr_players, arr_territories, totals, screen, gui_text_levels)
            #print("After auto attack:")
            #print_arr_players(arr_players)
        attack_type = int(-1) # neutralize the attack-type, so it'll get reselected for the next attack.
        time.sleep(2) # make the program hold for 2 seconds
        if (random.randint(0,100) < 30): # 30% change it'll quit the function
            continue_attack = int(0) # discontinue the attack
            return continue_attack # return the value of the 'continue_attack' (specifically - to discontinue attack)
        lv3_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv5_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv6_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv9_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)


            
def human_attack (back_mode, cnt, arr_players, arr_territories, totals, screen, gui_text_levels, lv3_gt, lv4_gt, lv5_gt, lv6_gt, lv7_gt, lv8_gt, lv9_gt): # function to allow a human-player to attack
    cnt = int(cnt) # stabilize the 'cnt' variable to be an integer
    attack_type = int(0) # 0=not-attacking / 1=manual / 2=auto
    continue_attack = able_attack(arr_players, cnt) # determine if attack should continue
    while (continue_attack == int(1)): # if the attack is continued, then...
        manual_button = Button(1, "MANUAL", back_mode, (gui_text_levels[11][0],gui_text_levels[11][1],140,50), 5, 1, 0, screen) # initiate the "auto" button.
        auto_button = Button(1, "AUTO", back_mode, (gui_text_levels[9][0],gui_text_levels[9][1],140,50), 5, 2, 0, screen) # initiate the "auto" button.
        skip_button = Button(1, "SKIP", back_mode, (gui_text_levels[12][0],gui_text_levels[12][1],140,50), 5, 0, 0, screen) # initiate the "skip" button.
        id_src = int(-1) # neutralize the selected source territory
        id_dst = int(-2) # neutralize the selected destination territory
        lv3_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv3_gt.change_text(str(arr_players[cnt].name) + ", slct. attacking territory!") # change the text-value of the text-object (gui_text)
        lv3_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        if (continue_attack == int(0)): # if the attack is discontinued, then...
            return 0 # return '0' (to the general 'attack' function)
        while (id_src == int(-1) and (id_dst == int(-2) or id_dst == int(-1))): # while none of the source-territory nor destination-territory are selected, then...
            while (id_src == int(-1)): # while the source territory has not been selected, then...
                for event in pygame.event.get(): # get the PyGame event.
                    mouse = pygame.mouse.get_pos() # get the mouse position
                    click = pygame.mouse.get_pressed() # get the Boolean value of the mouse-click
                    color = screen.get_at(mouse) # get the color of the pixel of the current location of the mouse
                    y = screen.get_size()[1] # get the length of the PyGame window.
                    continue_attack = skip_button.button_functional(continue_attack) # initiate functionality of the "skip" button.
                    if (continue_attack == int(0)): # if the attack is discontinued, then...
                        return 0 # return '0' (to the general 'attack' function)
                    if ((click[0] == int(1)) and (color[2] != 0) and (color[2] != 255) and (mouse[1] < (y-200))): # if clicked the left-mouse button, and blue value is niether 0 nor 255, and if the mouse is NOT over the 'communication-panel', then...
                        id_selected = shortest_distance((mouse[0],mouse[1]),arr_territories) # get the selected territory with the "dot-system".
                        #print("totals[0] is: " + str(totals[0])) # debug function
                        if (arr_territories[int(id_selected) - totals[0]].controller == int(arr_players[cnt].id_num) and (arr_territories[id_selected - totals[0]].force_no > 1)): # if the selected territory is controlled by the player, then...
                            id_src = int(id_selected) # assign the id-number of the selected territory as the source-territory.
                            lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                            lv6_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                            lv6_gt.change_text("ATTACKER: " + str(arr_territories[id_src - totals[0]].name)) # change the text-value of the text-object (gui_text)
                            lv6_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                            lv5_gt.change_text(str(arr_players[cnt].name) + ", slct. territory to attack!") # change the text-value of the text-object (gui_text)
                            lv5_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                            lv4_gt.change_text("right-click to release") # change the text-value of the text-object (gui_text)
                            lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                            break # the function can move onto selected the attacked territory.
                        elif ((arr_territories[int(id_selected) - totals[0]].controller != int(arr_players[cnt].id_num)) and (arr_territories[id_selected - totals[0]].force_no > 1)):
                            lv6_gt.change_text("attacking territory must be owned!")
                            lv6_gt.insert_gui_text(back_mode)
                            time.sleep(1)
                            lv6_gt.remove_gui_text()
                        elif (arr_territories[id_selected - totals[0]].force_no == 1):
                            lv6_gt.change_text("attacking territory must have at-least 2 forces!")
                            lv6_gt.insert_gui_text(back_mode)
                            time.sleep(1)
                            lv6_gt.remove_gui_text()
                    if (event.type == pygame.QUIT):
                        pygame.display.quit()
                        pygame.quit()
                        exit(0)
            id_dst = int(-1) # neutralize the selected destination territory
            while (id_dst == int(-1)): # while the destination-territory has not been selected yet, then...
                #print("here 3") # debug print.
                for event in pygame.event.get(): # get the PyGame event.
                    mouse = pygame.mouse.get_pos() # get the mouse position
                    click = pygame.mouse.get_pressed() # get the Boolean value of the mouse-click
                    color = screen.get_at(mouse) # get the color of the pixel of the current location of the mouse
                    y = screen.get_size()[1] # get the length of the PyGame window.
                    continue_attack = skip_button.button_functional(continue_attack)
                    #print("continue_attack is: " + str(continue_attack)) # debug print
                    if (continue_attack == int(0)): # if the attack is discontinued, then...
                        return 0 # return '0' (to the general 'attack' function)
                    if (click[0] == int(1) and (color[2] != 0) and (color[2] != 255) and (mouse[1] < (y-200))): # if clicked the left-mouse button, and blue value is niether 0 nor 255, and if the mouse is NOT over the 'communication-panel', then...
                        attack_type = int(0) # neutralize the type of the attack
                        id_selected = shortest_distance((mouse[0],mouse[1]),arr_territories) # determine the selected territory with the "dot-system".
                        if ((str(arr_territories[int(id_selected) - totals[0]].controller) not in arr_players[cnt].allies) and (arr_territories[int(id_selected) - totals[0]].controller != int(arr_players[cnt].id_num)) and (id_selected in arr_territories[id_src - totals[0]].borders)): # allies? # PROBLEM - " type 'int' is not iterable "
                            id_dst = int(id_selected)  # assign the id-number of the selected territory as the destination-territory.
                            #print("the presumed color is: " + str(arr_territories[id_dst - totals[0]].controller))
                            lv9_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                            lv9_gt.change_text("ATTACKED: " + str(arr_territories[int(id_dst) - totals[0]].name)) # change the text-value of the text-object (gui_text)
                            #print("the id_dst is: " + str(id_dst)) # debug print
                            #print("the totals[0] is: " + str(totals[0])) # debug print
                            #print("The weird thing is: " + str(int(id_dst) - totals[0])) # debug print
                            #print("THE TERRITORY IS: ") # debug print
                            lv9_gt.insert_gui_text(determine_color(arr_territories[int(id_dst) - totals[0]].controller)) # PROBLEM
                        elif (arr_territories[int(id_selected) - totals[0]].controller == int(arr_players[cnt].id_num)):
                            lv9_gt.change_text("cannot attack owned territories!")
                            lv9_gt.insert_gui_text(back_mode)
                            time.sleep(1)
                            lv9_gt.remove_gui_text()
                        elif (str(arr_territories[int(id_selected) - totals[0]].controller) in arr_players[cnt].allies):
                            lv9_gt.change_text("cannot attack your allies!")
                            lv9_gt.insert_gui_text(back_mode)
                            time.sleep(1)
                            lv9_gt.remove_gui_text()
                        elif (id_selected not in arr_territories[id_src - totals[0]].borders):
                            lv9_gt.change_text("cannot attack none-bordering territory!")
                            lv9_gt.insert_gui_text(back_mode)
                            time.sleep(1)
                            lv9_gt.remove_gui_text()
                    if (click[2] == int(1)): # if the selected ATTACKING territory is deselected, then...
                        #print("Please select another territory") # print-to-CLI the message (that the player should select another ATTACKING territory).
                        id_src = int(-1) # neutralize the selected ATTACKING territory.
                        id_dst = int(-2) # neutralize the selected ATTACKED territory.
                        lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                        lv5_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                        lv6_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                        lv9_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                    if (event.type == pygame.QUIT):
                        pygame.display.quit()
                        pygame.quit()
                        exit(0)
        while (id_src >= 0 and id_dst >= 0): # if BOTH source-territory and destination-territory have been selected, then...
            #print("here 4") # debug print
            for event in pygame.event.get(): # get the PyGame event
                continue_attack = skip_button.button_functional(continue_attack) # initialize functionality of the skip-button
                mouse = pygame.mouse.get_pos() # get the position of the mouse
                click = pygame.mouse.get_pressed() # get the Boolean value of the mouse-click 
                attack_type = auto_button.button_functional(attack_type) # initialize funcionality of the auto-button
                attack_type = manual_button.button_functional(attack_type) # initialize functionality of the manual-button
                if (continue_attack == int(0)): # if the attack is discountinued, then...
                    return 0 # return '0' (to the general 'attack' function)
                if (click[2] == int(1)): # if the selected ATTACKING territory is deselected, then...
                    #print("Please select another territory") # print-to-CLI the message (that the player should select another ATTACKING territory).
                    id_src = int(-1) # neutralize the selected ATTACKING territory.
                    id_dst = int(-2) # neutralize the selected ATTACKED territory.
                    lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                    lv5_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                    lv6_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                    lv9_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                    break # move onto the attack-type.
                if (event.type == pygame.QUIT):
                    pygame.display.quit()
                    pygame.quit()
                    exit(0)
                if (attack_type == int(1) and (arr_territories[id_src - totals[0]].force_no > 1) and (arr_territories[id_dst - totals[0]].controller != arr_players[cnt].id_num)): # if the attack type is manual AND the number of forces of the attacking territory is at-least 1 AND the attacked territory does NOT belong to the attacking player, then...
                    #print("Number of my forces is: " + str(arr_territories[id_src - totals[0]].force_no))
                    single_attack(back_mode, id_src, id_dst, cnt, arr_players, arr_territories, totals, screen, gui_text_levels) # start the single-attack (with the function call)
                    attack_type = int(0) # neutralize the attack-type
                    #print_arr_players(arr_players) # debug print
                elif (attack_type == int(2) and (arr_territories[id_src - totals[0]].force_no > 1) and (arr_territories[id_dst - totals[0]].controller != arr_players[cnt].id_num)): # if the attack type is auto AND the number of forces of the attacking territory is at-least 1 AND the attacked territory does NOT belong to the attacking player, then...
                    auto_attack(back_mode, id_src, id_dst, cnt, arr_players, arr_territories, totals, screen, gui_text_levels) # start the auto-attack (with the function call)
                    attack_type = int(0) # neutralize the attack-type
                    #print_arr_players(arr_players) # debug print
    return 0 # return '0' (to the general 'attack' function)

def auto_attack (back_mode, id_src, id_dst, cnt, arr_players, arr_territories, totals, screen, gui_text_levels): # function to allow automatic attack (it ends when either all attacking forces drop to 1 OR when capture attacked territory)
    pygame.display.update()
    cnt = int(cnt) # stabilize the 'cnt' variable to an integer.
    finished = int(0) # the finished is '0' - which means NOT finished
    clr_atk = determine_color(arr_territories[int(id_src) - totals[0]].controller) # determine the color of the attacking-player
    clr_def = determine_color(arr_territories[int(id_dst) - totals[0]].controller) # determine the color of the attacked-player
    while ((arr_territories[int(id_src) - totals[0]].force_no > 1) and (finished == int(0))): # while the number of territories of the attacker is greater than 1 (able to attack) AND the attack is not yet finished, then...
        arr_territories[int(id_src) - totals[0]].stick_blob() # re-apply the colored-png (blob)
        arr_territories[int(id_src) - totals[0]].stick_force_no(2) # re-apply the number-of-forces (text)
        arr_territories[int(id_dst) - totals[0]].stick_blob() # re-apply the colored-png (blob)
        arr_territories[int(id_dst) - totals[0]].stick_force_no(3) # re-apply the number-of-forces (text)
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
        atk_roll = single_dice_roll() # the dice roll of the attacker # CHANGE
        def_roll = single_dice_roll() # the dice roll of the defender
        stick_dice(atk_roll, gui_text_levels[6], clr_atk, cnt, screen) # apply the dice-icon onto the screen
        stick_dice(def_roll, gui_text_levels[7], clr_def, cnt, screen) # apply the dice-icon onto the screen
        if (atk_roll > def_roll): # if the roll of the attacker is greater than the roll of the defender
            arr_territories[int(id_dst) - totals[0]].force_no -= 1 # decrease number of territories of the attacked territory by 1
            for run in range(0, len(arr_players), 1): # loop over the list of player-objects
                if (str(id_dst) in arr_players[run].trr_and_frc): # if the destination territory is found in the dictionary of "territory and force", then...
                    arr_players[run].trr_and_frc[str(id_dst)] -= 1 # decrease the number of forces by 1
            finished = territory_capture(cnt, id_src, id_dst, arr_players, arr_territories, totals, screen) # determine if there was a conquest
            if (finished == int(1)): # if the attack has finished, then...
                time.sleep(1)
                arr_territories[int(id_src) - totals[0]].stick_blob() # re-apply the colored-png (blob)
                arr_territories[int(id_src) - totals[0]].stick_force_no(0) # re-apply the number-of-forces (text)
                arr_territories[int(id_dst) - totals[0]].stick_blob() # re-apply the colored-png (blob)
                arr_territories[int(id_dst) - totals[0]].stick_force_no(0) # re-apply the number-of-forces (text)
                break # moving out of this section
        else: # if the roll of the defender is greater / equals to the roll of the attacker
            arr_territories[int(id_src) - totals[0]].force_no -= 1 # decrease the number of forces of attacking territory by 1
            for run in range(0, len(arr_players), 1):
                if (arr_players[run].id_num == arr_territories[int(id_src) - totals[0]].controller):
                    arr_players[run].trr_and_frc[str(id_src)] -= 1
        time.sleep(1)
        arr_territories[int(id_src) - totals[0]].stick_blob() # re-apply the colored-png (blob)
        arr_territories[int(id_src) - totals[0]].stick_force_no(0) # re-apply the number-of-forces (text)
        arr_territories[int(id_dst) - totals[0]].stick_blob() # re-apply the colored-png (blob)
        arr_territories[int(id_dst) - totals[0]].stick_force_no(0) # re-apply the number-of-forces (text)
        time.sleep(1) # make the program hold for 0.8 seconds
        remove_dice(gui_text_levels[6][0],gui_text_levels[6][1], back_mode, screen) # remove the dice-icon from the PyGame window.
        remove_dice(gui_text_levels[7][0],gui_text_levels[7][1], back_mode, screen) # remove the dice-icon from the PyGame window.
    time.sleep(1.5) # make the program hold for 0.8 seconds
    remove_dice(gui_text_levels[6][0],gui_text_levels[6][1], back_mode, screen) # remove the dice-icon from the PyGame window.
    remove_dice(gui_text_levels[7][0],gui_text_levels[7][1], back_mode, screen) # remove the dice-icon from the PyGame window.

def stick_dice(num, gui_text_levels, color, cnt, screen): # function to determine which dice-icon to stick onto the PyGame window.
    cnt = int(cnt) # stabilize the 'cnt' variable into an integer.
    if (num == int(1)): # if the randomized dice-roll is 1, then...
        one_valued_dice(gui_text_levels[0],gui_text_levels[1], color, screen) # apply the one-valued-dice icon onto the PyGame window.
    elif (num == int(2)): # if the randomized dice-roll is 2, then...
        two_valued_dice(gui_text_levels[0],gui_text_levels[1], color, screen) # apply the two-valued-dice icon onto the PyGame window.
    elif (num == int(3)): # if the randomized dice-roll is 3, then...
        three_valued_dice(gui_text_levels[0],gui_text_levels[1], color, screen) # apply the three-valued-dice icon onto the PyGame window.
    elif (num == int(4)): # if the randomized dice-roll is 4, then...
        four_valued_dice(gui_text_levels[0],gui_text_levels[1], color, screen) # apply the four-valued-dice icon onto the PyGame window.
    elif (num == int(5)): # if the randomized dice-roll is 5, then...
        five_valued_dice(gui_text_levels[0],gui_text_levels[1], color, screen) # apply the five-valued-dice icon onto the PyGame window.
    elif (num == int(6)): # if the randomized dice-roll is 6, then...
        six_valued_dice(gui_text_levels[0],gui_text_levels[1], color, screen) # apply the six-valued-dice icon onto the PyGame window.
        
def determine_color (num):
    if (num == int(0)): # color at position 0
        return (34,139,34) # green
    elif (num == int(1)): # color at position 1
        return (0,95,190) # blue
    elif (num == int(2)): # color at position 2
        return (251,219,3) # yellow
    elif (num == int(3)): # color at position 3
        return (251,28,46) # red
    elif (num == int(4)): # color at position 4
        return (255,102,0) # orange
    elif (num == int(5)): # color at position 5
        return (66,12,76) # purple
    elif (num == int(6)): # color at position 6
        return (110,110,110) # grey

def single_attack (back_mode, id_src, id_dst, cnt, arr_players, arr_territories, totals, screen, gui_text_levels): # function of single (AKA 'manual') attack
    arr_territories[int(id_src) - totals[0]].stick_blob() # re-apply the colored-png (blob)
    arr_territories[int(id_src) - totals[0]].stick_force_no(2) # re-apply the number-of-forces (text)
    arr_territories[int(id_dst) - totals[0]].stick_blob() # re-apply the colored-png (blob)
    arr_territories[int(id_dst) - totals[0]].stick_force_no(3) # re-apply the number-of-forces (text)
    pygame.display.update()
    clr_atk = determine_color(arr_territories[int(id_src) - totals[0]].controller) # color of attacking dice
    clr_def = determine_color(arr_territories[int(id_dst) - totals[0]].controller) # color of attacked dice
    atk_roll = single_dice_roll() # the dice roll of the attacker
    def_roll = single_dice_roll() # the dice roll of the defender
    stick_dice(atk_roll, gui_text_levels[6], clr_atk, cnt, screen) # apply the dice-icon onto the screen
    stick_dice(def_roll, gui_text_levels[7], clr_def, cnt, screen) # apply the dice-icon onto the screen
    if (atk_roll > def_roll): # if the roll of the attacker is greater than the roll of the defender
        arr_territories[int(id_dst) - totals[0]].force_no -= 1 # decrease number of forces of attacking territory by 1.
        for run in range(0, len(arr_players), 1): # loop over the list of player-objects.
            if (str(id_dst) in arr_players[run].trr_and_frc): # if ID-num is found in the dictionary of "territory and force", then...
                arr_players[run].trr_and_frc[str(id_dst)] -= 1 # decrease the number of forces of the attacked territory by 1.
        #print_arr_players(arr_players) # debug function
        territory_capture(cnt, id_src, id_dst, arr_players, arr_territories, totals, screen) # determine if the territory has been captured
        #print_arr_players(arr_players) # debug function
    else: # if the roll of the defender is greater / equals to the roll of the attacker
        arr_territories[int(id_src) - totals[0]].force_no -= 1 # decrease the number of forces of the source territory by 1.
        for run in range(0, len(arr_players), 1): # loop over the list of player-objects.
            if (str(id_src) in arr_players[run].trr_and_frc): # if the source ID-number is in the dictionary of "territory and force", then...
                arr_players[run].trr_and_frc[str(id_src)] -= 1 # decrease the number of forces by 1
        #print_arr_players(arr_players) # debug print
    time.sleep(1)
    arr_territories[int(id_src) - totals[0]].stick_blob() # re-apply the colored-png (blob)
    arr_territories[int(id_src) - totals[0]].stick_force_no(0) # re-apply the number-of-forces (text)
    arr_territories[int(id_dst) - totals[0]].stick_blob() # re-apply the colored-png (blob)
    arr_territories[int(id_dst) - totals[0]].stick_force_no(0) # re-apply the number-of-forces (text)
    time.sleep(1.5) # make the program hold for 0.8 seconds
    remove_dice(gui_text_levels[6][0],gui_text_levels[6][1], back_mode, screen) # remove the dice-icon from the PyGame window.
    remove_dice(gui_text_levels[7][0],gui_text_levels[7][1], back_mode, screen) # remove the dice-icon from the PyGame window.

def territory_capture (cnt, id_src, id_dst, arr_players, arr_territories, totals, screen): # function to determine and act if a territory has been capture
    #print("The 'capture' conditional is: " + str(arr_territories[id_dst - totals[0]].force_no)) # debug print
    if (arr_territories[int(id_dst) - totals[0]].force_no == int(0)): # if the number of forces in the destination territory is 0, then...
        for run in range(0, len(arr_players), 1): # loop over the list of player-objects.
            if (str(id_dst) in arr_players[run].trr_and_frc): # if the destination-ID is found in dictionary of "territory and force", then...
                #print("cnt is: " + str(cnt)) # debug print
                arr_players[run].trr_and_frc.pop(str(id_dst)) # remove this ID-number from the dictionary
                arr_players[cnt].trr_and_frc.update({str(id_dst):1}) # append this ID-number to the dictionary of the conquering player.
            if (str(id_src) in arr_players[run].trr_and_frc): # if the source-ID is found in the dictionary of "territory and force"
                arr_players[run].trr_and_frc[str(id_src)] -= 1 # decrease the number of forces of the attacking territory by 1.

        arr_territories[int(id_dst) - totals[0]].controller = int(arr_players[cnt].id_num) # update the new controller of the territory in the territory-object
        arr_territories[int(id_src) - totals[0]].force_no -= 1 # decrease the number of forces of the source-territory by 1.
        arr_territories[int(id_dst) - totals[0]].force_no += 1 # increase the number of forces of the destination-territory by 1.
        return 1 # return 1 - because there was a capture of a territory
    else:
        return 0 # return 0 - because there WASN'T a capture of a territory

def single_dice_roll (): # function that returns a random value from 1 to 6
    return random.randrange(1,7) # this simulates a dice-roll

def attack (cnt, back_mode, arr_players, arr_territories, totals, screen, gui_text_levels, lv1_gt,lv2_gt,lv3_gt,lv4_gt,lv5_gt,lv6_gt,lv7_gt,lv8_gt,lv9_gt): # function for allowing current player to attack an opponent.
    lv1_gt.change_text("ATTACK") # change the text-value of the text-object (gui_text)
    lv1_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    if (arr_players[cnt].typed == int(0)): # if the player is a computer, then...
        lv2_gt.change_text("waiting for " + str(arr_players[cnt].name) + " to attack") # change the text-value of the text-object (gui_text)
    else: # if the player is a human, then...
        lv2_gt.change_text(str(arr_players[cnt].name) + ", time to attack") # change the text-value of the text-object (gui_text)
    lv2_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv2_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    continue_attack = able_attack(arr_players, cnt) # function to determine whether it's possible to perform an attack
    while (continue_attack == 1): # if it IS possible to perform an attack, then...
        pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
        if (arr_players[cnt].typed == int(0)): # 0=COMP
            #continue_attack = int(0)
            continue_attack = comp_attack (back_mode, cnt, arr_players, arr_territories, totals, screen, gui_text_levels, lv2_gt, lv3_gt, lv5_gt, lv6_gt, lv7_gt, lv8_gt, lv9_gt) # the computer-attack function is called.
        else: # 1=HUMAN
            continue_attack = human_attack (back_mode, cnt, arr_players, arr_territories, totals, screen, gui_text_levels, lv3_gt, lv4_gt, lv5_gt, lv6_gt, lv7_gt, lv8_gt, lv9_gt) # the human-attack function is called.

def able_attack (arr_players, cnt): # function to determine if an attack is possible
    cnt = int(cnt) # stabilize the 'cnt' variable to be an integer.
    for run in arr_players[cnt].trr_and_frc: # loop over the territories of the current-user (in the dictionary of "territory and force")
        if (arr_players[cnt].trr_and_frc[run] > 1): # if at-least one territory has 2 or more forces, then...
            return 1 # return 1 - because there IS a possibility to attack.
    return 0 # return 0 - because there is NOT a possibility to attack.


def able_move (arr_players, cnt): # function to determine if a player can move forces.
    cnt = int(cnt) # stabilize the 'cnt' variable to be an integer.
    if (len(arr_players[cnt].trr_and_frc) > 1): # if the players owns 2 or more territories
        for cnt2 in arr_players[cnt].trr_and_frc: # loop over the territories of the "territory and force" dictionary
            if (arr_players[cnt].trr_and_frc[cnt2] > 1): # if the territory has 2 or more forces, then...
                #print("force amount is: " + str(arr_players[cnt].trr_and_frc[cnt2])) # debug function
                #print("DURING MOVE") # debug function
                #print_arr_players(arr_players) # debug function
                return 1 # return 1 because the player CAN move forces.
    return 0 # return 0 beause the player CANNOT move forces

def comp_move_one (cnt, arr_players, arr_territories, totals, moves_remaining, lv2_gt, lv3_gt, lv4_gt, lv5_gt, lv6_gt, lv9_gt): # function to allow computer-player to move forces
    cnt = int(cnt) # stabilize the 'cnt' variable to be an integer.
    moves_remaining = int(moves_remaining) # stabilize the 'moves_remaining' variable to be an integer.
    lv2_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv2_gt.change_text(str(arr_players[cnt].name) + " is moving forces") # change the text-value of the text-object (gui_text)
    lv2_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    #print("The able_move(arr_players, cnt) is: " + str(able_move(arr_players, cnt))) # debug print
    if (able_move(arr_players, cnt)): # if the player can move forces, then...
        #print(str(arr_players[cnt].name) + " is able to move!") # debug print
        id_src = int(-1) # neutralize the source-territory
        id_dst = int(-1) # neutralize the destination-territory
        lv3_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv3_gt.change_text(str(arr_players[cnt].name) + " is selecting src. territory") # change the text-value of the text-object (gui_text)
        lv3_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv4_gt.change_text(str(moves_remaining) + " remaining") # change the text-value of the text-object (gui_text)
        lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        while (id_src == int(-1)): # while the source-territory has not been selected yet, then...
            pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
            id_src = random.choice(list(arr_players[cnt].trr_and_frc)) # select a random territory from the "territory and force" dictionary of the current player
            while (arr_territories[int(id_src) - totals[0]].force_no == int(1)): # if the number of forces of the selected territory is 1 (which means that forces CANNOT be moves from this territory), then...
                pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
                id_src = random.choice(list(arr_players[cnt].trr_and_frc)) # reselect a random territory from the "territory and force" dictionary of the current player
        lv6_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv6_gt.change_text("SOURCE: " + str(arr_territories[int(id_src) - totals[0]].name)) # change the text-value of the text-object (gui_text)
        lv6_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        lv5_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv5_gt.change_text(str(arr_players[cnt].name) + " is selecting dst. territory") # change the text-value of the text-object (gui_text)
        lv5_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        while (id_dst == int(-1)): # if the destination territory has not been selected yet, then...
            pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
            id_dst = random.choice(arr_territories[int(id_src) - totals[0]].borders) # PROBLEM (24/10/2020)
            #print("str(arr_territories[int(id_dst) - totals[0]].controller is: " + str(str(arr_territories[int(id_dst) - totals[0]].controller))) # debug print
            #print("arr_players[cnt].allies is: " + str(arr_players[cnt].allies)) # debug print
            #print("arr_territories[int(id_src) - totals[0]].controller is: " + str(arr_territories[int(id_src) - totals[0]].controller)) # debug print
            #print("arr_territories[int(id_dst) - totals[0]].controller is: " + str(arr_territories[int(id_dst) - totals[0]].controller)) # debug print
            while ((str(arr_territories[int(id_dst) - totals[0]].controller) not in arr_players[cnt].allies) or (arr_territories[int(id_src) - totals[0]].controller != arr_territories[int(id_dst) - totals[0]].controller)): # PROBLEM 8/9/2020
                pygame.event.clear()  # clearing the event-cache (preventing from the PyGame window to freeze)
                id_dst = random.choice(arr_territories[int(id_src) - totals[0]].borders) # reselect a random destination territory
                if (random.randint(0,100) < 10): # 30% change it'll quit the function
                    moves_remaining -= 1 # decrease the count of moves remaining by 1.
                    time.sleep(1) # make the program hold for 1 seconds
                    return moves_remaining # return the count of the remaining amount of moves
        lv9_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
        lv9_gt.change_text("DESTINATION: " + str(arr_territories[int(id_dst) - totals[0]].name)) # change the text-value of the text-object (gui_text)
        lv9_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
        arr_territories[int(id_src) - totals[0]].stick_blob() # apply the 'blob' (colored-PNG) onto the PyGame window.
        arr_territories[int(id_dst) - totals[0]].stick_blob() # apply the 'blob' (colored-PNG) onto the PyGame window.
        arr_territories[int(id_src) - totals[0]].stick_force_no(4) # apply the force-number onto the PyGame window.
        arr_territories[int(id_dst) - totals[0]].stick_force_no(4) # apply the force-number onto the PyGame window.
        #print("before comp move") # debug print
        #print_arr_players(arr_players) # debug print
        arr_players[cnt].trr_and_frc[str(id_src)] -= 1 # decrease number-of-forces of source territory by 1 (player-object aspect)
        arr_players[cnt].trr_and_frc[str(id_dst)] += 1 # increase number-of-forces of destination territory by 1 (player-object aspect)
        #print("after comp move") # debug print
        #print_arr_players(arr_players) # debug print
        arr_territories[int(id_src) - totals[0]].force_no -= 1 # decrease number-of-forces of source territory by 1 (territory-object aspect)
        arr_territories[int(id_dst) - totals[0]].force_no += 1 # increase number-of-forces of destination territory by 1 (territory-object aspect)
        time.sleep(1)
        arr_territories[int(id_src) - totals[0]].stick_blob() # apply the 'blob' (colored-PNG) onto the PyGame window.
        arr_territories[int(id_dst) - totals[0]].stick_blob() # apply the 'blob' (colored-PNG) onto the PyGame window.
        arr_territories[int(id_src) - totals[0]].stick_force_no(0) # apply the force-number onto the PyGame window. # missing
        arr_territories[int(id_dst) - totals[0]].stick_force_no(0) # apply the force-number onto the PyGame window.
        time.sleep(1) # make the program hold for 1 seconds
        moves_remaining -= 1 # decrease the number of remaining-moves by 1.
        return moves_remaining # return the number of remaining-moves.
    else: # otherwise - if the player is unable to move forces, then...
        moves_remaining = int(0) # make an absolute-decrease in number of moves
        time.sleep(1) # make the program hold for 1 seconds
        return moves_remaining # return the number of remaining-moves.


        
        
        

def human_move_multiple (cnt, back_mode, arr_players, arr_territories, totals, moves_remaining, screen, gui_text_levels, lv2_gt, lv3_gt, lv4_gt, lv5_gt, lv6_gt, lv7_gt, lv9_gt): # function to allow a human-player to make multiple-moves.
    cnt = int(cnt) # stabilize the 'cnt' variable into an integer.
    #print(str(arr_players[cnt].name) + ", it's time to move forces!") # debug print
    moves_remaining = int(moves_remaining)  # stabilize the 'cnt' variable into an integer.
    lv4_gt.change_text(str(moves_remaining) + " remaining") # change the text-value of the text-object (gui_text)
    lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    if (len(arr_players[cnt].trr_and_frc) > 1): # if there are 2 or more territories owned by the current player, then...
        id_src = int(-1) # neutralize the source-territory
        id_dst = int(-2) # neutralize the destination-territory
        while (moves_remaining > 0 and (id_src == int(-1) and (id_dst == int(-2) or id_dst == int(-1)))): # if the number of moves remaining is greater than zero AND none of source-territory nor destination-territory have been selected, then...
            skip_button = Button(1, "SKIP", back_mode, (gui_text_levels[12][0],gui_text_levels[12][1],140,50), 5, 0, 0, screen) # create the 'skip' button
            #print(str(arr_players[cnt].name) + ", select source territory!") # debug print
            lv3_gt.change_text(str(arr_players[cnt].name) + ", select src. territory!") # change the text-value of the text-object (gui_text)
            lv3_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
            lv3_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
            while (id_src == int(-1)): # if the source-territory is not yet selected, then...
                for event in pygame.event.get(): # get the PyGame event.
                    mouse = pygame.mouse.get_pos() # get the positions (x,y) coordinates of the mouse.
                    click = pygame.mouse.get_pressed() # get the boolean-value of the mouse-click.
                    color = screen.get_at(mouse) # get the RGB value of the pixel that the mouse is currently hovered-on.
                    y = screen.get_size()[1] # get the length of the PyGame window.
                    moves_remaining = skip_button.button_functional(moves_remaining) # initialize functionality of the skip-button
                    if (moves_remaining == int(0)): # if there are no more moves-remaining, then...
                        return 0 # return 0 - because there are no more moves remaining.
                    if (click[0] == int(1) and (color[2] != 0) and (color[2] != 255) and (mouse[1] < (y-200))): # if the left-button has been clicked, then...
                        id_selected = shortest_distance((mouse[0],mouse[1]),arr_territories) # get the ID-number of the selected territory (dots system).
                        if ((arr_territories[id_selected - totals[0]].controller == int(arr_players[cnt].id_num)) and (arr_territories[id_selected - totals[0]].force_no > 1)): # if the selected territory does belong to the player, then...
                            id_src = int(id_selected) # assign the ID-number of the territory into the source-territory-variable.
                            lv6_gt.change_text("SOURCE: " + str(arr_territories[id_src - totals[0]].name)) # change the text-value of the text-object (gui_text)
                            lv6_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                            lv6_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.

                            lv7_gt.change_text("right-click to release")
                            lv7_gt.remove_gui_text()
                            lv7_gt.insert_gui_text(arr_players[cnt].color)

                            lv5_gt.change_text(str(arr_players[cnt].name) + ", select dest. territory!") # change the text-value of the text-object (gui_text)
                            lv5_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                            lv5_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.



                            # 6/9/2020 - WORK HERE - "left-click to release"

                            break
                        elif (arr_territories[id_selected - totals[0]].controller != int(arr_players[cnt].id_num)):
                            lv6_gt.change_text("source territory must be owned!")
                            lv6_gt.insert_gui_text(back_mode)
                            time.sleep(1)
                            lv6_gt.remove_gui_text()
                        elif (arr_territories[id_selected - totals[0]].force_no == 1):
                            lv6_gt.change_text("source territory must have at-least 2 forces!")
                            lv6_gt.insert_gui_text(back_mode)
                            time.sleep(1)
                            lv6_gt.remove_gui_text()
                    if (event.type == pygame.QUIT):
                        pygame.display.quit()
                        pygame.quit()
                        exit(0)
            id_dst = int(-1) # neutralize the destination-territory, make available to receive a value.
            #print(str(arr_players[cnt].name) + ", select destination territory!") # debug print
            while (id_dst == int(-1)): # while the destination-territory has not been selected, then...
                for event in pygame.event.get(): # get the PyGame event.
                    mouse = pygame.mouse.get_pos() # get the positions (x,y) coordinates of the mouse.
                    click = pygame.mouse.get_pressed() # get the boolean-value of the mouse-click.
                    color = screen.get_at(mouse) # get the RGB value of the pixel that the mouse is currently hovered-on.
                    moves_remaining = skip_button.button_functional(moves_remaining) # initialize functionality of the skip-button
                    y = screen.get_size()[1] # get the length of the PyGame window.
                    if (event.type == pygame.QUIT):
                        pygame.display.quit()
                        pygame.quit()
                        exit(0)
                    if (moves_remaining == int(0)): # if the number of remaining moves is 0, then...
                        arr_territories[int(id_src) - totals[0]].stick_blob() # re-apply the colored-PNG (blob) of the source-territory.
                        arr_territories[int(id_src) - totals[0]].stick_force_no(0) # re-apply the text of number-of-forces of the source-territory.
                        return 0 # return 0, because the number of remaining forces is 0.
                    if (click[0] == int(1) and (color[2] != 0) and (color[2] != 255) and (mouse[1] < (y-200))): # if the left-button has been clicked, then...
                        id_selected = shortest_distance((mouse[0],mouse[1]),arr_territories) # get the ID-number of the selected territory (dots system).
                        if ((arr_territories[id_selected - totals[0]].controller == int(arr_players[cnt].id_num)) and (arr_territories[id_src - totals[0]].force_no > 1) and (moves_remaining > 0) and (id_selected != id_src) and (id_selected in arr_territories[id_src - totals[0]].borders)): # if the selected territory does belong to the player, then...
                            id_dst = int(id_selected) # assign territory-ID to the territory-destination variable
                            lv9_gt.change_text("DESTINATION: " + str(arr_territories[id_dst - totals[0]].name)) # change the text-value of the text-object (gui_text)
                            lv9_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                            lv9_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                            arr_territories[id_src - totals[0]].force_no -= 1 # decrement the count of forces of the 'force_no' attribute (of territory object) by 1.
                            arr_territories[id_dst - totals[0]].force_no += 1 # increment the count of forces of the 'force_no' attribute (of territory object) by 1.
                            arr_territories[int(id_src) - totals[0]].stick_blob() # re-apply the colored-PNG (blob) of the source-territory.
                            arr_territories[int(id_src) - totals[0]].stick_force_no(4) # re-apply the text of number-of-forces of the source-territory.
                            arr_territories[int(id_dst) - totals[0]].stick_blob() # re-apply the colored-PNG (blob) of the destination-territory.
                            arr_territories[int(id_dst) - totals[0]].stick_force_no(4) # re-apply the text of number-of-forces of the destination-territory.
                            #print("--------------------BEFORE-------------------") # debug print
                            #print("The source is: " + str(arr_players[cnt].trr_and_frc[id_src])) # debug print
                            #print("The destination is: " + str(arr_players[cnt].trr_and_frc[id_dst])) # debug print
                            arr_players[cnt].trr_and_frc[str(id_src)] -= 1 # decrease number-of-forces of source territory by 1 (player-object aspect)
                            arr_players[cnt].trr_and_frc[str(id_dst)] += 1 # increase number-of-forces of destination territory by 1 (player-object aspect)
                            #print("-------------------AFTER---------------------") # debug print
                            #print("The source is: " + str(arr_players[cnt].trr_and_frc[id_src])) # debug print
                            #print("The destination is: " + str(arr_players[cnt].trr_and_frc[id_dst])) # debug print
                            #arr_players[cnt].trr_and_frc[id_src] -= 1 # decrement the count of forces from the "territory and force" dictionary by 1 (where the ID-selected matches the key).
                            #arr_players[cnt].trr_and_frc[id_dst] += 1 # increment the count of forces from the "territory and force" dictionary by 1 (where the ID-selected matches the key).
                            #print_arr_players(arr_players) # debug print
                            moves_remaining = int(moves_remaining - 1) # decrease number of remaining-forces by 1.
                            lv4_gt.change_text(str(moves_remaining) + " remaning") # change the text-value of the text-object (gui_text)
                            lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                            lv4_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
                            time.sleep(1)
                            arr_territories[int(id_dst) - totals[0]].stick_blob() # re-apply the colored-PNG (blob) of the destination-territory. # list of index out of range
                            arr_territories[int(id_dst) - totals[0]].stick_force_no(0) # re-apply the text of number-of-forces of the destination-territory.
                            id_dst = int(-1) # neutralize the destination-territory
                        elif (id_selected == id_src):
                            lv9_gt.change_text("cannot move forces to same territory!")
                            lv9_gt.insert_gui_text(back_mode)
                            time.sleep(1)
                            lv9_gt.remove_gui_text()
                        elif (id_selected not in arr_territories[id_src - totals[0]].borders):
                            lv9_gt.change_text("dest. territory does board with src. territory!")
                            lv9_gt.insert_gui_text(back_mode)
                            time.sleep(1)
                            lv9_gt.remove_gui_text()
                        elif (arr_territories[id_selected - totals[0]].controller != int(arr_players[cnt].id_num)):
                            lv9_gt.change_text("dest. territory must be owned!")
                            lv9_gt.insert_gui_text(back_mode)
                            time.sleep(1)
                            lv9_gt.remove_gui_text()
                        if (moves_remaining == 0): # if the number of remaining-moves is 0, then...
                            break # break out of the function
                            arr_territories[int(id_src) - totals[0]].stick_blob() # re-apply the colored-PNG (blob) of the source-territory.
                            arr_territories[int(id_src) - totals[0]].stick_force_no(0) # re-apply the text of number-of-forces of the source-territory.
                            arr_territories[int(id_dst) - totals[0]].stick_blob() # re-apply the colored-PNG (blob) of the destination-territory.
                            arr_territories[int(id_dst) - totals[0]].stick_force_no(0) # re-apply the text of number-of-forces of the destination-territory.
                    elif (click[2] == int(1)): # if the right-mouse button has been clicked, then...
                        arr_territories[int(id_src) - totals[0]].stick_blob() # re-apply the colored-PNG (blob) of the source-territory. # list of index out of range
                        arr_territories[int(id_src) - totals[0]].stick_force_no(0) # re-apply the text of number-of-forces of the source-territory.
                        #print("Please select another territory") # print-to-CLI the message (to select another source-territory).
                        id_src = int(-1) # neutralize the selected source-territory.
                        id_dst = int(-2) # neutralize the selected destination-territory.
                        lv5_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                        lv6_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
                        lv9_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    else: # if the human-player cannot move forces, then...
        moves_remaining = int(0) # make an absolute-decrease in number of moves-remaining.
    lv4_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    return moves_remaining # return the number of moves-remaining

def move (cnt,back_mode, arr_players, arr_territories, totals, screen, gui_text_levels, lv1_gt, lv2_gt, lv3_gt, lv4_gt, lv5_gt, lv6_gt, lv7_gt, lv9_gt): # function for allowing current player to move forces.
    cnt = int(cnt) # stabilize the 'cnt' variable value into an integer
    moves_left = calculate_moves_left(cnt, arr_players) # calculate the number of moves remaining (based on number of territories)
    lv1_gt.change_text("MOVE") # change the text-value of the text-object (gui_text)
    lv1_gt.insert_gui_text(arr_players[cnt].color) # apply the text-object (gui_text) onto the PyGame window with the specified color.
    while (moves_left > 0): # if the number-of-moves is greater than 0, then...
        if (arr_players[cnt].typed == int(0)): # if the player-type is a computer, then...
            moves_left = comp_move_one(cnt, arr_players, arr_territories, totals, moves_left, lv2_gt, lv3_gt, lv4_gt, lv5_gt, lv6_gt, lv9_gt) # function to allow computer-player to move forces.
        else: # otherwise - if the player-type is a human, then...
            #pass
            #moves_left = int(0)
            moves_left = human_move_multiple(cnt, back_mode, arr_players, arr_territories, totals, moves_left, screen, gui_text_levels, lv2_gt, lv3_gt, lv4_gt, lv5_gt, lv6_gt, lv7_gt, lv9_gt) # function to allow humna-player to move forces.
    lv1_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv2_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv3_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv5_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv6_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)
    lv9_gt.remove_gui_text() # use the class-method to apply a filled-rectangle over the text (to "delete" it)

def calculate_moves_left (cnt, arr_players): # function to determine number-of-moves remaining (based on number of owned territories)
    cnt = int(cnt) # stabilize the 'cnt' variable-value into an integer.
    return (len(arr_players[cnt].trr_and_frc)) # return the number of territories of the current player.

def calculate_fortify (cnt, arr_players, totals): # method for calculating the number of forces to deploy.
    cnt = int(cnt) # stabilize the 'cnt' variable into an integer.
    amount = int(math.ceil(len(arr_players[cnt].trr_and_frc) / 2)) # the actual number of forces to deploy in a single turn.
    if (totals[0] == int(0)): # countries-map
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['0','1','2','3','4','5','6','7','8']): # multiple-membership
            amount += int(5) # north-america
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['9','10','11','12']): # multiple-membership
            amount += int(2) # south-america
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['13','14','15','16','17','18','19']): # multiple-membership
            amount += int(5) # europe
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['20','21','22','23','24','25']): # multiple-membership
            amount += int(3) # africa
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['26','27','28','29','30','31','32','33','34','35','36','37']): # multiple-membership
            amount += int(7)
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['38','39','40','41']): # multiple-membership
            amount += int(2)
    elif (totals[0] == int(42)): # hexagons-map
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['42','43','44','45','46','47','48','56','57','58','59','60','61','62']): # multiple-membership
            amount += int(4) # north-west hexagons
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['49','50','51','52','53','54','55','63','64','65','66','67','68','69']): # multiple-membership
            amount += int(4) # north-east hexagons
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['70','71','72','73','74','75','76','84','85','86','87','88','89','90']): # multiple-membership
            amount += int(4) # south-west hexagons
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['77','78','79','80','81','82','83','91','92','93','94','95','96','97']): # multiple-membership
            amount += int(4) # south-east hexagons
    elif (totals[0] == int(98)): # pyramid-map
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['98','99','100','101','102','103','104','105','106','107','108','109','110','111','112','113']): # multiple-membership
            amount += int(4) # north block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['114','123','124','125','134','135','136','137','138','147','148','149','150','151','152','153']): # multiple-membership
            amount += int(4) # west block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['115','116','117','118','119','120','121','126','127','128','129','130','139','140','141','154']): # multiple-membership
            amount += int(4) # central block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['122','131','132','133','142','143','144','145','146','155','156','157','158','159','160','161']): # multiple-membership
            amount += int(4) # eastern block
    elif (totals[0] == int(162)):
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['162','163']): # multiple-membership
            amount += int(2) # north-western block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['164','165']): # multiple-membership
            amount += int(2) # south-eastern block
    elif (totals[0] == int(166)):
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['166','167','168','169','174','175','176','177']): # multiple-membership
            amount += int(3) # north-western block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['170','171','172','173','178','179','180','181']): # multiple-membership
            amount += int(3) # north-eastern block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['182','183','184','185','190','191','192','193']): # multiple-membership
            amount += int(3) # south-western block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['186','187','188','189','194','195','196','197']): # multiple-membership
            amount += int(3) # south-eastern block
    elif (totals[0] == int(198)):
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['198','199','200','204','205','206','210','211','212']): # multiple-membership
            amount += int(4) # north-western block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['201','202','203','207','208','209','213','214','215']): # multiple-membership
            amount += int(4) # north-eastern block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['216','217','218','222','223','224','228','229','230']): # multiple-membership
            amount += int(4) # south-western block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['219','220','221','225','226','227','231','232','233']): # multiple-membership
            amount += int(4) # south-eastern block
    elif (totals[0] == int(234)):
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['234','240','242','241']): # multiple-membership
            amount += int(4) # 1st-block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['235','236','243','244']): # multiple-membership
            amount += int(4) # 2nd-block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['237','238','245','246']): # multiple-membership
            amount += int(4) # 3rd-block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['239','247','248','249']): # multiple-membership
            amount += int(4) # 4th-block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['250','251','252','260']): # multiple-membership
            amount += int(4) # 5th-block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['253','254','261','262']): # multiple-membership
            amount += int(4) # 6th-block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['255','256','263','264']): # multiple-membership
            amount += int(4) # 7th-block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['257','258','265','259']): # multiple-membership
            amount += int(4) # 8th-block
    elif (totals[0] == int(266)):
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['266']): # multiple-membership
            amount += int(1) # esc button
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['267','268','269','270']): # multiple-membership
            amount += int(3) # f1-f4 buttons
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['271','272','273','274']): # multiple-membership
            amount += int(3) # f5-f8 buttons
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['275','276','277','278']): # multiple-membership
            amount += int(3) # f9-f12 buttons
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['279','280','281']): # multiple-membership
            amount += int(2) # print-scroll-pause buttons
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['282','283','284','285','286','287','288','289','290','291','292','293','294','295','303','304','305','306','307','308','309','310','311','312','313','314','315','316','324','325','326','327','328','329','330','331','332','333','334','335','336','340','341','342','343','344','345','346','347','348','349','350','351','352','358','359','360','361','362','363','364','365']): # multiple-membership
            amount += int(25) # big-block
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['296','297','298','317','318','319']): # multiple-membership
            amount += int(7) # insert-home-delete-end buttons
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['299','300','301','302','320','321','322','323','337','338','339','354','355','356','357','369','370']): # multiple-membership
            amount += int(15) # numpad buttons
        if all (k in (arr_players[cnt].trr_and_frc).keys() for k in ['353','366','367','368']): # multiple-membership
            amount += int(5) # arrow-key buttons
    return amount
        
def initiate_arr_names (arr_names, player_select): # function to initiate the list of the names of players
    if (len(arr_names) != int(player_select[2])): # while there aren't 2 names
        while (len(arr_names) < int(player_select[2])):
            arr_names.append(str("")) # add an empty string to the list
        while (len(arr_names) > int(player_select[2])): # 
            arr_names.pop() # remove the last string from the list.
    #print("arr_names is: " + str(arr_names)) # debug print - print the list of the names

def refresh_panel(resolutions, back_mode, screen): # color the panel in the color of the background
    back_mode = int(back_mode) # stabilize the back_mode value into an integer.
    if (back_mode == int(0)): # if the background is dark, then...
        color = (0,0,0) # the color will be black.
    else: # if the background is white, then...
        color = (255,255,255) # the color will be white.
    pygame.draw.rect(screen, color, (0,resolutions[1]-200,resolutions[0],200), 0) # draw a rectangle over the entire-panel, to conceal any residue of previous player-turn
    pygame.display.update() # refresh the PyGame window.

def check_game_over (arr_players): # function to determine if the game is finished
    arr_alive = [] # array that collects all 'active' players (that have an ID-number that's different than '-1')
    for cnt in range(0, len(arr_players), 1): # loop for the list of player-objects
        if (arr_players[cnt].id_num != int(-1)): # if the player-object is NOT deactivated (has at least 1 owned territory), then...
            arr_alive.append(str(arr_players[cnt].id_num)) # append the id-number of the active player to the list.
    #print("arr_alive is: " + str(arr_alive)) # debug print
    #print("length of arr_alive is: " + str(len(arr_alive))) # debug print
    for cnt in range(0, len(arr_players), 1): # loop over the list of player-objects
        if (len(arr_alive) == len(arr_players[cnt].allies)): # if the length of 'alive-arr' if equal to the length of list of allies of the player, then...
            if all (k in arr_alive for k in arr_players[cnt].allies): # multiple-membership - if all items in 'arr-alive' exist in 'allies-group', then...
                return 1 # return 1 - the game is over, all players remaining active in the game are allies.
    return 0 # return 0 - the game is not over yet.
            
def disable_players (arr_players): # function to determine if a player gets disabled (can no longer play their turn)
    for cnt in range(0, len(arr_players), 1): # loop over the list of player-objects.
        if (len(arr_players[cnt].trr_and_frc) == int(0)): # if the number of territories of that player is 0, then...
            arr_players[cnt].id_num = int(-1) # turn it's ID-number into '-1' (disabling the player without deleting the player-object)

def insert_credentials_text (text, position, color, screen): # method for applying the button onto the PyGame window.
    font = pygame.font.Font('freesansbold.ttf', 50) # font size is 30
    text = font.render(text, True, color) # define the text of the button
    textRect = text.get_rect() # define the rectangle that the text will be inside of.
    textRect.center = ((position[0]+(position[2]/2)),(position[1]+(position[3]/2))) # define the center of the rectangle.
    screen.blit(text, textRect) # apply the text and rectangle onto the screen.
    pygame.display.update() # refresh the PyGame window.

def add_to_allies(allies, temp2, temp1): # function to add a player's-ID to an allies-group.
    for cnt in range(0, len(allies), 1): # loop over the list of allies.
        if (str(temp2) in allies[cnt]): # if the ID-number of the player already exists within the allies-group, then...
            allies[cnt].remove(str(temp2)) # remove the ID-number of that player.
            break # break out of this loop - because the ID-number of the player has already been removed (and cannot appear in more than 1 allies-group simultaneously)
    allies[temp1-1].append(str(temp2)) # add to the allies-group the ID-number of the selected player.


def locate_player (arr_players, id_num): # locate the player # FUNCTION NOT USED
    for cnt in range(0, len(arr_players), 1): # loop over the list of player-objects.
        if (arr_players[cnt].id_num == id_num): # if the ID-number is of the iterated player-object, then...
            return arr_players[cnt] # return the object


def reset_allies (allies, back_mode): # function to reset the allies-group (clear all ID-numbers that have been inserted into them)
    if (back_mode == int(0)): # if the background-color is dark, then...
        color = (0,0,0) # BLACK
    else:
        color = (255,255,255) # WHITE
    for cnt in range(0, len(allies), 1): # loop over the allies-group
        allies[cnt] = [] # reassign the allies-group to be an empty-list.
    pygame.draw.rect(screen, color, (10,255,1080,50), 0) # draw a rectangle over the gui-numbers of the selected-allies of the players