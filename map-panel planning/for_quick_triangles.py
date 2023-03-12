import pygame
pygame.init()
screen = pygame.display.set_mode((1000,700)) # set screen 2D dimentions.
game_map = pygame.image.load('quick-triangles (dark).png')

pygame.draw.lines(screen, (255,255,255), False, [(0,500),(1227,500)], 3)

screen.blit(game_map,(0,0))
pygame.display.update()

while (True):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        print(mouse)