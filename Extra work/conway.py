# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:52:14 2019

@author: morei
"""

import matplotlib.pyplot as plt
from time import sleep
from random import randint
#seed must be [[1, 2], [1,3]] for live cells in positions 1:2 and 1:3
#grid setup
#x0:y0,y1,y2,y3
#x1:y0,y1,y2,y3
#x2:y0,y1,y2,y3
def conway(grid_size=50, iterations=1000, run_time_interval=0.01, seed=[]):
    grid = grid_setup(grid_size, seed) 
    plt.figure()
    for _ in range(iterations):
        plt.clf()
        x_map = []
        y_map = []
        grid = generation(grid)
        for x in range(grid_size):
            for y in range(grid_size):
                if grid[x][y] == 1:
                    x_map.append(x)
                    y_map.append(y)
        plt.xlim(0, grid_size)
        plt.ylim(0, grid_size)
        plt.plot(x_map, y_map, "ks") 
        plt.tight_layout()
        plt.draw()
        plt.pause(run_time_interval)
        
def grid_setup(grid_size, seed):    
    grid = []
    for x in range(grid_size):
        grid.append([])
        for y in range(grid_size):
            grid[x].append(randint(0, 1))
    if grid!=[]:
        for pos in seed:
            grid[pos[0]][pos[1]] = 1
    return grid

def generation(grid):
    temp_grid = []
    for _ in range(len(grid)):
        temp_grid.append([])
        for __ in range(len(grid)):
            temp_grid[_].append(grid[_][__])
    for x in range(len(grid)):
        for y in range(len(grid)):
            result = analyse([x,y], grid)
            if result < 2:
                temp_grid[x][y] = 0
            elif result > 3:
                temp_grid[x][y] = 0
            elif result == 3 and temp_grid[x][y] == 0:
                temp_grid[x][y] = 1
    return temp_grid

def analyse(pos, aux_grid): #pos [x][y]
    pos_x = pos[0]
    pos_y = pos[1]
    border = len(aux_grid) - 1
    counter = 0
    for x in range (-1, 2):
        for y in range(-1, 2):
            curr_x = pos_x + x
            curr_y = pos_y + y

            if(curr_x < 0 or curr_x > border or curr_y < 0 or curr_y > border):
                continue
            elif aux_grid[curr_x][curr_y] == 1 and (x != 0 or y != 0):
                counter += 1
    return counter 