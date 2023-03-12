import pygame
screen = pygame.display.set_mode((500,500)) # setting the resolutions of the game-window.
def one_valued_dice(x,y,color, screen):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+18,y+18), 4, 0)
    pygame.display.update()

def two_valued_dice(x,y,color, screen):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+10,y+10), 4, 0)
    pygame.draw.circle(screen, color, (x+24,y+24), 4, 0)
    pygame.display.update()

def three_valued_dice(x,y,color, screen):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+8,y+8), 4, 0)
    pygame.draw.circle(screen, color, (x+17,y+17), 4, 0)
    pygame.draw.circle(screen, color, (x+26,y+26), 4, 0)
    pygame.display.update()

def four_valued_dice(x,y,color, screen):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+10,y+10), 4, 0)
    pygame.draw.circle(screen, color, (x+24,y+10), 4, 0)
    pygame.draw.circle(screen, color, (x+10,y+24), 4, 0)
    pygame.draw.circle(screen, color, (x+24,y+24), 4, 0)
    pygame.display.update()

def five_valued_dice(x,y,color, screen):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+8,y+8), 4, 0)
    pygame.draw.circle(screen, color, (x+26,y+8), 4, 0)
    pygame.draw.circle(screen, color, (x+8,y+26), 4, 0)
    pygame.draw.circle(screen, color, (x+26,y+26), 4, 0)
    pygame.draw.circle(screen, color, (x+17,y+17), 4, 0)
    pygame.display.update()

def six_valued_dice(x,y,color, screen):
    pygame.draw.rect(screen,color,(x,y,34,34), 4)
    pygame.draw.circle(screen, color, (x+9,y+8), 4, 0)
    pygame.draw.circle(screen, color, (x+9,y+17), 4, 0)
    pygame.draw.circle(screen, color, (x+9,y+26), 4, 0)
    pygame.draw.circle(screen, color, (x+25,y+8), 4, 0)
    pygame.draw.circle(screen, color, (x+25,y+17), 4, 0)
    pygame.draw.circle(screen, color, (x+25,y+26), 4, 0)
    pygame.display.update()

def remove_dice (x,y,back_mode, screen):
    if (back_mode == 0): # 0=DARK
        color = (0,0,0)
    else: # 1=LIGHT
        color = (255,255,255)
    pygame.draw.rect(screen,(color),(x-1,y-1,37,37),0)
    pygame.display.update()