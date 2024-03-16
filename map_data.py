# map data and height values
import random

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

#height_map = [
    # [[64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [511, 0], [511, 0], [511, 0], [511, 0], [511, 0], [511, 0], [511, 0], [511, 0], [511, 0],
    #  [511, 0], [511, 0], [511, 0], [148, 72], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [148, 72], [148, 72], [148, 72], [148, 72], [148, 72], [148, 72], [148, 72], [148, 72],
    #  [148, 72], [148, 72], [148, 72], [148, 72], [148, 72], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [136, 72], [136, 72], [136, 72], [136, 72], [148, 72], [148, 72], [148, 72], [148, 72],
    #  [148, 72], [148, 72], [148, 72], [148, 72], [148, 72], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [120, 72], [120, 72], [120, 72], [120, 72], [148, 72], [148, 72], [148, 72], [148, 72],
    #  [148, 72], [148, 72], [148, 72], [148, 72], [148, 72], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [100, 72], [100, 72], [100, 72], [100, 72], [148, 72], [148, 72], [148, 72], [148, 72],
    #  [148, 72], [148, 72], [148, 72], [148, 72], [148, 72], [64, 448], [64, 448], [64, 448], [499, 0], [499, 0],
    #  [499, 0], [499, 0], [499, 0], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [88, 72], [88, 48], [88, 48], [88, 48], [511, 0], [96, 160], [96, 160], [96, 160], [96, 160],
    #  [96, 160], [96, 160], [96, 160], [96, 160], [64, 448], [64, 448], [64, 448], [499, 0], [96, 448], [112, 448],
    #  [128, 448], [499, 0], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [88, 48], [88, 48], [88, 48], [88, 48], [88, 48], [96, 160], [96, 160], [96, 160], [96, 160],
    #  [96, 160], [96, 160], [96, 160], [96, 160], [64, 448], [64, 448], [64, 448], [499, 0], [80, 448], [64, 448],
    #  [144, 448], [499, 0], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [88, 48], [88, 48], [88, 48], [88, 48], [511, 0], [96, 160], [96, 160], [96, 160], [96, 160],
    #  [96, 160], [96, 160], [96, 160], [96, 160], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [160, 448], [499, 0], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [88, 48], [88, 48], [88, 48], [88, 48], [88, 48], [96, 160], [96, 160], [96, 160], [96, 160],
    #  [96, 160], [96, 160], [96, 160], [96, 160], [64, 448], [64, 448], [64, 448], [499, 0], [208, 448], [192, 448],
    #  [176, 448], [499, 0], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [88, 48], [88, 48], [88, 48], [88, 48], [511, 0], [96, 160], [96, 160], [96, 160], [96, 160],
    #  [96, 160], [96, 160], [96, 160], [96, 160], [64, 448], [64, 448], [64, 448], [499, 0], [64, 448], [64, 448],
    #  [64, 448], [499, 0], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [88, 48], [88, 48], [88, 48], [88, 48], [88, 48], [96, 160], [96, 160], [96, 160], [96, 160],
    #  [96, 160], [96, 160], [96, 160], [96, 160], [64, 448], [64, 448], [64, 448], [499, 0], [499, 0], [499, 0],
    #  [499, 0], [499, 0], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [88, 48], [88, 48], [88, 48], [88, 48], [511, 0], [96, 160], [96, 160], [96, 160], [96, 160],
    #  [96, 160], [96, 160], [96, 160], [96, 160], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [88, 48], [88, 48], [88, 48], [88, 48], [88, 48], [96, 160], [96, 160], [96, 160], [96, 160],
    #  [96, 160], [96, 160], [96, 160], [96, 160], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [88, 48], [88, 48], [88, 48], [88, 48], [511, 0], [96, 160], [96, 160], [96, 160], [96, 160],
    #  [96, 160], [96, 160], [96, 160], [96, 160], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [88, 48], [88, 48], [88, 48], [88, 48], [511, 0], [96, 160], [96, 160], [96, 160], [96, 160],
    #  [96, 160], [96, 160], [96, 160], [96, 160], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [88, 48], [88, 48], [64, 448], [88, 48], [511, 0], [511, 0], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448]],
    # [[64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]],
    # [[64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448], [64, 448],
    #  [64, 448], [64, 448]]
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
                height_map_add.append([64, 488])

            map_data.append(array_map_add)
            height_map.append(height_map_add)


MAXIMUM_HEIGHT = 1024
height_sects = [499, 0] # for level editing
height_change_counter = 0

# rendering
screen_data_size = 180
level_editing_mode = False


# map_data_string = 'mapdata1.dd3dm'
# height_data_string = 'heightdata1.dd3dm'
#
# def writeFile(filename, data):
#     write_file = open(filename, 'a')
#     for i in range(len(filename)):
#         write_file.write(str(data[i]))
#
# writeFile(map_data_string, map_data)