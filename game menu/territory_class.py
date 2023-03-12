import pygame # import the PyGame library.
pygame.init() # initialize the PyGame library.
import pymongo # reading data using the pymongo library.
from pymongo import MongoClient # get the "MongoClient" module from the "PyMongo" library.

# this is the cluster - as exists in the MongoDB atlas.
cluster = MongoClient("mongodb+srv://PyRiskUser:6310290099@cluster0.udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"] # defining the database as variable named 'db'. The "pyrisk_db" is the database as appears in the MongoDB cloud.
res_doc = db["pyrisk_resolutions"] # from the 'db' variable - find the "pyrisk_resolution" document - as appears in the MongoDB cloud.
total_doc = db["pyrisk_total_territories"] # from the 'db' variable - find the "pyrisk_total_territories" document - as appears in the MongoDB cloud.

blob_links_doc = db["pyrisk_blob_links"] # from the 'db' variable - find the "pyrisk_blob_links" document - as appears in the MongoDB cloud.
bonus_doc = db["pyrisk_bonus"] # from the 'db' variable - find the "pyrisk_bonus" document - as appears in the MongoDB cloud.
borders_doc = db["pyrisk_borders"] # from the 'db' variable - find the "pyrisk_borders" document - as appears in the MongoDB cloud.
dots_doc = db["pyrisk_dots"] # from the 'db' variable - find the "pyrisk_dots" document - as appears in the MongoDB cloud.
force_doc = db["pyrisk_force_text"] # from the 'db' variable - find the "pyrisk_force_text" document - as appears in the MongoDB cloud.
position_doc = db["pyrisk_positions"] # from the 'db' variable - find the "pyrisk_positions" document - as appears in the MongoDB cloud.

general_doc = db["pyrisk_general"] # the "pyrisk_general" document is currently not in use.


# CONTROLLERS:
# -1 = nobody (black / white)
# +0 = green
# +1 = blue
# +2 = yellow
# +3 = red
# +4 = orange
# +5 = purple
# +6 = grey

