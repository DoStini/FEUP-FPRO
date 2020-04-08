# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:33:00 2019

@author: morei
"""

def tic_tac_toe(board, player):
    board = [list(board[x:x+3]) for x in range(0, len(board), 4)]
    dic = {0:"A", 1:"B", 2:"C"}
    
    for x, line in enumerate(board):
        for y, val in enumerate(line):
            if val != " ":
                continue
            col = [x[y] for x in board]
            diag1 = {(0,0):board[0][0], (1,1):board[1][1], (2,2):board[2][2]}
            diag2 = {(0,2):board[0][2], (1,1):board[1][1], (2,0):board[2][0]}
            ## CHECKAR NA LINHA
            if line.count(player) == 2:
                return dic[x] + str(y+1)
            ## CHEKCAR NA COLUNA
            elif col.count(player) == 2:
                return dic[x] + str(y+1)
            elif ((x,y) in diag1 and (list(diag1.values()).count(player) == 2)
                or (x,y) in diag2 and (list(diag2.values()).count(player) == 2)):
                return dic[x] + str(y+1)