# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:04:29 2019

@author: morei
"""

def move_ball(board):
    pos = [0,0]
    DIC = {'E':[0,1], 'N':[-1,0], 'W':[0,-1], 'S':[1, 0]}
    dir = ""
    board, pos, dir = setup(board)
    path = [(pos[0], pos[1])]
    while board[pos[0]][pos[1]] != "X":
        pos[0], pos[1] = pos[0] + DIC[dir][0], pos[1] + DIC[dir][1]
        bit = board[pos[0]][pos[1]]
        if bit == "\\" or bit == "/":
            dir = rotate(dir, bit)
        path.append(tuple(pos))

    return path

def rotate(dir, obs):
    DIC = {"/":{"N":"E", "S":"W", "E":"N", "W":"S"}, "\\":{"N":"W", "S":"E", "E":"S", "W":"N"}}
    return DIC[obs][dir]

def setup(board):
    for x,val in enumerate(board):
        board[x] = list(val)
        for y in range(len(board[x])):
            if board[x][y] == "E" or board[x][y] == "N" or board[x][y] == "W" or board[x][y] == "S":    
                pos = [x,y]
                dir = board[x][y]
                break
    
    return board, pos, dir   