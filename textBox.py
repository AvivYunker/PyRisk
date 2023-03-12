import pygame
import time
pygame.init()
screen = pygame.display.set_mode((1000,400)) # set screen 2D dimentions.

pygame.key.set_text_input_rect(pygame.Rect(0,0,240,240))


def add_char_gui (val, arr_dem):
    print(str(val))
    font = pygame.font.Font('freesansbold.ttf', 45) # 'PyRisk' logo.
    color = (0,255,255)
    #pygame.draw.rect(screen, color, (arr_dem[0],arr_dem[1],arr_dem[2],arr_dem[3]),5)
    text1 = font.render(chr(val), True, color)
    textRect1 = text1.get_rect()
    textRect1.center = ((arr_dem[0]+(arr_dem[2]/2)),(arr_dem[1]+(arr_dem[3]/2)))
    screen.blit(text1, textRect1)
    pygame.display.update()

def remove_char_gui (arr_dem):
    pygame.draw.rect(screen, (0,0,0), (arr_dem[0]-7,arr_dem[1]-10,arr_dem[2],arr_dem[3]), 0)
    pygame.display.update()

cont = int(1)
strr = str("")
level = int(50)
while (cont):
    if (level < 50):
        level += 30
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        for cnt in range(0, len(keys), 1):
            if (keys[cnt] == 1):
                if (str(cnt) == '13'):
                    cont = int(0)
                    break
                elif (str(cnt) == '8'):
                    level -= 30
                    strr = strr[:-1]
                    remove_char_gui((level, 95,34,50))
                    #level -= 30
                    continue
                if (len(strr) <= 6):
                    add_char_gui(cnt,(level,100,20,20))
                    level += 30
                    print("CHR is: " + chr(cnt))
                    print("VAL is: " + str(cnt))
                    strr += chr(cnt)
                print("CHR is: " + chr(cnt))
                print("VAL is: " + str(cnt))
                print("level is: " + str(level))
                pygame.event.wait()
print("\n")
print(str(strr))