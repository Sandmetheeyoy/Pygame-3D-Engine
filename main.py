# importing pygame module
import pygame
import math
import random

pygame.init() # initializing pygame engine
screen_width = 1250
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height)) # screen
pygame.display.set_caption("Raycasting Engine")
surface = pygame.display.set_mode((screen_width, screen_height))


# screen texture data
screen_height_sector_data = [] # screen height sector
screen_border_data = []

screen_data_size = 240
level_editing_mode = False

MAXIMUM_HEIGHT = 1024

height_sects = [200, 128] # for level editing
height_change_counter = 0

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)

# light mapping
light_coords = (688.7816196944873, 385.3241257901776)

def measure_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist



map_size = (1024, 768) # size of the fookin map
map_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

height_map = [
[[16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [0, 16], [0, 16], [0, 16], [64, 0], [64, 0], [16, 400], [16, 400], [16, 400], [16, 400], [64, 0], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [64, 0], [16, 400], [16, 400], [16, 400], [16, 400], [64, 0], [0, 16], [0, 16], [64, 0], [64, 0], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [64, 0], [64, 0], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [16, 400], [64, 0], [16, 400], [16, 400], [16, 400], [16, 400], [64, 0], [64, 0], [64, 0], [64, 0], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [64, 0], [64, 0], [64, 0], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [16, 400], [64, 0], [16, 400], [16, 400], [16, 400], [64, 0], [64, 0], [64, 0], [64, 0], [16, 400], [64, 0], [16, 400], [16, 400], [16, 400], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [64, 0], [16, 400], [16, 400], [16, 400], [64, 0], [48, 464], [48, 464], [64, 0], [64, 0], [16, 400], [16, 400], [64, 0], [64, 0], [64, 0], [64, 0], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [64, 0], [64, 0], [64, 0], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [48, 464], [48, 464], [48, 464], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [64, 0], [64, 0], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [64, 0], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [48, 464], [48, 464], [200, 0], [200, 0], [64, 0], [64, 0], [48, 64], [48, 64], [48, 64], [48, 64], [200, 0], [32, 128], [32, 128], [32, 128], [200, 0], [48, 464], [48, 464], [64, 256], [64, 0], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [64, 0], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [48, 464], [48, 464], [48, 464], [48, 464], [48, 464], [48, 464], [48, 64], [48, 64], [48, 64], [48, 64], [32, 128], [16, 128], [16, 128], [16, 128], [32, 128], [48, 464], [48, 464], [64, 256], [64, 256], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [64, 0], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [48, 464], [48, 464], [64, 0], [200, 0], [64, 0], [64, 0], [48, 64], [48, 64], [48, 64], [48, 64], [32, 128], [16, 128], [16, 128], [16, 128], [32, 128], [48, 464], [48, 464], [64, 256], [64, 256], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [48, 464], [48, 464], [48, 464], [64, 0], [64, 0], [0, 16], [64, 0], [64, 0], [48, 64], [48, 64], [48, 64], [48, 64], [32, 128], [16, 128], [16, 128], [16, 128], [32, 128], [48, 464], [48, 464], [64, 256], [64, 256], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [64, 0], [64, 0], [64, 0], [48, 464], [48, 464], [48, 464], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [48, 64], [48, 64], [48, 64], [48, 64], [32, 128], [16, 128], [16, 128], [16, 128], [32, 128], [48, 464], [48, 464], [64, 256], [64, 256], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [64, 0], [16, 400], [64, 0], [200, 0], [64, 0], [64, 0], [64, 0], [16, 400], [16, 400], [16, 400], [64, 0], [64, 0], [48, 64], [48, 64], [48, 64], [200, 0], [32, 128], [32, 128], [32, 128], [200, 0], [48, 464], [48, 464], [64, 256], [64, 0], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [64, 0], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [64, 0], [64, 0], [48, 464], [48, 64], [48, 464], [48, 464], [48, 464], [48, 464], [48, 64], [48, 64], [48, 64], [64, 0], [64, 0], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [16, 400], [64, 0], [64, 0], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [48, 64], [64, 0], [64, 0], [64, 0], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400], [64, 0], [64, 0], [16, 400], [64, 0], [64, 0], [48, 64], [48, 64], [48, 64], [64, 0], [64, 0], [64, 0], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400], [64, 0], [64, 0], [64, 0], [64, 0], [48, 64], [48, 64], [48, 64], [64, 0], [0, 16], [0, 16], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [64, 0], [48, 64], [48, 64], [48, 64], [64, 0], [0, 16], [0, 16], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [64, 0], [64, 0], [64, 0], [64, 0], [64, 0], [0, 16], [0, 16], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [0, 16], [16, 400]],
[[16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400], [16, 400]]
] # height mapping



