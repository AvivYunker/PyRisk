import pygame
pygame.init()
screen = pygame.display.set_mode((1227,828)) # set screen 2D dimentions.
game_map = pygame.image.load('countries (light).png')
screen.fill((0,0,0))
#screen.blit(game_map,(0,0))
pygame.draw.polygon(screen, (255,0,0), [(100,100),(110,110),(100,120)], 0)
pygame.display.update()

while (True):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        print(mouse)