import pygame
pygame.init
def single_pixel(x,y,color):
    from pygame import gfxdraw
    x = int(x)
    y = int(y)
    gfxdraw.pixel(screen, x, y, color)
    #pygame.display.update()

def assign_800x800_pixels():
    x = int(100)
    y = int(100)
    # x = width / y = length
    BLUE = (0,0,255)
    while (y <= 700):
        while (x <= 700):
            single_pixel(x,y,BLUE)
            x+=1
        x=100
        y+=100
    x = int(100)
    y = int(100)
    # x = width / y = length
    while (x <= 700):
        while (y <= 700):
            single_pixel(x,y,BLUE)
            y+=1
        y=100
        x+=100



BLACK = (0,0,0)
SIZE2 = (800, 800)
screen = pygame.display.set_mode(SIZE2)
screen.fill(BLACK)
pygame.display.flip()
assign_800x800_pixels()
pygame.display.update()

clock = pygame.time.Clock()

crashed = False
while (not crashed):
    for event in pygame.event.get(): # this gets any event that happens
        print(event)
        if event.type == pygame.QUIT:
            crashed = True

    clock.tick(60)