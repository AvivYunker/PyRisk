import pygame
from pygame import *
from pygame.locals import *
from pygame.draw import *
import math
pygame.init()
def single_pixel(x,y,color):
    from pygame import gfxdraw
    x = int(x)
    y = int(y)
    gfxdraw.pixel(screen, x, y, color)
    pygame.display.update()

def shield_icon(x,y,color):
    PI = math.pi
    GREEN = (0,255,0)
    pygame.draw.circle(screen, color, (x,y), 30, 1)
    pygame.draw.lines(screen, color, False, [(x,y+20),(x+15,y+5)], 2)
    pygame.draw.lines(screen, color, False, [(x,y+20),(x-15,y+5)], 2)
    pygame.draw.lines(screen, color, False, [(x+15,y+5),(x+15,y-15)], 2)
    pygame.draw.lines(screen, color, False, [(x-15,y+5),(x-15,y-15)], 2)
    pygame.draw.lines(screen, color, False, [(x+15,y-15),(x-15,y-15)], 2)

def sword_icon(x,y,color):
    pygame.draw.circle(screen, color, (x,y), 30, 1)
    pygame.draw.rect(screen, color, (x-7,y+17,16,4), 0)
    pygame.draw.rect(screen, color, (x-3,y+5,8,15), 0)
    pygame.draw.rect(screen, color, (x-10,y+5,21,4), 0)
    pygame.draw.lines(screen, color, False, [(x,y+5),(x, y-20)], 2)
    pygame.draw.lines(screen, color, False, [(x+4,y+5),(x+4, y-15)], 2)
    pygame.draw.lines(screen, color, False, [(x-4,y+5),(x-4, y-15)], 2)
    pygame.draw.lines(screen, color, False, [(x+4,y-15),(x,y-20)], 2)
    pygame.draw.lines(screen, color, False, [(x-4,y-15),(x,y-20)], 2)


#def sword_icon(x,y,color):
    #pygame.draw.circle(screen, color, (x,y), 30, 1)
    #pygame.draw.rect(screen,color,(x-4,y+18,8,5), 0)
    #pygame.draw.rect(screen,color,(x-8,y+14,16,4), 0)
    #pygame.draw.rect(screen,color,(x-3,y+5,6,10), 0)
    #pygame.draw.rect(screen,color,(x-10,y+4,20,4), 0)
    #pygame.draw.lines(screen, color, False, [(x,y-20),(x,y+5)], 5)

def arrow_icon(x,y,color):
    pygame.draw.circle(screen, color, (x,y), 30, 2)
    pygame.draw.lines(screen, color, False, [(x-28,y),(x+28,y)], 5)
    pygame.draw.lines(screen, color, False, [(x+28,y),(x,y-15)], 5)
    pygame.draw.lines(screen, color, False, [(x+28,y),(x,y+15)], 5)

def add_allies_icon(x,y,color):
    pygame.draw.circle(screen, color, (x,y), 30, 2)
    pygame.draw.lines(screen, color, False, [(x-28,y),(x+28,y)], 6)
    pygame.draw.lines(screen, color, False, [(x,y-28),(x,y+28)], 6)

def exclamation_icon(x,y,color):
    pygame.draw.circle(screen, color, (x,y), 30, 2)
    pygame.draw.lines(screen, color, False, [(x,y-23),(x,y+10)], 5)
    pygame.draw.circle(screen, color, (x+1,y+18), 5)

def double_exclamation_icon(x,y,color):
    pygame.draw.circle(screen, color, (x,y), 30, 2)
    pygame.draw.lines(screen, color, False,[(x-6,y-23),(x-6,y+10)], 5)
    pygame.draw.lines(screen, color, False,[(x+7,y-23),(x+7,y+10)], 5)
    pygame.draw.circle(screen, color, (x-5,y+18), 5)
    pygame.draw.circle(screen, color, (x+8,y+18), 5)

def reinforce_icon(x,y,color):
    pygame.draw.circle(screen, color, (x,y, 5, 2))

def exit_icon(x,y,color):
    pygame.draw.rect(screen,color,(x,y,80,60), 3)
    pygame.draw.lines(screen,color, False,[(x,y),(x+80,y+60)],3)
    pygame.draw.lines(screen,color, False,[(x+80,y),(x,y+60)],3)

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

#WHITE = (255, 255, 255)
#BLACK = (0,0,0)
#GREEN = (0,255,0)
#BLUE = (0,0,255)
#YELLOW = (255,255,0)
#RED = (255,0,0)
#X = 900 # width
#Y = 700 # height
#screen = pygame.display.set_mode((X, Y ))



#while True :
    #screen.fill(BLACK) # screen-background will be black.

    #sword_icon(100,100,WHITE)
    #shield_icon(200,200,YELLOW)
    #arrow_icon(300,300,GREEN)
    #add_allies_icon(400,400, BLUE)
    #exclamation_icon(500,500,YELLOW)
    #double_exclamation_icon(600,600,RED)
    #exit_icon(600,300,RED)

    #one_valued_dice(600,100,GREEN)
    #two_valued_dice(700,100,GREEN)
    #three_valued_dice(800,100,GREEN)
    #four_valued_dice(600,200,GREEN)
    #five_valued_dice(700,200,GREEN)
    #six_valued_dice(800,200,GREEN)

    #for event in pygame.event.get() :
        #if event.type == pygame.QUIT :
            #pygame.quit() # finish the game
            #quit() # quit the program
        #pygame.display.update()
