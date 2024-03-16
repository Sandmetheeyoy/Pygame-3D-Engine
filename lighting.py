# lighting module
# light mapping
from map_data import *
import math
light_coords = [[677.2021004443403, 367.3692750895706]]


# LIGHTMAPS
light_maps = []
if len(map_data) > 0:
    for i in range(len(map_data)):
        light_level = []
        for j in range(len(map_data[0])):
            light_level.append(16)
        light_maps.append(light_level)


# light_production
def light_raycasts(x, y):
    #prevCoords = [-10000, -10000]
    traversedCoords = []
    # first direction
    for dir in range(90):
        xx, yy = int(x/32)*32+16, int(y/32)*32+16
        steps = 235

        for s in range(64):

            xx += math.cos(math.radians(dir*4))*4
            yy -= math.sin(math.radians(dir*4))*4

            steps = max(steps - 4, 16)
            if [int(xx/32), int(yy/32)] not in traversedCoords: # if it is not filled, then fill it.
                light_maps[int(yy/32)][int(xx/32)] += steps
                if height_map[int(yy/32)][int(xx/32)][1] < 1:
                    break
            #print([int(xx/32), int(yy/32)] != prevCoords)



            traversedCoords.append([int(xx/32), int(yy/32)])

# casting light (doesn't even work well)
for i in range(len(light_coords)):
    light_raycasts(light_coords[i][0], light_coords[i][1])