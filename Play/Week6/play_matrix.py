# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:58:14 2019

@author: morei
"""

import copy

def is_orthogonal(mx):
    mxt = transpose(mx)
    result = []
    for x in range(len(mx)):
        result.append(list(mx.copy()))
    for x in range(len(mx)):
        for y in range(len(mx)):
            result[x][y] = mx[x][0]*mxt[0][y] + mx[x][1]*mxt[1][y]
    print(result)
    prev = result[0][0]
    for x in range(len(result)):
        for y in range(len(result)):
            if x == y and result[x][y] != 1 or x != y and result[x][y] != 0:
                return False
    return True
    
def transpose(mat):
    new_mat = []
    new_mat = copy.deepcopy(mat)
    for x in range(len(mat)):
        for y in range(len(mat)):
            new_mat[y][x] = mat[x][y]
    return new_mat