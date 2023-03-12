# arr_dem = dimentions of rectangle
# length = maximum number of characters.
# color = according to "back_mode".
# example of code: 123-abc-456
import pygame
pygame.init()
X = int(1100)
Y = int(700)
screen = pygame.display.set_mode((X,Y))
WHITE = (255,255,255)
screen.fill(WHITE)

class textBox:
    def __init__ (self, arr_dem, length, color, font, thick, screen, strr):
        self.arr_dem = arr_dem
        self.length = length
        self.color = color
        self.font = font
        self.thick = thick
        self.screen = screen
        self.strr = strr

    def text_box_functional(self):
        self.get_font()
        self.get_color()
        self.draw_button()

    def get_font (self):
        if (self.font == int(0)):
            self.font = pygame.font.Font('freesansbold.ttf', 25)
        elif (self.font == int(1)):
            self.font = pygame.font.Font('freesansbold.ttf', 25)

    def get_color (self):
        if (self.color == int(0)): # 0=BLACK
            self.color = (255,255,255)
        else: # 1=WHITE
            self.color = (0,0,0)

    def draw_text_box (self):
        pygame.draw.rect(self.screen, self.color, (self.arr_dem[0],self.arr_dem[1],self.arr_dem[2],self.arr_dem[3]),5)
        pygame.display.update()

    def on_hover_text_box (self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if ((self.arr_dem[0]+self.arr_dem[2] > mouse[0] > self.arr_dem[0]) and (self.arr_dem[1]+self.arr_dem[3] > mouse[1] > self.arr_dem[1])):
            pygame.draw.rect(self.screen, (255,255,0), (self.arr_dem[0],self.arr_dem[1],self.arr_dem[2],self.arr_dem[3]),5)
            pygame.display.update()
        else:
            self.draw_text_box()

    def on_click_text_box (self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if ((click[0] == int(1)) and ((self.arr_dem[0] + self.arr_dem[2] > mouse[0] > self.arr_dem[0]) and (self.arr_dem[1] + self.arr_dem[3] > mouse[1] > self.arr_dem[1]))):
            pygame.draw.rect(self.screen, (0,255,0), (self.arr_dem[0], self.arr_dem[1], self.arr_dem[2], self.arr_dem[3]), self.thick)
            text = self.font.render(self.strr, True, (0,255,0))
            textRect = text.get_rect()
            textRect.center = (self.arr_dem[0]+self.arr_dem[2]/2,self.arr_dem[1]+self.arr_dem[3]/2)
            self.screen.blit(text, textRect)
            #while ((self.arr_dem[0] + self.arr_dem[2] > mouse[0] > self.arr_dem[0]) and (self.arr_dem[1] + self.arr_dem[3] > mouse[1] > self.arr_dem[1])):
            pygame.display.update()


    def insert_text (self):
        click = pygame.mouse.get_pressed()
        cont = int(1)
        print("INSERT TEXT")
        level = int(50)
        while (cont):
            if (click[2] == int(1)):
                cont = int(0)
            if (level < 50):
                level += 30
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                for cnt in range(0, len(keys), 1):
                    if (keys[cnt] == 1):
                        if (str(cnt) == '13'):
                            cont = int(0)
                            break
                        elif (str(cnt) == '8'):
                            self.strr = self.strr[:-1]
                            level = self.remove_char_gui([level, self.arr_dem[1],34,50])
                            #if (len(self.strr) == int(8) or len(self.strr) == int(4)):
                                #self.strr = self.strr[:-1]
                                #level = self.remove_char_gui([level, self.arr_dem[1],34,50])
                            #level -= 30
                            continue
                        if (len(self.strr) < self.length):
                            level = self.add_char_gui(cnt,[level,self.arr_dem[1],20,20])
                            #level += 30
                            #print("CHR is: " + chr(cnt))
                            #print("VAL is: " + str(cnt))
                            self.strr += chr(cnt)
                        #if (len(self.strr) == int(3) or len(self.strr) == int(7)):
                            #self.strr += chr(45)
                            #level = self.add_char_gui(45,[level,self.arr_dem[1],20,20])
                        print("level is: " + str(level))
                        pygame.event.wait()

    def add_char_gui (self, val, arr_text):
        print(str(val))
        font = pygame.font.Font('freesansbold.ttf', 45) # 'PyRisk' logo.
        color = (0,255,0)
        #pygame.draw.rect(screen, color, (arr_dem[0],arr_dem[1],arr_dem[2],arr_dem[3]),5)
        text1 = font.render(chr(val), True, color)
        textRect1 = text1.get_rect()
        textRect1.center = ((arr_text[0]+(arr_text[2]/2)),(arr_text[1]+(arr_text[3]/2)))
        screen.blit(text1, textRect1)
        pygame.display.update()
        arr_text[0] += 30
        return arr_text[0]

    def remove_char_gui (self, arr_text):
        arr_text[0] -= 30
        pygame.draw.rect(screen, (0,0,0), (arr_text[0]-7,arr_text[1]-10,arr_text[2],arr_text[3]), 0)
        pygame.display.update()
        #arr_text[0] -= 30
        return arr_text[0]

font1 = pygame.font.Font('freesansbold.ttf', 45) # 'PyRisk' logo.
strr = str("")
tb1 = textBox((200,100,100,50), 11, (0,0,0), font1, 5,screen, strr)
tb1.draw_text_box()
while (True):
    for event in pygame.event.get():
        tb1.on_hover_text_box()
        tb1.on_click_text_box()
        tb1.insert_text()