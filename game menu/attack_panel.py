import pygame
pygame.init()
from button_class import Button
screen = pygame.display.set_mode((800,942)) # set screen 2D dimentions.
game_map = pygame.image.load("squares (dark).png")
screen.blit(game_map,(0,0))
pygame.draw.line(screen, (255,0,0), (0,720),(800,720), 1)
pygame.display.update()
back_mode = int(0)
map1_button = Button(3, "", back_mode, (300, 300, 240, 175), 5, 1, 0)
while (True):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        print(mouse)