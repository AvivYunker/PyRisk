# arr_dem = dimentions of rectangle
# length = maximum number of characters.
# color = according to "back_mode".
# example of code: 123-abc-456
import pygame
pygame.init()
#X = int(1100)
#Y = int(700)
#screen = pygame.display.set_mode((X,Y))
#WHITE = (255,255,255)
#screen.fill(WHITE)

class textBox:
    def __init__ (self, arr_dem, length, color, font, thick, screen, level, strr):
        self.arr_dem = arr_dem
        self.length = length
        self.color = color
        self.deleting_color = int(0)
        self.font = font
        self.thick = thick
        self.screen = screen
        self.level = level
        self.strr = strr

    def initiate_text_box(self):
        self.get_font()
        self.get_color()
        self.draw_text_box()

    def get_font (self):
        if (self.font == int(0)):
            self.font = pygame.font.Font('freesansbold.ttf', 20)
        elif (self.font == int(1)):
            self.font = pygame.font.Font('freesansbold.ttf', 30)

    def get_color (self):
        if (self.color == int(0)): # 0=BLACK
            self.color = (255,255,255)
            self.deleting_color = (0,0,0)
            #print("Changed to WHITE!")
        else: # 1=WHITE
            self.color = (0,0,0)
            self.deleting_color = (255,255,255)
            #print("Changed to BLACK!")

    def draw_text_box (self):
        pygame.draw.rect(self.screen, self.color, (self.arr_dem[0]-10,self.arr_dem[1],self.arr_dem[2],self.arr_dem[3]+2),5)
        pygame.display.update()

    def on_hover_text_box (self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if ((self.arr_dem[0]+self.arr_dem[2] > mouse[0] > self.arr_dem[0]) and (self.arr_dem[1]+self.arr_dem[3] > mouse[1] > self.arr_dem[1])):
            self.insert_text(mouse)
            pygame.display.update()
            #print("The code (in CLASS) is: " + str(self.strr))
            return self.strr
        else:
            pass
            #self.draw_text_box()

    def on_click_text_box (self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if ((click[0] == int(1)) and ((self.arr_dem[0] + self.arr_dem[2] > mouse[0] > self.arr_dem[0]) and (self.arr_dem[1] + self.arr_dem[3] > mouse[1] > self.arr_dem[1]))):
            pygame.draw.rect(self.screen, (0,255,0), (self.arr_dem[0], self.arr_dem[1], self.arr_dem[2], self.arr_dem[3]+2), self.thick)
            text = self.font.render(self.strr, True, (0,255,0))
            textRect = text.get_rect()
            textRect.center = (self.arr_dem[0]+self.arr_dem[2]/2,self.arr_dem[1]+self.arr_dem[3]/2)
            self.screen.blit(text, textRect)
            #while ((self.arr_dem[0] + self.arr_dem[2] > mouse[0] > self.arr_dem[0]) and (self.arr_dem[1] + self.arr_dem[3] > mouse[1] > self.arr_dem[1])):
            pygame.display.update()

    def reset_string (self):
        self.strr = str("")

    def insert_text (self, mouse):
        pygame.draw.rect(self.screen, (255,255,0), (self.arr_dem[0]-10,self.arr_dem[1],self.arr_dem[2],self.arr_dem[3]+2),5)
        pygame.display.update()
        cont = int(1)
        #print("INSERT TEXT")
        while (cont == int(1) and (self.arr_dem[0] + self.arr_dem[2] > mouse[0] > self.arr_dem[0]) and (self.arr_dem[1] + self.arr_dem[3] > mouse[1] > self.arr_dem[1])):
            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()
            #print("The level is: " + str(self.level))
            #print("I'm in!")
            if (click[2] == int(1)):
                cont = int(0)
            #print("Type of level is: " + str(type(self.level)))
            #print("Type of arr_dem[0] is: " + str(type(self.arr_dem[0])))
            if (self.level < self.arr_dem[0]):
                self.level += 30
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                for cnt in range(0, len(keys), 1):
                    if (keys[cnt] == 1):
                        if (str(cnt) == '8'):
                            self.strr = self.strr[:-1]
                            self.remove_char_gui([self.level, self.arr_dem[1]+18,34,50])
                            continue
                        if ((len(self.strr) < self.length) and ((97 <= cnt <= 122) or (48 <= cnt <= 57) or (cnt == 45))):
                            #print("bool is: " + str(len(self.strr) < self.length))
                            self.add_char_gui(cnt,[self.level,self.arr_dem[1]+15,20,20])
                            #level += 30
                            #print("CHR is: " + chr(cnt))
                            #print("VAL is: " + str(cnt))
                            #print("self.length is: " + str(self.length))
                            #print("strr.length is: " + str(len(self.strr)))
                            self.strr += chr(cnt)
                        #if (len(self.strr) == int(3) or len(self.strr) == int(7)):
                            #self.strr += chr(45)
                            #level = self.add_char_gui(45,[level,self.arr_dem[1],20,20])
                        #print("self.level is: " + str(self.level))
                        pygame.event.wait()
        self.draw_text_box()

    def add_char_gui (self, val, arr_text):
        self.level += 30
        font = pygame.font.Font('freesansbold.ttf', 45) # 'PyRisk' logo.
        #color = (0,255,0)
        text1 = font.render(chr(val), True, self.color)
        textRect1 = text1.get_rect()
        textRect1.center = ((arr_text[0]+(arr_text[2]/2)),(arr_text[1]+(arr_text[3]/2)))
        self.screen.blit(text1, textRect1)
        pygame.display.update()
        #print("self.arr_dem[0] is: " + str(self.arr_dem[0]))'

    def remove_char_gui (self, arr_text):
        if (self.level > self.arr_dem[0]):
            self.level -= 30
            #print("after char-remove, level is: " + str(self.level))
            pygame.draw.rect(self.screen, (self.deleting_color), (arr_text[0]-37,arr_text[1]-15,arr_text[2],arr_text[3]-5), 0)
            pygame.display.update()

#font1 = pygame.font.Font('freesansbold.ttf', 45) # 'PyRisk' logo.
#strr = str("")
#tb1 = textBox((200,100,100,50), 11, (0,0,0), font1, 5,screen, strr)
#tb1.draw_text_box()
#while (True):
    #for event in pygame.event.get():
        #tb1.on_hover_text_box()
        #tb1.on_click_text_box()
        #tb1.insert_text()