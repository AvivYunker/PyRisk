import pygame
pygame.init()
from icons import *
screen = pygame.display.set_mode((1200,700)) # set screen 2D dimentions.
game_map = pygame.image.load('hexagons (dark).png')
screen.fill((255,255,255))
screen.blit(game_map,(0,0))
pygame.draw.lines(screen, (255,255,255), False, [(0,500),(1227,500)], 3)
pygame.display.update()

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
create_text_box("1st hexagon", font1, GREEN_PL, [275,630,50,100])
create_text_box("2nd hexagon", font1, RED_PL, [900,630,50,100])

while (True):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        print(mouse)