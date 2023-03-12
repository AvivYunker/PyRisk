import pygame
pygame.init()
from icons import *
screen = pygame.display.set_mode((1227,828)) # set screen 2D dimentions.
game_map = pygame.image.load('countries (light).png')
screen.fill((255,255,255))
screen.blit(game_map,(0,0))
pygame.draw.lines(screen, (0,0,0), False, [(0,628),(1227,628)], 3)


font1 = pygame.font.Font('freesansbold.ttf', 30) # 'PyRisk' logo.
font2 = pygame.font.Font('freesansbold.ttf', 40) # 'How many players?' / 'light / dark mode'
font3 = pygame.font.Font('freesansbold.ttf', 50) # 'PROCEED'

# COLORS:
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

GREEN_PL = (34,139,34)
BLUE_PL = (0,95,190)
YELLOW_PL = (251,219,3)
RED_PL = (251,28,46)
ORANGE_PL = (255,102,0)
PURPLE_PL = (66,12,76)
GREY_PL = (110,110,110)

def create_text_box(text, font, color, arr_dem):
    #pygame.draw.rect(screen, color, (arr_dem[0],arr_dem[1],arr_dem[2],arr_dem[3]),5)
    text1 = font.render(text, True, color)
    textRect1 = text1.get_rect()
    textRect1.center = ((arr_dem[0]+(arr_dem[2]/2)),(arr_dem[1]+(arr_dem[3]/2)))
    screen.blit(text1, textRect1)
    pygame.display.update()

def create_text_box_rectangular (text, font, color, arr_dem):
    pygame.draw.rect(screen, color, (arr_dem[0],arr_dem[1],arr_dem[2],arr_dem[3]),5)
    text1 = font.render(text, True, color)
    textRect1 = text1.get_rect()
    textRect1.center = ((arr_dem[0]+(arr_dem[2]/2)),(arr_dem[1]+(arr_dem[3]/2)))
    screen.blit(text1, textRect1)
    pygame.display.update()

def erase_text_box (color, arr_dem):
    pygame.draw.rect(screen, color, (arr_dem[0],arr_dem[1],arr_dem[2],arr_dem[3]))

def one_valued_dice(x,y,color):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+18,y+18), 4, 0)

def two_valued_dice(x,y,color):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+10,y+10), 4, 0)
    pygame.draw.circle(screen, color, (x+24,y+24), 4, 0)

def three_valued_dice(x,y,color):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+8,y+8), 4, 0)
    pygame.draw.circle(screen, color, (x+17,y+17), 4, 0)
    pygame.draw.circle(screen, color, (x+26,y+26), 4, 0)

def four_valued_dice(x,y,color):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+10,y+10), 4, 0)
    pygame.draw.circle(screen, color, (x+24,y+10), 4, 0)
    pygame.draw.circle(screen, color, (x+10,y+24), 4, 0)
    pygame.draw.circle(screen, color, (x+24,y+24), 4, 0)

def five_valued_dice(x,y,color):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+8,y+8), 4, 0)
    pygame.draw.circle(screen, color, (x+26,y+8), 4, 0)
    pygame.draw.circle(screen, color, (x+8,y+26), 4, 0)
    pygame.draw.circle(screen, color, (x+26,y+26), 4, 0)
    pygame.draw.circle(screen, color, (x+17,y+17), 4, 0)

def six_valued_dice(x,y,color):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+9,y+8), 4, 0)
    pygame.draw.circle(screen, color, (x+9,y+17), 4, 0)
    pygame.draw.circle(screen, color, (x+9,y+26), 4, 0)
    pygame.draw.circle(screen, color, (x+25,y+8), 4, 0)
    pygame.draw.circle(screen, color, (x+25,y+17), 4, 0)
    pygame.draw.circle(screen, color, (x+25,y+26), 4, 0)

def force_move_arrow(x,y,color, length):
    pygame.draw.lines(screen, color, False, [(x,y),(x+length,y)], 15)
    pygame.draw.polygon(screen, color, [(x+length,y-20),(x+length+25,y),(x+length,y+20)], 0)


create_text_box("PLAYER1", font1, GREEN_PL, [410,620,50,50])
create_text_box(", Select territory to attack!", font1, BLACK, [670,620,50,50])
#create_text_box("Select territories to reinforce!", font1, BLACK, [700,620,50,50])
#create_text_box("Select territories to move forces!", font1, BLACK, [700,620,50,50])
create_text_box("western-united-states", font1, GREEN_PL, [275,630,50,100])
create_text_box("eastern-united-states", font1, RED_PL, [900,630,50,100])

create_text_box_rectangular("MANUAL", font1, GREEN_PL, [430,770,150,50])
create_text_box_rectangular("AUTO", font1, GREEN_PL, [600,770,150,50])


one_valued_dice(230,720,GREEN_PL)
two_valued_dice(270,720,BLUE_PL)
three_valued_dice(310,720,YELLOW_PL)

four_valued_dice(860,720,RED_PL)
five_valued_dice(900,720,ORANGE_PL)
six_valued_dice(940,720,PURPLE_PL)
six_valued_dice(980,720,GREY_PL)

force_move_arrow(460,680,BLUE, 280)

pygame.display.update()
while (True):
    for event in pygame.event.get():
        x = pygame.mouse.get_rel()[0]
        y = pygame.mouse.get_rel()[1]
        mouse = pygame.mouse.get_pos()
        print(mouse)
        print("(" + str(x) + "," + str(y) + ")")
        click = pygame.mouse.get_pressed()
        if (click[0] == int(1)):
            erase_text_box(WHITE,[0,665,600,50])
            pygame.display.update()
        elif (click[2] == int(1)):
            erase_text_box(WHITE,[600,665,630,50])
            pygame.display.update()
        elif (click[1] == int(1)):
            erase_text_box(WHITE,[0,630,1227,30])
            pygame.display.update()


# countries = 600
# hexagons = 550
# pyramid = 600
# quick-triangles = 500
# serious-triangles = 550
# squares = 800
# stadium = 550