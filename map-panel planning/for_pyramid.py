import pygame
pygame.init()
screen = pygame.display.set_mode((1000,800)) # set screen 2D dimentions.
game_map = pygame.image.load('pyramid (dark).png')
screen.blit(game_map,(0,0))

pygame.draw.lines(screen, (255,255,255), False, [(0,600),(1227,600)], 3)

pygame.display.update()

while (True):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        print(mouse)