import pygame
#screen = pygame.display.set_mode((1000,800))
import thread

def pygame_wait():
    screen = pygame.display.set_mode((1000,800))
    while (True):
        for event in pygame.event.get:
            mouse = pygame.mouse.get_pos()
            print(mouse)

def simple_counter():
    for cnt in range(0, 1000000, 1):
        print(cnt)

print("Before")
runInParallel(pygame_wait, simple_counter)
print("After")