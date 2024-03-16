# importing pygame module
import pygame
import math
import random
from map_data import *
from textures import *
from lighting import *
from utility_functions import *
from setup import *

from player import Player
pygame.init() # initializing pygame engine

player = Player(256, 300)



def level_editing():
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        map_data[int(my/screen_height*24)][int(mx/screen_width*32)] = 1
        height_map[int(my/screen_height*24)][int(mx/screen_width*32)] = height_sects
    elif pygame.mouse.get_pressed()[2]:
        mx, my = pygame.mouse.get_pos()
        map_data[int(my/screen_height*24)][int(mx/screen_width*32)] = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]: # delete the entire thing
        for i in range(24):
            for j in range(32):
                map_data[i][j] = 0


## FONT
globalFont = pygame.font.Font('freesansbold.ttf', 32)
showHeightVals = globalFont.render(str(height_sects[0]) + ", " + str(height_sects[1]), True, (255, 0, 0))
rectShowHeightVals = showHeightVals.get_rect()
rectShowHeightVals.center = (512, 512)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():  # loops through all the events of the game
        if event.type == pygame.QUIT:  # a constant synonymous to the window
            #if level_editing_mode: # turn on level editing mode
            for i in range(len(map_data)):
                print(map_data[i], end=",")
                print()

            for i in range(len(height_map)):
                print(height_map[i], end=",")
                print()

            pygame.quit()
            print(player.x, player.y)
            exit()


        if level_editing_mode:
            level_editing()
    if not level_editing_mode:
        player.raycast(player.xProjection, player.yProjection, player.faceDir)
        #player.raycast(162.4531612306712, 436.00049263481077, player.faceDir)

        player.move(0)


    if level_editing_mode:
        for i in range(len(map_data)):
            for j in range(len(map_data[0])):
                height_sects_t = height_map[i][j]
                if map_data[i][j] == 1:
                    pygame.draw.rect(surface, (255
                                               , 0, 0), (
                        (j/32)*screen_width,
                        (i/24)*screen_height,
                        1000/32,
                        screen_height/24
                    ))


        mx, my = pygame.mouse.get_pos()
        pygame.draw.rect(surface, (255, 255, 255), (
            int(mx / screen_width * 32)*(screen_width/32),
            int(my / screen_height * 24)*(screen_height/24),
            32,
            screen_height/24
        ), 2)



    # level editing as player
    keys = pygame.key.get_pressed()
    if height_change_counter >= 15:
        height_map[int(player.y/32)][int(player.x/32)][0] = max(0, min(height_map[int(player.y/32)][int(player.x/32)][0]
                                                                       + (keys[pygame.K_l] - keys[pygame.K_j])*16, 512))
        height_map[int(player.y/32)][int(player.x/32)][1] = max(0, min(height_map[int(player.y/32)][int(player.x/32)][1]
                                                                       + (keys[pygame.K_o] - keys[pygame.K_i])*16, 512))
        height_change_counter = 0
    else:
        height_change_counter += 1

    if keys[pygame.K_m]: # pasting
        height_map[int(player.y/32)][int(player.x/32)] = height_sects[:]
        for i in range(len(light_maps)):
            for j in range(len(light_maps[0])):
                light_maps[i][j] = 16  # redoing the entire map

        for i in range(len(light_coords)):
            light_raycasts(light_coords[i][0], light_coords[i][1])


    #pygame.draw.rect(surface, (255, 0, 0), (0, 0, 128, 32))
    #pygame.draw.rect(surface, (0, 255, 0), (0, 0, (clock.get_fps()/60)*128, 32))
    #screen.blit(showHeightVals, rectShowHeightVals)
    pygame.mouse.set_visible(False)
    pygame.display.update()  # updates the display surface -> anything drawn can be displayed to the player
    screen.fill((0, 0, 0))
    clock.tick(35)