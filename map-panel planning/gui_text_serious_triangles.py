import pygame
pygame.init()
from button_class import Button
screen = pygame.display.set_mode((1000,700))
game_map = pygame.image.load('serious-triangles (dark).png')
#screen.fill((255,255,255))
screen.blit(game_map,(175,0))
#screen.fill((255,255,255))

pygame.draw.lines(screen, (255,255,255), False, [(0,500),(1227,500)], 3)
pygame.display.update()
# screen.fill((255,255,255))

# WHAT TEXT DO WE NEED?
# FORTIFY # 7
# 012345, click on territories to fortify! # 40
# ABCDEF has been fortified! # 26
# north-west-territory has been fortified! # 40
# ACEGHK has been fortified! # 26
# ATTACK # 6 chars
# 012345, select attacking territory! # 35
# 012345, select territory to attack! # 35
# MOVE # 4
# 012345, select source territory! # 32
# 012456, select destination territory! # 37

# 012345, you cannot attack your allies. Try again.
# 012345, not enough forces to move.
# 012345 is attacking 543210
#
# waiting for 012345 to fortify forces
# waiting for 012345 to attack
# waiting for 012345 to move forces

# 012345, INVALID MOVE! DOES NOT BOARD!

def one_valued_dice(x,y,color):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+18,y+18), 4, 0)


class gui_text:
    def __init__ (self, text, size, default_color, dimen, screen):
        self.text = text
        self.size = size
        self.default_color = default_color
        self.font = 0
        self.dimen = dimen
        self.screen = screen

    def get_default_color(self, back_mode):
        if (back_mode == int(0)): # 0=DARK
            self.default_color = (255,255,255) # WHITE
        else: # 1=LIGHT
            self.default_color = (0,0,0) # BLACK

    def get_font (self):
        self.font = pygame.font.Font('freesansbold.ttf', self.size)

    def insert_gui_text (self, ply_color):
        #print(len(self.dimen))
        #pygame.draw.rect(screen, self.color, (self.dimen[0],self.dimen[1],self.dimen[2],self.dimen[3]), self.thick)
        text = self.font.render(self.text, True, ply_color)
        #textRect = text.get_rect()
        #textRect.center = (self.dimen[0],self.dimen[2],self.dimen[1],self.dimen[3])
        screen.blit(text, (self.dimen[0],self.dimen[1]))
        pygame.display.update()

    #def calculate_remove_gui (self):
        #print("the length of text is: " + str(len(self.text)))
        #self.length_remove = (len(self.text))
        #print("self.length_remove is: " + str(self.length_remove))


    def remove_gui_text (self):
        length_remove = len(self.text)
        print("The length is: " + str(length_remove))
        pygame.display.update()
        pygame.draw.rect(screen, (0,0,0), (self.dimen[0],self.dimen[1],self.dimen[2]*self.size*length_remove*0.6+16,self.dimen[3]))
        # self.default_color
        pygame.display.update()

# SERIOUS-TRIANGLES
gt0 = gui_text("ATTACK", 40, 0, [430,505,1,40], screen) # level 1
gt2 = gui_text("012345, select fortifying territory!", 20, 0, [338,547,1,20], screen) # level 2
gt1 = gui_text("012345, select attacking territory!", 20, 0, [15,577,1,20], screen) # level 3
gt5 = gui_text("15 remaining", 20, 0, [450,577,1,20], screen) # level 4
gt3 = gui_text("012345, select territory to attack!", 20, 0, [660,577,1,20], screen) # level 5
gt4 = gui_text("ATTACKER: Alaska", 20, 0, [15,607,1,20], screen) # level 6
one_valued_dice(455,607,(34,139,34)) # level 7
one_valued_dice(545,607,(34,139,34)) # level 8
gt6 = gui_text("ATTACKED: Alberta", 20, 0, [660,607,1,20], screen) # level 9


gt0.get_default_color(0)
gt0.get_font()
gt0.insert_gui_text((34,139,34))

gt1.get_default_color(0)
gt1.get_font()
gt1.insert_gui_text((34,139,34))

gt2.get_default_color(0)
gt2.get_font()
gt2.insert_gui_text((34,139,34))

gt3.get_default_color(0)
gt3.get_font()
gt3.insert_gui_text((34,139,34))

gt4.get_default_color(0)
gt4.get_font()
gt4.insert_gui_text((34,139,34))

gt5.get_default_color(0)
gt5.get_font()
gt5.insert_gui_text((34,139,34))

gt6.get_default_color(0)
gt6.get_font()
gt6.insert_gui_text((34,139,34))

#one_valued_dice(455,607,(34,139,34)) # level 7
#one_valued_dice(545,607,(34,139,34)) # level 8

back_mode = int(0)

# serious-triangles
#auto_attack_button = Button(1, "MANUAL", back_mode, (305,645,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#skip_move_button = Button(1, "SKIP", back_mode, (448,645,140,50), 5, 6, 0, screen) # initiate the "skip" button.
#manual_attack_button = Button(1, "AUTO", back_mode, (590,645,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#skipMove_autoFortify_button = Button(1, "SKIP", back_mode, (853,645,140,50), 5, 6, 0, screen) # initiate the "skip" button.
#save_button = Button(1, "SAVE", back_mode, (853,509,140,50), 5, 6, 0, screen) # initiate the "skip" button.

while (True):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mouse)
        if (click[2] == 1):
            gt0.remove_gui_text()
            gt1.remove_gui_text()
            gt2.remove_gui_text()
            gt3.remove_gui_text()
            gt4.remove_gui_text()
        elif (click[0] == 1):
            gt0.insert_gui_text((34,139,34))
            gt1.insert_gui_text((34,139,34))
            gt2.insert_gui_text((34,139,34))
            gt3.insert_gui_text((34,139,34))
            gt4.insert_gui_text((34,139,34))