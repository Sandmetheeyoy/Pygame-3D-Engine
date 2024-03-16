# importing all kinds of stuff
from setup import *
from lighting import *
import pygame
# player all data and functions


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
        self.prevCoordContact = ()
        self.prevCoordContactWall = ()
        self.zLimits = (0, 0)
        self.headBob = 0
        self.headBobCount = 0


    def raycast(self, x, y, base_dir):
        dir = base_dir+45
        base_dir_rad = math.radians(base_dir)

        # floorcasting
        for i in range(screen_data_size):
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
                gx += dx * 4
                gy -= dy * 4
                distance += 4 # incrementation of distance

                if (int(gx/32) >= 31 or int(gx/32) <= 0 or int(gy/32) > 22 or int(gy/32) < 0):
                    break
                if (map_data[int((gy-dy*4)/32)][int((gx+dx*4)/32)] == 1) and self.coordContact != (int(gy/32), int(gx/32)):

                    if height_map[int((gy+dy*4)/32)][int((gx-dx*4)/32)][0] <= height_map[int((gy-dy*4)/32)][int((gx+dx*4)/32)][0]:
                        dist = distance*math.cos((base_dir_rad-dir_rad)) # recording of distance

                        self.coordContact = (int(gy/32), int(gx/32))

                        wall_renders.append(dist)
                        wall_renders_height.append(height_map[int(((gy-dy*4)/32))][int(((gx+dx*4)/32))])

                        # drawing light
                        var_shadow.append(min(light_maps[int((gy+dy*4)/32)][int((gx-dx*4)/32)], 235))


            for lw in range(len(wall_renders)):
                len_wall = wall_renders[len(wall_renders)-1-lw]

                shadow = var_shadow[len(wall_renders)-1-lw]
                color = (shadow, shadow
                         , shadow)

                half_magnitude = screen_height / (len_wall+1)

                height_factor = wall_renders_height[len(wall_renders_height)-1-lw][0]/32
                height1_factor = (512-(wall_renders_height[len(wall_renders_height)-1-lw][0]+wall_renders_height[len(wall_renders_height)-1-lw][1]))/32

                # drawing lower wall
                if (screen_height/2 - half_magnitude * (24 * height_factor - self.zProjection) - 1 + self.yUp) < screen_height:

                    pygame.draw.rect(surface, color,
                                 (i * (screen_width) / screen_data_size - 1,
                                  screen_height / 2 - (half_magnitude) * (24 * height_factor - self.zProjection) - 1 + self.yUp,
                                  screen_width / screen_data_size + 1, half_magnitude * (height_factor) * 24 + 1 + half_magnitude * 24))

                # drawing upper wall
                if ((screen_height / 2 - (half_magnitude) * (
                                              24 * 16 - self.zProjection) - 1 + self.yUp)) > -(half_magnitude * (height1_factor) * 24 + 1):

                    pygame.draw.rect(surface, color,
                                 (i * (screen_width) / screen_data_size - 1,
                                  screen_height / 2 - (half_magnitude) * (
                                              24 * 16 - self.zProjection) - 1 + self.yUp,
                                  screen_width / screen_data_size + 1,
                                  half_magnitude * (height1_factor) * 24 + 1))

            dir -= 90 / screen_data_size

    def move(self, dir):
        self.xProjection = pygame.math.lerp(self.xProjection, self.x, 0.2)
        self.yProjection = pygame.math.lerp(self.yProjection, self.y, 0.2)

        keys = pygame.key.get_pressed()
        self.xprevious = self.x
        self.yprevious = self.y

        mx = math.cos(math.radians(self.faceDir))*(keys[pygame.K_w] - keys[pygame.K_s]) + math.cos(math.radians(self.faceDir+90))*(keys[pygame.K_a] - keys[pygame.K_d])
        my = math.sin(math.radians(self.faceDir))*(keys[pygame.K_w] - keys[pygame.K_s]) + math.sin(math.radians(self.faceDir+90))*(keys[pygame.K_a] - keys[pygame.K_d])
        self.x += mx * 7
        self.y -= my * 7

        if abs(mx) + abs(my) > 0.001:
            self.headBobCount += 0.3
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

        self.yUp = max(-400, min(self.yUp, 400))
        self.zAxis = max(self.zAxis - self.zSpeed, 0)
        if self.zAxis <= self.zLimits[0]:
            self.zAxis = self.zLimits[0]
            self.zSpeed = 0

            if keys[pygame.K_SPACE]:
                self.zSpeed = -self.jumpHeight

        if self.zAxis+30 > self.zLimits[0]+self.zLimits[1]:
            self.zSpeed = 1



        self.zSpeed = min(self.zSpeed + self.jumpAccel, self.gravAccel)

        self.zLimits = height_map[int(self.y/32)][int(self.x/32)]
        self.zProjection = pygame.math.lerp(self.zProjection, self.zAxis+self.headBob*3, 0.3)