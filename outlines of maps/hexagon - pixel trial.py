import pygame
pygame.init
def single_pixel(x,y,color):
    from pygame import gfxdraw
    x = int(x)
    y = int(y)
    gfxdraw.pixel(screen, x, y, color)
    pygame.display.update()

def single_hexagon(x,y, arr):
    x = int(x)
    y = int(y)
    FULL = int(55)
    HALF = int(24)
    GREEN = (255,255,255)
    cnt = int(0)
    while (cnt < FULL):
        single_pixel(x,y,GREEN)
        x+=1
        cnt+=1
    cnt = int(0)
    while (cnt < HALF):
        single_pixel(x,y,GREEN)
        x+=1
        y+=2
        cnt+=1
    cnt = int(0)
    while (cnt < HALF):
        single_pixel(x,y,GREEN)
        x-=1
        y+=2
        cnt+=1
    cnt = int(0)
    while (cnt < FULL):
        single_pixel(x,y,GREEN)
        x-=1
        cnt+=1
    cnt = int(0)
    while (cnt < HALF):
        single_pixel(x,y,GREEN)
        x-=1
        y-=2
        cnt+=1
    cnt = int(0)
    while (cnt < HALF):
        single_pixel(x,y,GREEN)
        x+=1
        y-=2
        cnt+=1
    cnt = int(0)

SIZE = (1200, 600) # for 'HEXAGONS'
BLACK = (0,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
screen = pygame.display.set_mode(SIZE)
screen.fill(BLACK) # determine background color
pygame.display.flip() # really change the background color
clock = pygame.time.Clock()

arr = []

y = int(50)
cnt_even_odd = int(0)
while (y < 400):
    if (cnt_even_odd % 2 == 0):
        for x in range(45, 1100, 159):
            single_hexagon(x,y,arr)
    else:
        for x in range(124, 1100, 159):
            single_hexagon(x,y,arr)
    y+=47.63
    cnt_even_odd+=1

lim = len(arr)
for cnt in range (0, lim, 1):
    print(str(arr[cnt]), end="")

crashed = False
while (not crashed):
    for event in pygame.event.get(): # this gets any event that happens
        if event.type == pygame.QUIT:
            crashed = True
    clock.tick(60)

input("\nDONE!\n")
