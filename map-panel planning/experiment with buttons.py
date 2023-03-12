import pygame
pygame.init()
from button_class import Button
from guiText_class import gui_text
screen = pygame.display.set_mode((1100,700))
game_map = pygame.image.load('menu5dark.png')
#screen.fill((255,255,255))
screen.blit(game_map,(0,0))
#screen.fill((255,255,255))

pygame.draw.lines(screen, (255,255,255), False, [(0,500),(1227,500)], 3)

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

back_mode = int(0)

allies1 = Button(1, "ALLIES-1", back_mode, (280,70,140,50), 5, 6, 0, screen) # initiate the "auto" button.
allies2 = Button(1, "ALLIES-2", back_mode, (475,70,140,50), 5, 6, 0, screen) # initiate the "auto" button.
allies3 = Button(1, "ALLIES-3", back_mode, (670,70,140,50), 5, 6, 0, screen) # initiate the "auto" button.
reset = Button(1, "RESET", back_mode, (50,70,140,50), 5, 6, 0, screen) # initiate the "reset-allies" button.


pygame.draw.lines(screen, (255,0,0), False,[(670,70),(810,120)],5)
pygame.draw.lines(screen, (255,0,0), False,[(810,70),(670,120)],5)

pygame.draw.rect(screen, (255,0,0), (10,255,1080,50), 0) # draw the frame (rectangle) of the button.

pygame.display.update()

lv1_gt = gui_text("OK", 40, 0, (50,230, 1, 40), screen) # this is the header: "FORTIFY" / "ATTACK" / "MOVE"
lv1_gt.init_gui_text(back_mode)

# 2 PLAYER SELECTION
player1 = Button(1, "1234567", back_mode, (375,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
player2 = Button(1, "1234567", back_mode, (575,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.

# 3 PLAYER SELECTION
#player1 = Button(1, "1234567", back_mode, (280,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player2 = Button(1, "1234567", back_mode, (475,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player3 = Button(1, "1234567", back_mode, (670,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.

# 4 PLAYER SELECTION
#player1 = Button(1, "1234567", back_mode, (175,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player2 = Button(1, "1234567", back_mode, (375,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player3 = Button(1, "1234567", back_mode, (575,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player4 = Button(1, "1234567", back_mode, (775,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.

# 5 PLAYER SELECTION
#player1 = Button(1, "1234567", back_mode, (85,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player2 = Button(1, "1234567", back_mode, (280,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player3 = Button(1, "1234567", back_mode, (475,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player4 = Button(1, "1234567", back_mode, (670,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player5 = Button(1, "1234567", back_mode, (865,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.

# 6 PLAYER SELECTION
#player1 = Button(1, "1234567", back_mode, (75,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player2 = Button(1, "1234567", back_mode, (237,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player3 = Button(1, "1234567", back_mode, (399,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player4 = Button(1, "1234567", back_mode, (561,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player5 = Button(1, "1234567", back_mode, (723,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.
#player6 = Button(1, "1234567", back_mode, (885,200,140,50), 5, 6, 0, screen) # initiate the "auto" button.

pygame.draw.rect(screen, (255,0,0), (50,100,200,50), 0) # draw the frame (rectangle) of the button.
lv1_gt.change_text("5")
lv1_gt.insert_gui_text((0,255,0))

#skip_button = Button(1, "SKIP", back_mode, (853,645,140,50), 5, 6, 0, screen) # initiate the "skip" button.

while (True):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mouse)