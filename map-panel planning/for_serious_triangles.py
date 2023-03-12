import pygame
pygame.init()
screen = pygame.display.set_mode((650,700)) # set screen 2D dimentions.
game_map = pygame.image.load('serious-triangles (dark).png')
screen.blit(game_map,(0,0))

screen2 = pygame.display.set_mode((300,100))

pygame.draw.lines(screen, (255,255,255), False, [(0,500),(650,500)], 3)

pygame.display.update()

while (True):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        print(mouse)