# height mapping
if len(map_data) <= 0:
        for i in range(24):
            array_map_add = []
            height_map_add = []
            for j in range(32):
                array_map_add.append(0)
                height_map_add.append([64, 0])

            map_data.append(array_map_add)
            height_map.append(height_map_add)
            height_map[i][j] =  [64, 448]


# player
class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.xprevious, self.yprevious = x, y
        self.faceDir = 0
        self.accel = 0
        self.xProjection = self.x
        self.yProjection = self.y
        self.yUp = 24
        self.zAxis = 0
        self.zProjection = 0
        self.jumpHeight = 4
        self.jumpAccel = 0.2
        self.gravAccel = 15
        self.zSpeed = 0
        self.coordContact = ()
        self.zLimits = (0, 0)
        self.headBob = 0
        self.headBobCount = 0

        self.weapons = ["PISTOL", "SHOTGUN", "MACHINEGUN"]


    def raycast(self, x, y, base_dir):
        dir = base_dir+45
        base_dir_rad = math.radians(base_dir)
        for i in range(screen_data_size):
            index_appendance = -1
            distance = 0
            dir_rad = math.radians(dir)
            dx = math.cos(dir_rad)
            dy = math.sin(dir_rad)
            gx = x
            gy = y
            wall_renders = []
            wall_renders_height = []


            var_shadow = []
            for j in range(100):
                gx += dx*4
                gy -= dy*4
                distance += 4 # incrementation of distance

                if (int(gx/32) >= 31 or int(gx/32) <= 0 or int(gy/32) > 22 or int(gy/32) < 0):
                    break
                if (map_data[int((gy-dy*4)/32)][int((gx+dx*4)/32)] == 1) and self.coordContact != (int(gy/32), int(gx/32)):

                    if height_map[int((gy+dy*4)/32)][int((gx-dx*4)/32)][0] <= height_map[int((gy-dy*4)/32)][int((gx+dx*4)/32)][0]:
                        dist = distance*math.cos((base_dir_rad-dir_rad)) # recording of distance

                        self.coordContact = (int(gy/32), int(gx/32))


                        wall_renders.append(dist)
                        wall_renders_height.append(height_map[int(((gy-dy*4)/32))][int(((gx+dx*4)/32))])

                        # raytracing simulator
                        var_shadow.append(min(measure_distance(light_coords[0], light_coords[1], gx, gy), 233))

                        index_appendance += 1

                        height_map_contact = height_map[int((gy-dy*4)/32)][int((gx+dx*4)/32)]
                        if height_map_contact[1] == 0 or map_data[int((gy-dy*4)/32)][int((gx+dx*4)/32)] == 0:
                            break

            for lw in range(len(wall_renders)):
                len_wall = wall_renders[len(wall_renders)-1-lw]

                shadow = var_shadow[len(wall_renders)-1-lw]
                color = (235 - shadow, 235 - shadow
                         , 235 - shadow)



                #half_magnitude = screen_height - (len_wall)/400 * 00
                half_magnitude = screen_height / (len_wall)

                height_factor = wall_renders_height[len(wall_renders_height)-1-lw][0]/32
                height1_factor = (512-(wall_renders_height[len(wall_renders_height)-1-lw][0]+wall_renders_height[len(wall_renders_height)-1-lw][1]))/32

                # drawing lower wall
                if (screen_height/2 - half_magnitude * (24 * height_factor - self.zProjection) - 1 + self.yUp) < screen_height:
                    pygame.draw.rect(surface, color,
                                 (i * (screen_width) / screen_data_size - 1,
                                  screen_height / 2 - (half_magnitude) * (24 * height_factor - self.zProjection) - 1 + self.yUp,
                                  screen_width / screen_data_size + 1, half_magnitude * (height_factor) * 24 + 1 + half_magnitude * 24), 2)

                # drawing upper wall
                if ((screen_height / 2 - (half_magnitude) * (
                                              24 * 16 - self.zProjection) - 1 + self.yUp)) > -(half_magnitude * (height1_factor) * 24 + 1):
                    pygame.draw.rect(surface, color,
                                 (i * (screen_width) / screen_data_size - 1,
                                  screen_height / 2 - (half_magnitude) * (
                                              24 * 16 - self.zProjection) - 1 + self.yUp,
                                  screen_width / screen_data_size + 1,
                                  half_magnitude * (height1_factor) * 24 + 1), 2)


            dir -= 90 / screen_data_size

    def move(self, dir):
        self.xProjection = pygame.math.lerp(self.xProjection, self.x, 0.2)
        self.yProjection = pygame.math.lerp(self.yProjection, self.y, 0.2)

        keys = pygame.key.get_pressed()
        self.xprevious = self.x
        self.yprevious = self.y

        mx = math.cos(math.radians(self.faceDir))*(keys[pygame.K_w] - keys[pygame.K_s]) + math.cos(math.radians(self.faceDir+90))*(keys[pygame.K_a] - keys[pygame.K_d])
        my = math.sin(math.radians(self.faceDir))*(keys[pygame.K_w] - keys[pygame.K_s]) + math.sin(math.radians(self.faceDir+90))*(keys[pygame.K_a] - keys[pygame.K_d])
        self.x += mx * 4
        self.y -= my * 4

        if abs(mx) + abs(my) > 0.001:
            self.headBobCount += 0.2
            if self.headBobCount >= 360:
                self.headBobCount = 0
            self.headBob = math.sin(self.headBobCount)

        else:
            self.headbobCount = 0
            if abs(self.headBob) > 0.001:
                self.headBob *= 0.9
            else:
                self.headBob = 0
        map_height_index = height_map[int((self.y-my)/32)][int((self.x+mx)/32)]
        if (map_height_index[0] > self.zAxis): #or (map_height_index[1] < 12): #and map_height_index[0]+map_height_index[1] < self.zAxis+24:
            self.x = self.xprevious
            self.y = self.yprevious

        #mouse movement
        mouse_Rel = pygame.mouse.get_rel()
        pygame.mouse.set_pos((screen_width/2, screen_height/2))
        self.faceDir -= mouse_Rel[0]/5
        self.yUp -= mouse_Rel[1]/0.6

        self.zAxis = max(self.zAxis - self.zSpeed, 0)
        if self.zAxis <= self.zLimits[0]:
            self.zAxis = self.zLimits[0]
            self.zSpeed = 0

            if keys[pygame.K_SPACE]:
                self.zSpeed = -self.jumpHeight

        if self.zAxis > self.zLimits[0]+self.zLimits[1]:
            self.zSpeed = 1



        self.zSpeed = min(self.zSpeed + self.jumpAccel, self.gravAccel)

        self.zLimits = height_map[int(self.y/32)][int(self.x/32)]
        self.zProjection = pygame.math.lerp(self.zProjection, self.zAxis+self.headBob*3, 0.3)


