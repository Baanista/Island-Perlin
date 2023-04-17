import random
import threading
import pygame
import math

def random_num_map(size, seed):
    mapper = []


    for x in range(size[0]):
        mapper.append([])
        for y in range(size[1]):
            random.seed(seed)
            random.seed(random.random() * x)
            random.seed(random.random() * y)
            mapper[x].append((random.random()))
    return mapper

# def random_num_map(size):
#     mapper = []
#     for x in range(size[0]):
#         mapper.append([])
#         for y in range(size[1]):
#             mapper[x].append(.75)
#
#     for i in range(round((size[0] + size[1])*.5)):
#         mapper[random.randrange(0, size[0])][random.randrange(0, size[1])] = 5
#
#
#     return mapper

def center_adder(size):
    mapper = []
    for x in range(size[0]):
        mapper.append([])
        for y in range(size[1]):
            mapper[x].append(.5 - (((x- size[0]*.5)**2 + (y - size[1] * .5)**2) / size[0]**2))
    return mapper

def better_random_gen(size, seed):
    center_map = center_adder(size)
    random_map = random_num_map(size, seed)
    for x in range(size[0]):
        for y in range(size[1]):
            center_map[x][y] += 0
            center_map[x][y] /= random_map[x][y] * .3
            center_map[x][y] *= .3

    return center_map

def thing_noise(mapper, percent_change, squarelike, dividing_factor):
    up_percent = 1 + percent_change
    down_percent = 1 - percent_change
    output = mapper

    for x in range(len(output)):
        for y in range(len(mapper[x])):
            surrondings = 0
            surrondings += mapper[x][y]

            if x + 1 < len(mapper):
                surrondings += mapper[x+1][y]

            if x - 1 > 0:
                surrondings += mapper[x-1][y]

            if y + 1 < len(mapper):
                surrondings += mapper[x][y+1]

            if y - 1 > 0:
                surrondings += mapper[x][y-1]

            if squarelike:
                if y - 1 >= 0 and x - 1 >= 0:
                    surrondings += mapper[x-1][y-1]
                if y - 1 >= 0 and x + 1 < len(mapper):
                    surrondings += mapper[x+1][y-1]
                if y + 1 < len(mapper[x]) and x - 1 >= 0:
                    surrondings += mapper[x-1][y+1]
                if y + 1 < len(mapper[x]) and x + 1 < len(mapper):
                    surrondings += mapper[x+1][y+1]

            #surrondings *= len(output) - (x+1) + (x+1) - len(output) + len(output[0]) - (y + 1) + (y +1) - len(output[0])

            surrondings /= dividing_factor
            if surrondings >= .5:
                output[x][y] = mapper[x][y] * up_percent
                #output[x].append(row_3[x][y] * up_percent)
            if surrondings < .5:
                output[x][y] = mapper[x][y] * down_percent
    return output



# def noise_generator(size, percent_change):
#     mapper =



def print_map(mapper):
    for i in range(len(mapper)):
        print(mapper[i])

def create_noise(how_developed, seed, island_like, size, percent_change, dividing_factor):

    if island_like:
        mapper = better_random_gen(size, seed)
    else:
        mapper = random_num_map(size, seed)
    for i in range(how_developed):
        #mapper = thing_noise(mapper, .01, squarelike=False, dividing_factor=6)
        mapper = thing_noise(mapper, percent_change, squarelike=False, dividing_factor=dividing_factor)

    return mapper