class Territory: # the territory class.
    def __init__(self, id_num, name, pos, blob_names, real_blobs, borders, bonus_group, controller, force_no, dots, text_force_point,screen):
        self.id_num = id_num # the identification number of the territory (non-human-friendly).
        self.name = name # the name of the territory (human-friendly).
        self.pos = [0]*2 # pos = "position"
        self.blob_names = blob_names # the names of the blob - (green / blue / yellow / red / orange / purple / grey).
        self.real_blobs = [0]*7 # the actual PNG files of the territory - (green / blue / yellow / red / orange / purple / grey).
        self.borders = borders # the list of ID-numbers of bordering countries.
        self.bonus_group = {} # the dictionary of bounus group, and the actual-bonus number / count.
        self.controller = int(-1) # the controller of the territory - "-1" means "unaffiliated".
        self.force_no = force_no # force_no = "force number"
        self.dots = [] # the list of dots (main method for determining which territory has been selected by left-mouse click).
        self.text_force_point = [0]*2 # the point of the map (middle of territory) to put the number of territory forces.
        self.res = [0]*2 # the resolutions of of PyGame window - onto which the territory "blobs" are applied to.
        self.screen = screen # the PyGame window - onto which the territory "blobs" are applied to.

    def get_res (self, selected_map): # method for getting the map-resolutions from the database.
        RES = res_doc.find_one({"_id":(selected_map-1)}) # locate the matching "object" according to the map number.
        RES = RES["res"] # locate the resolutions of the located "object".
        self.res[0] = RES[0] # 'X' of self is 'X' of resolutions of located "object".
        self.res[1] = RES[1] # 'Y' of self is 'Y' of resolutions of located "object".

    def get_screen(self): # DO WE NEED THIS?
        X = int(self.res[0])
        Y = int(self.res[1])
        self.screen = pygame.display.set_mode((X,Y))


    def get_position (self): # method for getting the blob-positions from the database.
        position = position_doc.find_one({"_id":(self.id_num)}) # locate the matching "object" according to the territory's ID number.
        position = position["position"] # get the positions - (x,y) coordinates - from the database.
        #print(position) # debug print.
        self.pos[0] = position[0] # the attribute in place [0] (x) equals to the (x) coordinate from the object of the database.
        self.pos[1] = position[1] # the attribute in place [1] (y) equals to the (y) coordinate from the object of the database.
        #print("X is: " + str(self.pos[0])) # debug print
        #print("Y is: " + str(self.pos[1])) # debug print
    
    def get_name(self): # method for getting the name (human-friendly) from the database
        name = borders_doc.find_one({"_id":(self.id_num)}) # locate the matching "object" according to the territory's ID number.
        name = name["name"] # get the actual 'name' string from the located "object" from the document.
        self.name = name # assign the located name to the name-attributes of the class.
        #print("The name is: " + str(self.name)) # debug print

    def get_borders(self): # method for getting the ID-numbers of the bordering territories from the database.
        borders = borders_doc.find_one({"_id":(self.id_num)}) # locate the matching "object" according to the territory's ID number.
        borders = borders["borders"] # get the actual list of ID-numbers of the bordering territories.
        self.borders = borders # assign the located list to the borders-attribute of the class. 
        #print(borders) # debug print

    def get_png_names(self): # method for getting the blob-names (all 7 colors) from the database.
        png_name = blob_links_doc.find_one({"valid_ids":(self.id_num)}) # locate the matching "object" according to the territory's ID number.
        png_name = png_name["strings"] # get the actual 'strings' string from the located "object" from the document. 
        self.blob_names = png_name # assign the located list to the blob_names-attribute of the class. 
        #print("COLORS ARE:") # debug print
        #print(self.blob_names[0]) # green # debug print
        #print(self.blob_names[1]) # blue # debug print
        #print(self.blob_names[2]) # yellow # debug print
        #print(self.blob_names[3]) # red # debug print
        #print(self.blob_names[4]) # orange # debug print
        #print(self.blob_names[5]) # purple # debug print
        #print(self.blob_names[6]) # grey # debug print
    
    def get_bonus_group(self): # method for getting the bonus-group from the database
        #print("The ID is: " + str(self.id_num)) # debug print
        bonus_group = bonus_doc.find_one({"territories":(self.id_num)}) # locate the matching "object" according to the territory's ID number.
        #print("The type is: " + str((bonus_group)["territories"])) # debug print
        bonus_group = bonus_group["territories"] # get the actual list from the located "object" from the document.
        self.bonus_group = bonus_group # assign the located list to the bonus_group-attribute of the class. 
        #print(self.bonus_group) # debug print

    def get_dots (self): # method for getting the list of dots (of the specific territory) from the database
        dots = dots_doc.find_one({"_id":(self.id_num)}) # locate the matching "object" according to the territory's ID number.
        dots = dots["dots"] # get the actual list of dots from the located "object" from the document.
        self.dots = dots # assign the located list to the dots-attribute of the class.


    def zero_forces(self): # method to apply zero forces to the specified territory.
        self.force_no = int(0) # apply zero forces to the specified territory.


    def load_blobs(self): # method for getting the PNG files, from the game-folder.
        #blob_name = self.blob_names[self.controller] # variable not in use.
        self.real_blobs[0] = pygame.image.load(self.blob_names[0]) # GREEN # load the 'green' version of the PNG file from the game-folder.
        self.real_blobs[1] = pygame.image.load(self.blob_names[1]) # BLUE # load the 'blue' version of the PNG file from the game-folder.
        self.real_blobs[2] = pygame.image.load(self.blob_names[2]) # YELLOW # load the 'yellow' version of the PNG file from the game-folder.
        self.real_blobs[3] = pygame.image.load(self.blob_names[3]) # RED # load the 'red' version of the PNG file from the game-folder.
        self.real_blobs[4] = pygame.image.load(self.blob_names[4]) # ORANGE # load the 'orange' version of the PNG file from the game-folder.
        self.real_blobs[5] = pygame.image.load(self.blob_names[5]) # PURPLE # load the 'purple' version of the PNG file from the game-folder.
        self.real_blobs[6] = pygame.image.load(self.blob_names[6]) # GREY # load the 'grey' version of the PNG file from the game-folder.

    def stick_blob(self): # method for applying the loaded blob onto the PyGame window.
        self.screen.blit(self.real_blobs[self.controller], (self.pos[0], self.pos[1])) # apply the loaded blob...
        pygame.display.update() # refresh the PyGame window.
    
    def get_force_no_point(self): # method for getting the point (x,y) of the number of forces for that territory
        text_pos = force_doc.find_one({"_id":(self.id_num)}) # method for getting the text-mid-point from the database
        text_pos = text_pos["force_text"] # get the actual (x,y) coordinates from the located "object" from the document.
        #print("text_pos is: " + str(text_pos)) # debug print
        #print("text_pos (X) is: " + str(text_pos[0])) # debug print
        #print("text_pos (Y) is: " + str(text_pos[1])) # debug print
        #print("self.text_force_point is: " + str(self.text_force_point)) # debug print
        self.text_force_point[0] = text_pos[0] # assign the located X coordinate to the [0] cell of the text-force attribute of the object.
        self.text_force_point[1] = text_pos[1] # assign the located Y coordinate to the [1] cell of the text-force attribute of the object.
        #print(self.text_force_point) # debug print

    def stick_force_no(self, num): # method for appliying the force-number onto the applied blob.
        if (num == 0): # 0 = default color - (0,0,1) black
            color = (0,0,1)
        elif (num == 1): # 1 = fortify color - (0,255,255) cyan
            color = (0,255,255)
        elif (num == 2): # attack color - (119,0,0) dark-red
            color = (119,0,0)
        elif (num == 3): # defense color - (2,0,132) dark-blue
            color = (2,0,132)
        elif (num == 4): # move color - (43,255,107) (both source + destination same color) light-green
            color = (43,255,107)
        font1 = pygame.font.Font('freesansbold.ttf', 25) # initialize the font.
        text = font1.render(str(self.force_no), True, color) # initialize the text. ######
        textRect = text.get_rect() # initialize the rectangle - which acts as a frame to the text.
        textRect.center = (self.text_force_point[0]+15, self.text_force_point[1]+15) # determine the position the rectangle
        self.screen.blit(text, textRect) # apply the text onto the PyGame window.
        pygame.display.update() # refresh the PyGame window.

    def give_screen (self, screen): # method for giving the screen to the territory-object.
        self.screen = screen # assign the screen to the 'screen' attribute of the territory-object.

    def init_territory(self, selected_map): # method for initializing the territory-object (initialize all basic attributes)
        self.get_position() # load 'get_position' method.
        self.get_name() # load 'get_name' method.
        self.get_borders() # load 'get_borders' method.
        self.get_png_names() # load 'get_png_names' method.
        self.get_bonus_group() # load 'get_bonus_group' method.
        self.get_dots() # load 'get_dots' method.
        self.get_force_no_point() # load 'get_force_no_point' method.
        #self.zero_forces() # method not in use.
        self.load_blobs() # load 'load_blobs' method.
        self.get_res(selected_map) # load "get_res" with "selected-map" inserted.
        #self.get_screen() # method not in use.

### TESTER ###
#screen = pygame.display.set_mode((1300,700)) # set screen 2D dimentions.
#game_map = pygame.image.load("quick-triangles (dark).png")
#screen.blit(game_map,(0,0))
#selected_map = int(4)

#edge_lwr = int(162)
#edge_upr = int(166)

#arr_territories = []
#for cnt in range(edge_lwr, edge_upr, 1):
#    arr_territories.append(Territory(cnt, 0,0,0,0,[],[],4,50,[],[],screen))
#    arr_territories[cnt - edge_lwr].controller = int(6) # COLOR
#for cnt in range(edge_lwr, edge_upr, 1):
#    arr_territories[cnt - edge_lwr].init_territory(1)
#for cnt in range(edge_lwr, edge_upr, 1):
#    arr_territories[cnt - edge_lwr].stick_blob()
#for cnt in range(edge_lwr, edge_upr, 1):
#    arr_territories[cnt - edge_lwr].stick_force_no()
#pygame.display.update()
#input("\nDONE!\n")