import pygame
pygame.init()
class gui_text:
    def __init__ (self, text_string, text_size, default_color, dimen, screen):
        self.text_string = text_string
        self.text_size = text_size
        self.default_color = default_color
        self.font = 0
        self.dimen = dimen
        self.screen = screen

    def init_gui_text (self, back_mode):
        self.get_default_color(back_mode)
        self.get_font()

    def get_default_color(self, back_mode):
        if (back_mode == int(0)): # 0=DARK
            self.default_color = (0,0,0) # BLACK - blends with the 'dark' background.
        else: # 1=LIGHT
            self.default_color = (255,255,255) # WHITE - blends with the 'light' background.

    def get_font (self):
        self.font = pygame.font.Font('freesansbold.ttf', self.text_size)

    def insert_gui_text (self, ply_color):
        if (ply_color == int(0)): #0=DARK
            ply_color = (255,255,255)
        elif (ply_color == int(1)): #1=LIGHT
            ply_color = (0,0,0)
        text = self.font.render(self.text_string, True, ply_color)
        self.screen.blit(text, (self.dimen[0],self.dimen[1]))
        pygame.display.update()

    def change_text (self, text):
        self.text_string = text

    def remove_gui_text (self):
        length_remove = len(self.text_string)
        #print("The length is: " + str(length_remove))
        pygame.display.update()
        #print("self.dimen[0] is: " + str(self.dimen[0]))
        #print("self.dimen[1] is: " + str(self.dimen[1]))
        #print("self.dimen[2] is: " + str(self.dimen[2]))
        #print("self.dimen[3] is: " + str(self.dimen[3]))

        pygame.draw.rect(self.screen, self.default_color, (self.dimen[0],self.dimen[1],self.dimen[2]*self.text_size*length_remove*0.6+16,self.dimen[3]), 0)
        
        #pygame.draw.rect(screen, (0,255,0), (self.dimen[0],self.dimen[1],self.dimen[2],self.dimen[3]), self.thick) # apply the new rectangle - but this time, with color (0,255,0), green.
        pygame.display.update()