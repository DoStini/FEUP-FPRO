# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 08:50:26 2019

@author: morei
"""

def four_in_line(board):
    lines = board
    columns = [[li[x] for li in board] for x in range(len(lines[0]))]
    
    for x in range(len(board)):
        for y in range(len(board[0])):
            c = board[x][y]
            if c != 0:
                if check_line(board, [x,y], 1, c):
                    return {(x,y), check_line(board, [x,y], 1, c)}
                elif check_line(board, [x,y], 0, c):
                    return {(x,y), check_line(board, [x,y], 0, c)}
                elif check_diag(board, [x,y], c):
                    return {(x,y), check_diag(board, [x,y], c)}
                
                
    return lines, columns


def check_diag(board, pos, colour):
    # down to up
    counter = 0
    pos_copy = pos.copy()
    while pos_copy[0] >= 0 and pos_copy[1] < len(board[0]):
        if board[pos_copy[0]][pos_copy[1]] != colour:
            break
        counter += 1
        if counter == 4:
            return tuple(pos_copy)
        pos_copy[0] -= 1
        pos_copy[1] += 1
    counter = 0
    pos_copy = pos.copy()
    # up to down
    while pos_copy[0] < len(board) and pos_copy[1] < len(board[0]):
        if board[pos_copy[0]][pos_copy[1]] != colour:
            break
        counter += 1
        if counter == 4:
            return tuple(pos_copy)
        pos_copy[0] += 1
        pos_copy[1] += 1
    return False

def check_line(board, pos, axis, colour):
    max_ = len(board[0]) if axis == 1 else len(board)
    counter = 0
    while pos[axis] < max_:
        if board[pos[0]][pos[1]] != colour:
            return False
        counter += 1
        if counter == 4:
            return tuple(pos)
        pos[axis] += 1

    return False
    
#def check_list(li, colour):
#    check = False # started counting
#    counter = 0
#    for item in li:
#        if item == colour:
#            check = True
#            counter += 1
#        else:
#            check = False
#            counter = 0
#        if counter == 4:
#            return True
#    return False