import pygame
pygame.init()
from pygame import gfxdraw

def distance_two_dots(dot1, dot2):
    part1 = pow(dot2[1]-dot1[1], 2) # y2 - y1
    part2 = pow(dot2[0]-dot1[0], 2) # x2 - x1
    res = pow(part1 + part2, 0.5)
    return res

def shortest_distance(my_dot, arr_dot):
    selected = int(0)
    dist = 10000
    for cnt1 in range(0, len(arr_dot), 1):
        for cnt2 in range(0, len(arr_dot[cnt1]["dots"]), 1):
            #print(arr_dot[cnt1]["dots"][cnt2][0])
            #print(arr_dot[cnt1]["dots"][cnt2][1])
            #print(my_dot[0])
            #print(my_dot[1])
            temp = distance_two_dots((my_dot[0],my_dot[1]),(arr_dot[cnt1]["dots"][cnt2][0],arr_dot[cnt1]["dots"][cnt2][1]))
            if (temp < dist):
                dist = int(temp)
                selected = (arr_dot[cnt1]["id"])
                #print("ID IS: " + str(selected))
    return selected

X = int(1300)
Y = int(600)
screen = pygame.display.set_mode((X,Y))
# NEED TO FIX IDS ########################################
dict_266 = {"id":266,"dots":[(75,75)]}
dict_267 = {"id":267,"dots":[(175,75)]}
dict_268 = {"id":268,"dots":[(225,75)]}
dict_269 = {"id":269,"dots":[(275,75)]}
dict_270 = {"id":270,"dots":[(325,75)]}
dict_271 = {"id":271,"dots":[(403,75)]}
dict_272 = {"id":272,"dots":[(453,75)]}
dict_273 = {"id":273,"dots":[(503,75)]}
dict_274 = {"id":274,"dots":[(553,75)]}
dict_275 = {"id":275,"dots":[(632,75)]}
dict_276 = {"id":276,"dots":[(682,75)]}
dict_277 = {"id":277,"dots":[(732,75)]}
dict_278 = {"id":278,"dots":[(782,75)]}
dict_279 = {"id":279,"dots":[(860,75)]}
dict_280 = {"id":280,"dots":[(910,75)]}
dict_281 = {"id":281,"dots":[(960,75)]}
dict_282 = {"id":282,"dots":[(75,175)]}
dict_283 = {"id":283,"dots":[(125,175)]}
dict_284 = {"id":284,"dots":[(175,175)]}
dict_285 = {"id":285,"dots":[(225,175)]}
dict_286 = {"id":286,"dots":[(275,175)]}
dict_287 = {"id":287,"dots":[(325,175)]}
dict_288 = {"id":288,"dots":[(375,175)]}
dict_289 = {"id":289,"dots":[(425,175)]}
dict_290 = {"id":290,"dots":[(475,175)]}
dict_291 = {"id":291,"dots":[(525,175)]}
dict_292 = {"id":292,"dots":[(575,175)]}
dict_293 = {"id":293,"dots":[(625,175)]}
dict_294 = {"id":294,"dots":[(675,175)]}
dict_295 = {"id":295,"dots":[(726, 175),(753,175),(784, 175)]}
dict_296 = {"id":296,"dots":[(860,175)]}
dict_297 = {"id":297,"dots":[(910,175)]}
dict_298 = {"id":298,"dots":[(960,175)]}
dict_299 = {"id":299,"dots":[(1039,175)]}
dict_300 = {"id":300,"dots":[(1089,175)]}
dict_301 = {"id":301,"dots":[(1139,175)]}
dict_302 = {"id":302,"dots":[(1189,175)]}
dict_303 = {"id":303,"dots":[(74,225),(87,225),(100,225)]}
dict_304 = {"id":304,"dots":[(150,225)]}
dict_305 = {"id":305,"dots":[(200,225)]}
dict_306 = {"id":306,"dots":[(250,225)]}
dict_307 = {"id":307,"dots":[(300,225)]}
dict_308 = {"id":308,"dots":[(350,225)]}
dict_309 = {"id":309,"dots":[(400,225)]}
dict_310 = {"id":310,"dots":[(450,225)]}
dict_311 = {"id":311,"dots":[(500,225)]}
dict_312 = {"id":312,"dots":[(550,225)]}
dict_313 = {"id":313,"dots":[(600,225)]}
dict_314 = {"id":314,"dots":[(650,225)]}
dict_315 = {"id":315,"dots":[(700,225)]}
dict_316 = {"id":316,"dots":[(755,225),(768,250),(781,225),(765,275),(771,275)]}
dict_317 = {"id":317,"dots":[(860,225)]}
dict_318 = {"id":318,"dots":[(910,225)]}
dict_319 = {"id":319,"dots":[(960,225)]}
dict_320 = {"id":320,"dots":[(1039,225)]}
dict_321 = {"id":321,"dots":[(1089,225)]}
dict_322 = {"id":322,"dots":[(1139,225)]}
dict_323 = {"id":323,"dots":[(1189,225),(1189,250),(1189,275)]}
dict_324 = {"id":324,"dots":[(82,275),(92,275),(102,275)]}
dict_325 = {"id":325,"dots":[(160,275)]}
dict_326 = {"id":326,"dots":[(210,275)]}
dict_327 = {"id":327,"dots":[(260,275)]}
dict_328 = {"id":328,"dots":[(310,275)]}
dict_329 = {"id":329,"dots":[(360,275)]}
dict_330 = {"id":330,"dots":[(410,275)]}
dict_331 = {"id":331,"dots":[(460,275)]}
dict_332 = {"id":332,"dots":[(510,275)]}
dict_333 = {"id":333,"dots":[(560,275)]}
dict_334 = {"id":334,"dots":[(610,275)]}
dict_335 = {"id":335,"dots":[(660,275)]}
dict_336 = {"id":336,"dots":[(710,275)]}
dict_337 = {"id":337,"dots":[(1039,275)]}
dict_338 = {"id":338,"dots":[(1089,275)]}
dict_339 = {"id":339,"dots":[(1139,275)]}
dict_340 = {"id":340,"dots":[(75,325)]}
dict_341 = {"id":341,"dots":[(125,325)]}
dict_342 = {"id":342,"dots":[(175,325)]}
dict_343 = {"id":343,"dots":[(225,325)]}
dict_344 = {"id":344,"dots":[(275,325)]}
dict_345 = {"id":345,"dots":[(325,325)]}
dict_346 = {"id":346,"dots":[(375,325)]}
dict_347 = {"id":347,"dots":[(425,325)]}
dict_348 = {"id":348,"dots":[(475,325)]}
dict_349 = {"id":349,"dots":[(525,325)]}
dict_350 = {"id":350,"dots":[(575,325)]}
dict_351 = {"id":351,"dots":[(625,325)]}
dict_352 = {"id":352,"dots":[(675,325),(700,325),(728,325),(753,325),(778,325)]}
dict_353 = {"id":353,"dots":[(910,325)]}
dict_354 = {"id":354,"dots":[(1039,325)]}
dict_355 = {"id":355,"dots":[(1089,325)]}
dict_356 = {"id":356,"dots":[(1139,325)]}
dict_357 = {"id":357,"dots":[(1189,325),(1189,350),(1189,375)]}
dict_358 = {"id":358,"dots":[(80,375)]}
dict_359 = {"id":359,"dots":[(140,375)]}
dict_360 = {"id":360,"dots":[(200,375)]}
dict_361 = {"id":361,"dots":[(260,375),(290,375),(320,375),(350,375),(390,375),(420,375),(450,375),(480,375),(520,375)]}
dict_362 = {"id":362,"dots":[(580,375)]}
dict_363 = {"id":363,"dots":[(640,375)]}
dict_364 = {"id":364,"dots":[(700,375)]}
dict_365 = {"id":365,"dots":[(758,375),(768,375),(778,375)]}
dict_366 = {"id":366,"dots":[(860,375)]}
dict_367 = {"id":367,"dots":[(910,375)]}
dict_368 = {"id":368,"dots":[(960,375)]}
dict_369 = {"id":369,"dots":[(1039,375),(1064,375),(1089,375)]}
dict_370 = {"id":370,"dots":[(1139,375)]}