player = Player(256, 300)


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ingame_rendering():
    player.raycast(player.xProjection, player.yProjection, player.faceDir)
    player.move(0)


def level_editing(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = pygame.mouse.get_pos()
        if not map_data[int(my/screen_height*24)][int(mx/screen_width*32)]:
            map_data[int(my/screen_height*24)][int(mx/screen_width*32)] = 1
            height_map[int(my/screen_height*24)][int(mx/screen_width*32)] = height_sects
        else:
            map_data[int(my/screen_height*24)][int(mx/screen_width*32)] = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]: # delete the entire thing
        for i in range(24):
            for j in range(32):
                map_data[i][j] = 0




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
            level_editing(event)
    if not level_editing_mode:
        ingame_rendering()


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
        pygame.draw.rect(surface, (255*(height_sects[0]/512), 255*(height_sects[0]/512), 255*(height_sects[0]/512)), (
            int(mx / screen_width * 32)*(screen_width/32),
            int(my / screen_height * 24)*(screen_height/24),
            16,
            screen_height/24
        ), 2)

        pygame.draw.rect(surface,
                         (255 * (height_sects[1] / 512), 255 * (height_sects[1] / 512), 255 * (height_sects[1] / 512)),
                         (
                             int(mx / screen_width * 32) * (screen_width / 32)+16,
                             int(my / screen_height * 24) * (screen_height / 24),
                             16,
                             screen_height / 24
                         ), 2)


    # level editing as player
    keys = pygame.key.get_pressed()
    if height_change_counter >= 60:
        height_map[int(player.y/32)][int(player.x/32)][0] = max(0, min(height_map[int(player.y/32)][int(player.x/32)][0]
                                                                       + (keys[pygame.K_l] - keys[pygame.K_j])*16, 512))
        height_map[int(player.y/32)][int(player.x/32)][1] = max(0, min(height_map[int(player.y/32)][int(player.x/32)][1]
                                                                       + (keys[pygame.K_o] - keys[pygame.K_i])*16, 512))
        height_change_counter = 0
    else:
        height_change_counter += 1

    if keys[pygame.K_m]: # pasting
        height_map[int(player.y/32)][int(player.x/32)][1] = height_sects[1]

    pygame.mouse.set_visible(False)
    pygame.display.update()  # updates the display surface -> anything drawn can be displayed to the player
    screen.fill((0, 0, 0))
    clock.tick(35)
