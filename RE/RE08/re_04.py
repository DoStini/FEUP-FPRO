# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 11:27:35 2019

@author: morei
"""

def rec(matrix, word, pos):
    if len(word) == 1 and word == matrix[pos[0]][pos[1]]:
        return True
    
    elif matrix[pos[0]][pos[1]] != word[0]:
        return None
    else:   
        for x in range(-1,2):
            for y in range(-1,2):
                curr_x = pos[0] + x
                curr_y = pos[1] + y
                if in_bounds(curr_x, curr_y, len(matrix)) and pos != [curr_x, curr_y]:
                    val = rec(matrix, word[1:], [curr_x, curr_y])
                    if val: return True

def in_bounds(x, y, matrix_size):
    if 0 <= x < matrix_size and 0 <= y < matrix_size:
        return True
    else:
        return False