arr_centers = [dict_266,dict_267,dict_268,dict_269,dict_270,dict_271,dict_272,dict_273,dict_274,dict_275,dict_276,dict_277,dict_278,dict_279,dict_280,dict_281,dict_282,dict_283,dict_284,dict_285,dict_286,dict_287,dict_288,dict_289,dict_290,dict_291,dict_292,dict_293,dict_294,dict_295,dict_296,dict_297,dict_298,dict_299,dict_300,dict_301,dict_302,dict_303,dict_304,dict_305,dict_306,dict_307,dict_308,dict_309,dict_310,dict_311,dict_312,dict_313,dict_314,dict_315,dict_316,dict_317,dict_318,dict_319,dict_320,dict_321,dict_322,dict_323,dict_324,dict_325,dict_326,dict_327,dict_328,dict_329,dict_330,dict_331,dict_332,dict_333,dict_334,dict_335,dict_336,dict_337,dict_338,dict_339,dict_340,dict_341,dict_342,dict_343,dict_344,dict_345,dict_346,dict_347,dict_348,dict_349,dict_350,dict_351,dict_352,dict_353,dict_354,dict_355,dict_356,dict_357,dict_358,dict_359,dict_360,dict_361,dict_362,dict_363,dict_364,dict_365,dict_366,dict_367,dict_368,dict_369,dict_370,]

game_map = pygame.image.load('keyboard (dark).png')
screen.blit(game_map,(0,0))

for cnt1 in range(0, len(arr_centers), 1):
    for cnt2 in range(0, len(arr_centers[cnt1]["dots"]), 1):
        gfxdraw.pixel(screen, arr_centers[cnt1]["dots"][cnt2][0],arr_centers[cnt1]["dots"][cnt2][1], (255,0,0))

pygame.display.update()
print(len(arr_centers))
while (True):
   for event in pygame.event.get():
       mouse = pygame.mouse.get_pos()
       click = pygame.mouse.get_pressed()
       if (click[0] == int(1)):
           print(mouse)
           gfxdraw.pixel(screen, mouse[0], mouse[1], (0,255,0))
           id_selected = shortest_distance((mouse[0], mouse[1]), arr_centers)
           print("id: " + str(id_selected))
           pygame.display.update()