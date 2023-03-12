# (x,y) - x=width / y=height
# regular button - (), {A, +}
# slight-wide button - (), {alt, START}
# PHYISICAL KEYBOARD = (44,12)
import pygame
pygame.init
SIZE = (1300,600)
screen = pygame.display.set_mode(SIZE)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (0,0,0)
THICKNESS = 3

screen.fill(BLACK)
WHITE = (255,255,255)


kybrd0 = [(50,50),(100,50),(100,100),(50,100),(50,50)]
kybrd1 = [(150,50),(200,50),(200,100),(150,100),(150,50)]
kybrd2 = [(200,50),(250,50),(250,100),(200,100),(200,50)]
kybrd3 = [(250,50),(300,50),(300,100),(250,100),(250,50)]
kybrd4 = [(300,50),(350,50),(350,100),(300,100),(300,50)]
kybrd5 = [(378.57,50),(428.57,50),(428.57,100),(378.57,100),(378.57,50)]
kybrd6 = [(428.57,50),(478.57,50),(478.57,100),(428.57,100),(428.57,50)]
kybrd7 = [(478.57,50),(528.5699999999999,50),(528.5699999999999,100),(478.57,100),(478.57,50)]
kybrd8 = [(528.57,50),(578.57,50),(578.57,100),(528.57,100),(528.57,50)]
kybrd9 = [(607.14,50),(657.14,50),(657.14,100),(607.14,100),(607.14,50)]
kybrd10 = [(657.14,50),(707.14,50),(707.14,100),(657.14,100),(657.14,50)]
kybrd11 = [(707.14,50),(757.14,50),(757.14,100),(707.14,100),(707.14,50)]
kybrd12 = [(757.14,50),(807.14,50),(807.14,100),(757.14,100),(757.14,50)]
kybrd13 = [(835.71,50),(885.71,50),(885.71,100),(835.71,100),(835.71,50)]
kybrd14 = [(885.71,50),(935.71,50),(935.71,100),(885.71,100),(885.71,50)]
kybrd15 = [(935.71,50),(985.71,50),(985.71,100),(935.71,100),(935.71,50)]
kybrd16 = [(50,150),(100,150),(100,200),(50,200),(50,150)]
kybrd17 = [(100,150),(150,150),(150,200),(100,200),(100,150)]
kybrd18 = [(150,150),(200,150),(200,200),(150,200),(150,150)]
kybrd19 = [(200,150),(250,150),(250,200),(200,200),(200,150)]
kybrd20 = [(250,150),(300,150),(300,200),(250,200),(250,150)]
kybrd21 = [(300,150),(350,150),(350,200),(300,200),(300,150)]
kybrd22 = [(350,150),(400,150),(400,200),(350,200),(350,150)]
kybrd23 = [(400,150),(450,150),(450,200),(400,200),(400,150)]
kybrd24 = [(450,150),(500,150),(500,200),(450,200),(450,150)]
kybrd25 = [(500,150),(550,150),(550,200),(500,200),(500,150)]
kybrd26 = [(550,150),(600,150),(600,200),(550,200),(550,150)]
kybrd27 = [(600,150),(650,150),(650,200),(600,200),(600,150)]
kybrd28 = [(650,150),(700,150),(700,200),(650,200),(650,150)]
kybrd29 = [(700,150),(807.14,150),(807.14,200),(700,200),(700,150)]
kybrd30 = [(50,200),(125,200),(125,250),(50,250),(50,200)]
kybrd31 = [(125,200),(175,200),(175,250),(125,250),(125,200)]
kybrd32 = [(175,200),(225,200),(225,250),(175,250),(175,200)]
kybrd33 = [(225,200),(275,200),(275,250),(225,250),(225,200)]
kybrd34 = [(275,200),(325,200),(325,250),(275,250),(275,200)]
kybrd35 = [(325,200),(375,200),(375,250),(325,250),(325,200)]
kybrd36 = [(375,200),(425,200),(425,250),(375,250),(375,200)]
kybrd37 = [(425,200),(475,200),(475,250),(425,250),(425,200)]
kybrd38 = [(475,200),(525,200),(525,250),(475,250),(475,200)]
kybrd39 = [(525,200),(575,200),(575,250),(525,250),(525,200)]
kybrd40 = [(575,200),(625,200),(625,250),(575,250),(575,200)]
kybrd41 = [(625,200),(675,200),(675,250),(625,250),(625,200)]
kybrd42 = [(675,200),(725,200),(725,250),(675,250),(675,200)]
kybrd43 = [(725,200),(807.14,200),(807.14,300),(735,300),(735,250),(725,250),(725,200)]
kybrd44 = [(50,250),(135,250),(135,300),(50,300),(50,250)]
kybrd45 = [(135,250),(185,250),(185,300),(135,300),(135,250)]
kybrd46 = [(185,250),(235,250),(235,300),(185,300),(185,250)]
kybrd47 = [(235,250),(285,250),(285,300),(235,300),(235,250)]
kybrd48 = [(285,250),(335,250),(335,300),(285,300),(285,250)]
kybrd49 = [(335,250),(385,250),(385,300),(335,300),(335,250)]
kybrd50 = [(385,250),(435,250),(435,300),(385,300),(385,250)]
kybrd51 = [(435,250),(485,250),(485,300),(435,300),(435,250)]
kybrd52 = [(485,250),(535,250),(535,300),(485,300),(485,250)]
kybrd53 = [(535,250),(585,250),(585,300),(535,300),(535,250)]
kybrd54 = [(585,250),(635,250),(635,300),(585,300),(585,250)]
kybrd55 = [(635,250),(685,250),(685,300),(635,300),(635,250)]
kybrd56 = [(685,250),(735,250),(735,300),(685,300),(685,250)]
kybrd57 = [(50,300),(100,300),(100,350),(50,350),(50,300)]
kybrd58 = [(100,300),(150,300),(150,350),(100,350),(100,300)]
kybrd59 = [(150,300),(200,300),(200,350),(150,350),(150,300)]
kybrd60 = [(200,300),(250,300),(250,350),(200,350),(200,300)]
kybrd61 = [(250,300),(300,300),(300,350),(250,350),(250,300)]
kybrd62 = [(300,300),(350,300),(350,350),(300,350),(300,300)]
kybrd63 = [(350,300),(400,300),(400,350),(350,350),(350,300)]
kybrd64 = [(400,300),(450,300),(450,350),(400,350),(400,300)]
kybrd65 = [(450,300),(500,300),(500,350),(450,350),(450,300)]
kybrd66 = [(500,300),(550,300),(550,350),(500,350),(500,300)]
kybrd67 = [(550,300),(600,300),(600,350),(550,350),(550,300)]
kybrd68 = [(600,300),(650,300),(650,350),(600,350),(600,300)]
kybrd69 = [(650,300),(807.14,300),(807.14,350),(650,350),(650,300)]
kybrd70 = [(50,350),(110,350),(110,400),(50,400),(50,350)]
kybrd71 = [(110,350),(170,350),(170,400),(110,400),(110,350)]
kybrd72 = [(170,350),(230,350),(230,400),(170,400),(170,350)]
kybrd73 = [(230,350),(550,350),(550,400),(230,400),(230,350)]
kybrd74 = [(550,350),(610,350),(610,400),(550,400),(550,350)]
kybrd75 = [(610,350),(670,350),(670,400),(610,400),(610,350)]
kybrd76 = [(670,350),(730,350),(730,400),(670,400),(670,350)]
kybrd77 = [(730,350),(807.14,350),(807.14,400),(730,400),(730,350)]
kybrd78 = [(835.71,150),(885.71,150),(885.71,200),(835.71,200),(835.71,150)]
kybrd79 = [(885.71,150),(935.71,150),(935.71,200),(885.71,200),(885.71,150)]
kybrd80 = [(935.71,150),(985.71,150),(985.71,200),(935.71,200),(935.71,150)]
kybrd81 = [(835.71,200),(885.71,200),(885.71,250),(835.71,250),(835.71,200)]
kybrd82 = [(885.71,200),(935.71,200),(935.71,250),(885.71,250),(885.71,200)]
kybrd83 = [(935.71,200),(985.71,200),(985.71,250),(935.71,250),(935.71,200)]
kybrd84 = [(885.71,300),(935.71,300),(935.71,350),(885.71,350),(885.71,300)]
kybrd85 = [(835.71,350),(885.71,350),(885.71,400),(835.71,400),(835.71,350)]
kybrd86 = [(885.71,350),(935.71,350),(935.71,400),(885.71,400),(885.71,350)]
kybrd87 = [(935.71,350),(985.71,350),(985.71,400),(935.71,400),(935.71,350)]
kybrd88 = [(1014.28,150),(1064.28,150),(1064.28,200),(1014.28,200),(1014.28,150)]
kybrd89 = [(1064.28,150),(1114.28,150),(1114.28,200),(1064.28,200),(1064.28,150)]
kybrd90 = [(1114.28,150),(1164.28,150),(1164.28,200),(1114.28,200),(1114.28,150)]
kybrd91 = [(1164.28,150),(1214.28,150),(1214.28,200),(1164.28,200),(1164.28,150)]
kybrd92 = [(1014.28,200),(1064.28,200),(1064.28,250),(1014.28,250),(1014.28,200)]
kybrd93 = [(1064.28,200),(1114.28,200),(1114.28,250),(1064.28,250),(1064.28,200)]
kybrd94 = [(1114.28,200),(1164.28,200),(1164.28,250),(1114.28,250),(1114.28,200)]
kybrd95 = [(1164.28,200),(1214.28,200),(1214.28,300),(1164.28,300),(1164.28,200)]
kybrd96 = [(1014.28,250),(1064.28,250),(1064.28,300),(1014.28,300),(1014.28,250)]
kybrd97 = [(1064.28,250),(1114.28,250),(1114.28,300),(1064.28,300),(1064.28,250)]
kybrd98 = [(1114.28,250),(1164.28,250),(1164.28,300),(1114.28,300),(1114.28,250)]
kybrd99 = [(1014.28,300),(1064.28,300),(1064.28,350),(1014.28,350),(1014.28,300)]
kybrd100 = [(1064.28,300),(1114.28,300),(1114.28,350),(1064.28,350),(1064.28,300)]
kybrd101 = [(1114.28,300),(1164.28,300),(1164.28,350),(1114.28,350),(1114.28,300)]
kybrd102 = [(1164.28,300),(1214.28,300),(1214.28,400),(1164.28,400),(1164.28,300)]
kybrd103 = [(1014.28,350),(1114.28,350),(1114.28,400),(1014.28,400),(1014.28,350)]
kybrd104 = [(1114.28,350),(1164.28,350),(1164.28,400),(1114.28,400),(1114.28,350)]


pygame.draw.lines(screen, WHITE, False, kybrd0, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd1, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd2, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd3, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd4, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd5, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd6, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd7, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd8, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd9, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd10, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd11, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd12, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd13, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd14, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd15, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd16, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd17, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd18, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd19, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd20, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd21, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd22, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd23, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd24, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd25, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd26, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd27, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd28, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd29, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd30, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd31, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd32, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd33, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd34, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd35, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd36, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd37, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd38, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd39, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd40, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd41, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd42, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd43, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd44, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd45, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd46, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd47, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd48, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd49, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd50, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd51, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd52, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd53, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd54, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd55, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd56, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd57, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd58, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd59, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd60, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd61, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd62, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd63, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd64, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd65, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd66, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd67, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd68, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd69, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd70, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd71, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd72, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd73, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd74, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd75, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd76, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd77, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd78, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd79, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd80, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd81, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd82, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd83, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd84, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd85, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd86, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd87, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd88, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd89, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd90, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd91, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd92, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd93, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd94, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd95, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd96, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd97, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd98, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd99, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd100, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd101, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd102, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd103, THICKNESS)
pygame.draw.lines(screen, WHITE, False, kybrd104, THICKNESS)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(),
            sys.exit()
        print(event)
        pygame.display.update()
        break
