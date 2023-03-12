import pygame
pygame.init()
screen = pygame.display.set_mode((1200,660)) # set screen 2D dimentions.
game_map = pygame.image.load('stadium (dark).png')
screen.blit(game_map,(0,0))

pygame.draw.lines(screen, (255,255,255), False, [(0,460),(1200,460)], 3)

pygame.display.update()

while (True):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        print(mouse)