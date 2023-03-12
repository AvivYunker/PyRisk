import pygame # import the PyGame library.
pygame.init() # initialize the PyGame library.
import pygame.key # get the "pygame.key" module from the PyGame library.
class Button: # define the "Button" class.
    def __init__ (self, font, text, color, dimen, thick, value, img, screen): #(8) the attributes of the "territory" class.
        self.font = font # the font of the button-object.
        self.text = text # the text of the button-object.
        self.color = color # the color of the button-object.
        self.dimen = dimen # the dimentions of the button-object.
        self.thick = thick # the thickness of the button-object.
        self.value = value # the returned value of the button-object.
        self.img = img # the PNG file that is in center of the button-object.
        self.screen = screen
        self.init_button() # method for initializing a button-object.
        self.get_img() # method for getting the image of the button-object.
        self.put_img() # method for putting the image of the button-object.

    def get_img (self): # method for getting the PNG file.
        if (self.img != 0): # if the number is NOT zero, then...
            self.img = pygame.image.load(self.img) # load the image into the 'img' attribute of the object.
    
    def put_img (self): # method for applying the loaded PNG file.
        if (self.img != 0): # if the number is NOT zero, then...
            self.screen.blit(self.img,(self.dimen[0],self.dimen[1])) # apply the loaded PNG file onto the PyGame Window.
            pygame.display.update() # refresh the PyGame window.

    def init_button(self): # method for initializing the button.
        self.get_font() # call the "get_font" method for getting the font.
        self.get_color() # call the "get_color" method for getting the color.
        self.draw_button() # call the "draw_button" method to apply the button onto the screen.

    def button_functional(self, val): # method for functionalizing the button.
        self.button_on_hover(val) # method for determining if the mouse is hovering over the button.
        val = self.button_on_click(val) # value that is being returned from the "click" function - if the button has been clicked on.
        return val # return the value - to wherever is has been called. 

    def get_font (self): # method for getting the font.
        # there are 3 types of fonts, each different by their sizes.
        if (self.font == int(1)): # if the assigned number in the start was 1, then...
            self.font = pygame.font.Font('freesansbold.ttf', 30) # font size is 30
        elif (self.font == int(2)): # if the assigned number in the start was 2, then...
            self.font = pygame.font.Font('freesansbold.ttf', 40) # font size is 40
        elif (self.font == int(3)): # if the assigned number in the start was 3, then...
            self.font = pygame.font.Font('freesansbold.ttf', 50) # font size is 50

    def get_color (self): # method for setting both the frame and the text color.
        if (self.color == int(0)): # 0=BLACK - if the color of the background is black, the button must be white, then...
            self.color = (255,255,255) # WHITE
        else: # 1=WHITE - if the color of the background is white, the button must be black, then...
            self.color = (0,0,0) # BLACK
    
    def draw_button (self): # method for applying the button onto the PyGame window.
        #print(len(self.dimen)) # debug print
        pygame.draw.rect(self.screen, self.color, (self.dimen[0],self.dimen[1],self.dimen[2],self.dimen[3]), self.thick) # draw the frame (rectangle) of the button.
        text = self.font.render(self.text, True, self.color) # define the text of the button
        textRect = text.get_rect() # define the rectangle that the text will be inside of.
        textRect.center = ((self.dimen[0]+(self.dimen[2]/2)),(self.dimen[1]+(self.dimen[3]/2))) # define the center of the rectangle.
        self.screen.blit(text, textRect) # apply the text and rectangle onto the screen.
        pygame.display.update() # refresh the PyGame window.

    def button_on_hover(self, val): # method for determining if the mouse is hovering over the button.
        mouse = pygame.mouse.get_pos() # get the position (x,y) coordinates of the mouse.
        click = pygame.mouse.get_pressed() # get the boolean value for mouse-click.
        if ((self.dimen[0]+self.dimen[2] > mouse[0] > self.dimen[0] and self.dimen[1]+self.dimen[3] > mouse[1] > self.dimen[1]) and (val != self.value)): # if the mouse is within the rectangle of the button.
            pygame.draw.rect(self.screen, (255,255,0), (self.dimen[0],self.dimen[1],self.dimen[2],self.dimen[3]), self.thick) # apply the new rectangle - but this time, with color (255,255,0), yellow.
            text = self.font.render(self.text, True, (255,255,0)) # define the text of the button.
            textRect = text.get_rect() # define the rectangle that the text will be inside of.
            textRect.center = ((self.dimen[0]+(self.dimen[2]/2)),(self.dimen[1]+(self.dimen[3]/2))) # define the center of the rectangle
            self.screen.blit(text, textRect) # apply the text and rectangle onto the screen.
            #Button.button_on_click(self) # already has a method separately.
        elif (val == self.value) :
            pass
        else:
            Button.draw_button(self) # draw the button with the default colors (black button for white-background / white button for black-background).
    
    def button_on_click(self, val): # method for determining if the button has been clicked on.
        mouse = pygame.mouse.get_pos() # get the position (x,y) coordinates of the mouse.
        click = pygame.mouse.get_pressed() # get the boolean value for mouse-click.
        if ((click[0] == int(1)) and (self.dimen[0]+self.dimen[2] > mouse[0] > self.dimen[0] and self.dimen[1]+self.dimen[3] > mouse[1] > self.dimen[1])):
            pygame.draw.rect(self.screen, (0,255,0), (self.dimen[0],self.dimen[1],self.dimen[2],self.dimen[3]), self.thick) # apply the new rectangle - but this time, with color (0,255,0), green.
            text = self.font.render(self.text, True, (0,255,0)) # define the text of the button.
            textRect = text.get_rect() # define the rectangle that the text will be inside of.
            textRect.center = ((self.dimen[0]+(self.dimen[2]/2)),(self.dimen[1]+(self.dimen[3]/2))) # define the center of the rectangle
            self.screen.blit(text, textRect) # apply the text and rectangle onto the screen.
            pygame.display.update() # refresh the PyGame window.
            return self.value # return the value that the button is associated with.
        else: # if the position of the mouse is NOT over the rectangle of the mouse, then...
            return val # return the previous value that was contained, not nessecarily the value associated with this specific button.

    def draw_button_cross(self):
        pygame.draw.lines(self.screen, self.color, False, [(self.dimen[0],self.dimen[1]),(self.dimen[0]+self.dimen[2],self.dimen[1]+self.dimen[3])], 5)
        pygame.draw.lines(self.screen, self.color, False, [(self.dimen[0]+self.dimen[2],self.dimen[1]),(self.dimen[0],self.dimen[1]+self.dimen[3])], 5) #5-players
        pygame.display.update()    


    def draw_confirmation (self):
        pygame.draw.rect(self.screen, (0,255,0), (self.dimen[0],self.dimen[1],self.dimen[2],self.dimen[3]), self.thick) # apply the new rectangle - but this time, with color (0,255,0), green.

#five_players = Button(3, "5", back_mode, (665,115,130,80), 5, 5, 0, screen) # initiate the "5-players" button.
#pygame.draw.lines(screen, (255,0,0), False, [(665,115),(795,195)], 5) #5-players
#pygame.draw.lines(screen, (255,0,0), False, [(795,115),(665,195)], 5) #5-players



    #def give_value (self):
        #click = pygame.mouse.get_pressed()
        #if (click[0] == int(1)):
            #return self.value

    #def __init__ (self, font, text, color, dimen, value):
#button1 = Button(3, "B1", 1, [50,50,100,60], 5, 15)
#button1.get_dimentions()
#button1.get_font()
#button1.get_color()
#button1.draw_button()
#button1.button_on_hover()
#while (True):
    #for event in pygame.event.get():
        #mouse = pygame.mouse.get_pos()
        #button1.button_on_hover()
        #button1.button_on_click()

#input("DONE!")