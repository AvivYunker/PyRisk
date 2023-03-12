import pygame
pygame.init
def single_pixel(x,y,color):
    from pygame import gfxdraw
    x = int(x)
    y = int(y)
    gfxdraw.pixel(screen, x, y, color)
    gfxdraw.pixel(screen, x, y+1, color)
    #pygame.display.update()
def right_angled_triangle(x,y,pos):
    x = int(x)
    y = int(y)
    pos = int(pos)
    # pos=0 - |\ (bottom)
    # pos=1 - \| (higher)
    if (pos == 0):
        pass
    else:
        pass
def draw_single_square (x,y):
    x = int(x)
    y = int(y)
    RED = (255,0,0)
    cnt = int(0)
    while (cnt < 110):
        single_pixel(x,y,RED)
        x+=1
        cnt+=1
    cnt = int(0)
    while (cnt < 110):
        single_pixel(x,y,RED)
        y+=1
        cnt+=1
    cnt = int(0)
    while (cnt < 110):
        single_pixel(x,y,RED)
        x-=1
        cnt+=1
    cnt = int(0)
    while (cnt < 110):
        single_pixel(x,y,RED)
        y-=1
        cnt+=1

def diagonal_row(x,y, lenn, pos):
    x = int(x)
    y = int(y)
    RED = (255,0,0)
    lenn = int(lenn) # 0=short / 1=long
    pos = int(pos) # 0=x++/y++ / 1=x++/y--
    cnt = int(0)
    if (lenn == 0):
        if (pos == 0):
            while (cnt < 220):
                single_pixel(x,y,RED)
                x+=1
                y+=1
                cnt+=1
        else:
            while (cnt < 220):
                single_pixel(x,y,RED)
                x+=1
                y-=1
                cnt+=1
    else:
        if (pos == 1):
            while (cnt < 440):
                single_pixel(x,y,RED)
                x+=1
                y+=1
                cnt+=1
        else:
            while (cnt < 440):
                single_pixel(x,y,RED)
                x+=1
                y-=1
                cnt+=1



BLACK = (0,0,0)
BLUE = (0,0,255)
SIZE4 = (650,650) # for 'SERIOUS-TRIANGLES'
screen = pygame.display.set_mode(SIZE4)
screen.fill(BLACK) # determine background color
pygame.display.flip() # really change the background color
clock = pygame.time.Clock()

x = int(0)
y = int(40)
for cnt1 in range(0, 4, 1):
    x += 105
    for cnt2 in range(0, 4, 1):
        draw_single_square(x,y)
        x += 110
    x = int(0)
    y += 110

diagonal_row(105,480,1,0)
diagonal_row(105,40,1,1)
#...
diagonal_row(105,260,0,1) # lenn / pos
diagonal_row(325,480,0,1)
diagonal_row(325,40,0,0)
diagonal_row(105,260,0,0)




#...

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(),
            sys.exit()
        print(event)
        pygame.display.update()
        break
