import random
import threading
import pygame

def random_num_map(size):
    mapper = []
    for x in range(size[0]):
        mapper.append([])
        for y in range(size[1]):
            mapper[x].append((random.random()))
    return mapper

def center_adder(size):
    mapper = []
    for x in range(size[0]):
        mapper.append([])
        for y in range(size[1]):
            mapper[x].append(.5 - (((x- size[0]*.5)**2 + (y - size[1] * .5)**2) / size[0]**2))
    return mapper

def better_random_gen(size):
    center_map = center_adder(size)
    random_map = random_num_map(size)
    for x in range(size[0]):
        for y in range(size[1]):
            center_map[x][y] /= random_map[x][y]
            center_map[x][y] *= .3
    return center_map

def thing_noise(row_3, percent_change, squarelike, dividing_factor):
    up_percent = 1 + percent_change
    down_percent = 1 - percent_change
    output = row_3

    for x in range(len(output)):
        for y in range(len(row_3[x])):
            surrondings = 0
            surrondings += row_3[x][y]

            if x + 1 < len(row_3):
                surrondings += row_3[x+1][y]

            if x - 1 > 0:
                surrondings += row_3[x-1][y]

            if y + 1 < len(row_3):
                surrondings += row_3[x][y+1]

            if y - 1 > 0:
                surrondings += row_3[x][y-1]

            if squarelike:
                if y - 1 >= 0 and x - 1 >= 0:
                    surrondings += row_3[x-1][y-1]
                if y - 1 >= 0 and x + 1 < len(row_3):
                    surrondings += row_3[x+1][y-1]
                if y + 1 < len(row_3[x]) and x - 1 >= 0:
                    surrondings += row_3[x-1][y+1]
                if y + 1 < len(row_3[x]) and x + 1 < len(row_3):
                    surrondings += row_3[x+1][y+1]

            #surrondings *= len(output) - (x+1) + (x+1) - len(output) + len(output[0]) - (y + 1) + (y +1) - len(output[0])

            surrondings /= dividing_factor
            if surrondings >= .5:
                output[x][y] = row_3[x][y] * up_percent
                #output[x].append(row_3[x][y] * up_percent)
            if surrondings < .5:
                output[x][y] = row_3[x][y] * down_percent
    return output



# def noise_generator(size, percent_change):
#     mapper =



def print_map(mapper):
    for i in range(len(mapper)):
        print(mapper[i])

mapper =  random_num_map((10, 10))

#print_map(mapper)
# #print('-'
#       ''
#       ''
#       ''
#       ''
#       '-')


#print_map(thing_noise(mapper, 0.1))
