# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:25:06 2019

@author: morei
"""

from random import randint as rndm
import matplotlib.pyplot as plt


dic = {}
grid = []
pixel_grid = []
checker = []
GRID_SIZE = 0
def init(grid_size):
    global grid, pixel_grid, checker, GRID_SIZE
    GRID_SIZE = grid_size
    for x in range(GRID_SIZE):
        grid.append([])
        checker.append([])
        pixel_grid.append([])
        for y in range(GRID_SIZE):
            grid[x].append(0)
            checker[x].append(False)
            pixel_grid[x].append(0)


class Ocean:
    global grid, GRID_SIZE
    
    #VERY SLOW GENERATION. MAYBE DETECTED 
    # IN EACH PIXEL, GO BACK IF CURR PIXEL HAS 9 BLUE PIXELS AROUND
    # GO TO PIXELS AROUND AND UPDATE PIXEL VALUES OF ADJ AREA
    
    def __init__(self, min_area, max_area, deep_ocean_range, min_deep):
        self.name = "Ocean"
        self.min_area = min_area
        self.max_area = max_area
        self.color = "o"
        self.deep_color = "do"
        self.curr_area = 0
        self.deep_ocean_range = deep_ocean_range # lateral size to analyse
        self.min_deep = min_deep # In that square, there must be x water pixels
        self.build_biome()
        
    def build_biome(self):
        global grid, pixel_grid, GRID_SIZE
        
        plt.figure()
        
        DIRECTION = [[-1,1], [0,1]] # value to add up   # axis to change
        pos_x = rndm(0, GRID_SIZE-1)
        pos_y = rndm(0, GRID_SIZE-1)
        pos = [pos_x, pos_y]
        desired_area = rndm(self.min_area, self.max_area)
        grid[pos_x][pos_y] = self.color
        pixel_ = Pixel(self.name, self.deep_ocean_range, self.color, pos)
        pixel_grid[pos_x][pos_y] = pixel_
        x_map = []
        y_map = []

        
        while self.curr_area < desired_area:                        
            random_dir = [DIRECTION[0][rndm(0,1)], DIRECTION[1][rndm(0,1)]]
            pos[random_dir[1]] += random_dir[0]
            if not (0 <= pos[0] < GRID_SIZE  and 0 <= pos[1] < GRID_SIZE):
                pos[random_dir[1]] -= random_dir[0]
                continue
            if not checker[pos[0]][pos[1]]:
                grid[pos[0]][pos[1]] = self.color
                pixel_ = Pixel(self.name, self.deep_ocean_range, self.color, [pos[0], pos[1]])
                pixel_grid[pos[0]][pos[1]] = pixel_ ## NOT ADDING TO THE GRID!!
                checker[pos[0]][pos[1]] = True
                x_map.append(pos[0])
                y_map.append(pos[1])
                self.curr_area += 1

            plt.clf()
            plt.xlim(0, GRID_SIZE)
            plt.ylim(0, GRID_SIZE)
            plt.plot(x_map, y_map, "bs")
            plt.tight_layout()
            plt.draw()
            plt.pause(0.00001)
            

    def add_deep_ocean(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                pixel = pixel_grid[x][y]
                if pixel != 0 and pixel.parent == "Ocean" and pixel.big_area >= self.min_deep and pixel.adj_area == 9:
                    print("yes")
                    grid[x][y] = self.deep_color
                    pixel_grid[x][y].color = 2


class Biome:
    def __init__(self):
        pass
    
    def build_biome(self):
        global grid, pixel_grid, GRID_SIZE
        
        plt.figure()
        
        DIRECTION = [[-1,1], [0,1]] # value to add up   # axis to change
        pos_x = rndm(0, GRID_SIZE-1)
        pos_y = rndm(0, GRID_SIZE-1)
        pos = [pos_x, pos_y]
        desired_area = rndm(self.min_area, self.max_area)
        grid[pos_x][pos_y] = self.color
        pixel_ = Pixel(self.name, self.deep_ocean_range, self.color, pos)
        pixel_grid[pos_x][pos_y] = pixel_
        x_map = []
        y_map = []

        
        while self.curr_area < desired_area:                        
            random_dir = [DIRECTION[0][rndm(0,1)], DIRECTION[1][rndm(0,1)]]
            pos[random_dir[1]] += random_dir[0]
            if not (0 <= pos[0] < GRID_SIZE  and 0 <= pos[1] < GRID_SIZE):
                pos[random_dir[1]] -= random_dir[0]
                continue
            if not checker[pos[0]][pos[1]]:
                grid[pos[0]][pos[1]] = self.color
                pixel_ = Pixel(self.name, self.deep_ocean_range, self.color, [pos[0], pos[1]])
                pixel_grid[pos[0]][pos[1]] = pixel_ ## NOT ADDING TO THE GRID!!
                checker[pos[0]][pos[1]] = True
                x_map.append(pos[0])
                y_map.append(pos[1])
                self.curr_area += 1

            plt.clf()
            plt.xlim(0, GRID_SIZE)
            plt.ylim(0, GRID_SIZE)
            plt.plot(x_map, y_map, "bs")
            plt.tight_layout()
            plt.draw()
            plt.pause(0.00001)



                    
class Land:     
    def __init__(self):
        self.min_area = 20
        self.color = "g"
        self.curr_area = 0

class Pixel:
    def __init__(self,parent, max_dis, color, pos):
        self.parent = parent
        self.pos = pos
        self.color = color
        self.max_dis = max_dis
        self.adj_area = 0 #have to change this, put after the map is generated
        self.big_area = 0
    def calc_area(self, dis): # distance to current position CHANGE THIS VALUE SYSTEM!!
        counter = 0
        for x in range(-dis//2 + 1, dis//2 + 1):
            for y in range(-dis//2 + 1, dis//2 + 1):
                if 0 <= self.pos[0] + x < GRID_SIZE and 0 <= self.pos[1] + y < GRID_SIZE:
                    print(self.color, grid[self.pos[0]+x][self.pos[1]+y], self.pos[0]+x, self.pos[1]+y)
                    if grid[self.pos[0]+x][self.pos[1]+y] == self.color:
                        counter += 1
        return counter


def pixels_update():
    global grid, pixel_grid, checker, GRID_SIZE
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pixel_ = pixel_grid[x][y]
            if pixel_ != 0:
                pixel_grid[x][y].adj_area = pixel_.calc_area(3)
                pixel_grid[x][y].big_area = pixel_.calc_area(pixel_.max_dis)

def update_ocean_map():
    x_map = []
    y_map = []
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x][y] == "do":
                x_map.append(x)
                y_map.append(y)
    plt.xlim(0, GRID_SIZE)
    plt.ylim(0, GRID_SIZE)
    plt.plot(x_map, y_map, "ks")
    plt.tight_layout()
    plt.draw()
