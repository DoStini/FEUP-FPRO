# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:01:30 2019

@author: morei
"""

from copy import deepcopy


def min_path(matrix, a, b, visited=[]):
    for pos in visited:
        matrix[pos[0]][pos[1]] = False
    return len(find_paths(matrix, a, b))
    
    
def find_paths(matrix, a, b):
    lista = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            curr_x = a[0] + x
            curr_y = a[1] + y
            if 0 <= curr_x < len(matrix) and 0 <= curr_y < len(matrix[0]) and not (x==0 and y==0):
                if (curr_x, curr_y) != b and not matrix[curr_x][curr_y]:
                    temp_m = deepcopy(matrix)
                    temp_m[curr_x][curr_y] = True
                    val = find_paths(temp_m, (curr_x, curr_y), b)
                    if val is not None:
                        lista.append(val + [(curr_x, curr_y)])
                    else:
                        continue
                elif (curr_x, curr_y) == b:
                    return [(curr_x, curr_y)]
    if len(lista) != 0:
        return sorted(lista, key=lambda x: len(x))[0]