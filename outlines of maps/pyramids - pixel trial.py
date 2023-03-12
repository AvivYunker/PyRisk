import pygame
pygame.init
def single_pixel(x,y,color):
    from pygame import gfxdraw
    x = int(x)
    y = int(y)
    gfxdraw.pixel(screen, x, y, color)
    #pygame.display.update()

def single_triangle(x,y):
    x = int(x)
    y = int(y)
    cnt = int(0)
    GREEN = (255,255,255)
    while (cnt < 30):
        single_pixel(x,y,GREEN)
        x+=1
        y+=2
        cnt+=1
    cnt = int(0)
    while (cnt < 60):
        single_pixel(x,y,GREEN)
        x-=1
        cnt+=1
    cnt = int(0)
    while (cnt < 30):
        single_pixel(x,y,GREEN)
        x+=1
        y-=2
        cnt+=1

SIZE6 = (1000,750) # for 'PYRAMID'
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
screen = pygame.display.set_mode(SIZE6)
screen.fill(BLACK) # determine background color
pygame.display.flip() # really change the background color
clock = pygame.time.Clock()

arr = []

x = int(500)
y = int(0)
for cnt1 in range(1, 9, 1):
    y = int(y + 60)
    x = (500 - 30 * cnt1)
    for cnt2 in range(0, cnt1, 1):
        single_triangle(x,y)
        arr.append("(")
        arr.append(x)
        arr.append(',')
        arr.append(y)
        arr.append(")")
        x = int(x + 60)
    #x = int(2 * x / 3)
pygame.display.update()

lim = len(arr)
for cnt in range(0, lim, 1):
    print(str(arr[cnt]), end="")

print("Total dots: " + str(lim))
#single_triangle(500,80,0)
#single_triangle(470,140,0)
#single_triangle(530,140,0)




crashed = False
while (not crashed):
    for event in pygame.event.get(): # this gets any event that happens
        if event.type == pygame.QUIT:
            crashed = True
    clock.tick(60)
