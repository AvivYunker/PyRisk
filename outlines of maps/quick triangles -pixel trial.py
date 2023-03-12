import pygame
pygame.init
def single_pixel(x,y,color):
    from pygame import gfxdraw
    x = int(x)
    y = int(y)
    gfxdraw.pixel(screen, x, y, color)
    pygame.display.update()

def assign_500x500_pixels():
    x = int(100)
    y = int(100)
    BLUE = (0,0,255)
    while (x <= 400 and y <= 400):
        single_pixel(x,y,BLUE)
        x+=1
        y+=1
    x = int(400)
    y = int(100)
    while (x >= 100 and y <= 400):
        single_pixel(x,y,BLUE)
        x-=1
        y+=1
    x = int(100)
    y = int(100)
    while (x <= 400):
        single_pixel(x,y,BLUE)
        x+=1
    while (y <= 400):
        single_pixel(x,y,BLUE)
        y+=1
    while (x >= 100):
        single_pixel(x,y,BLUE)
        x-=1
    while (y >= 100):
        single_pixel(x,y,BLUE)
        y-=1




BLACK = (0,0,0)
SIZE3 = (500,500) # for 'QUICK-TRIANGLES'
screen = pygame.display.set_mode(SIZE3)
screen.fill(BLACK)
pygame.display.flip()
assign_500x500_pixels()
#pygame.display.update()



input("\nDONE!\n")