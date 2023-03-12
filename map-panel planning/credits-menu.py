import pygame
pygame.init()
from button_class import Button
screen = pygame.display.set_mode((1100,700))
game_map = pygame.image.load('menu8dark (dark).png')
screen.blit(game_map,(0,0))