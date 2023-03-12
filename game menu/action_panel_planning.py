import pygame
pygame.init()
from button_class import Button
screen = pygame.display.set_mode((1227,850)) # set screen 2D dimentions.
game_map = pygame.image.load("countries (dark).png")
pygame.draw.line(screen, (255,0,0), (0,628),(1227,628), 1)
screen.blit(game_map,(0,0))
back_mode = int(0)

# DEFINING THE BUTTONS:
passCode_1 = Button(3, "1", back_mode, (450, 635, 70, 50), 5, 1, 0)
passCode_2 = Button(3, "2", back_mode, (525, 635, 70, 50), 5, 1, 0)
passCode_3 = Button(3, "3", back_mode, (600, 635, 70, 50), 5, 1, 0)
passCode_4 = Button(3, "4", back_mode, (450, 690, 70, 50), 5, 1, 0)
passCode_5 = Button(3, "5", back_mode, (525, 690, 70, 50), 5, 1, 0)
passCode_6 = Button(3, "6", back_mode, (600, 690, 70, 50), 5, 1, 0)
passCode_7 = Button(3, "7", back_mode, (450, 745, 70, 50), 5, 1, 0)
passCode_8 = Button(3, "8", back_mode, (525, 745, 70, 50), 5, 1, 0)
passCode_9 = Button(3, "9", back_mode, (600, 745, 70, 50), 5, 1, 0)
passCode_V = Button(3, "V", back_mode, (487, 800, 70, 50), 5, 1, 0)
passCode_X = Button(3, "X", back_mode, (562, 800, 70, 50), 5, 1, 0)

selected_map = int(0)
pygame.display.update()
while (True):
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        selected_map = passCode_1.button_functional(selected_map)
        selected_map = passCode_2.button_functional(selected_map)
        selected_map = passCode_3.button_functional(selected_map)
        selected_map = passCode_4.button_functional(selected_map)
        selected_map = passCode_5.button_functional(selected_map)
        selected_map = passCode_6.button_functional(selected_map)
        selected_map = passCode_7.button_functional(selected_map)
        selected_map = passCode_8.button_functional(selected_map)
        selected_map = passCode_9.button_functional(selected_map)
        selected_map = passCode_V.button_functional(selected_map)
        selected_map = passCode_X.button_functional(selected_map)