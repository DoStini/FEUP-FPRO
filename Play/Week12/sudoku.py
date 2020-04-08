# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 22:15:46 2019

@author: morei
"""

def solve_sudoku(board):
    lines = [x for x in board]
    columns = [[y[x] for y in board] for x in range(len(board))]
    squares = [[lines[y][x:x+3] + lines[y+1][x:x+3] + lines[y+2][x:x+3] for x in range(0,7,3)] for y in range(0,7,3)]
    dic = {(0,1,2):0, (3,4,5):1, (6,7,8):2}
    dic = {y:dic[x] for x in dic for y in x}

    to_fill = []
    
    for x, line in enumerate(lines):
        for y, val in enumerate(line):
            if val == 0:
                to_fill.append((x,y))
                
    for pos in to_fill:
        sx = make_set([x for x in range(1,10) if x not in lines[pos[0]]])
        sy = make_set([x for x in range(1,10) if x not in columns[pos[1]]])
        sb = make_set([x for x in range(1,10) if x not in squares[dic[pos[0]]][dic[pos[1]]]])
        print(sx,sy,sb, columns[pos[1]])
        val = (sx&sy)&sb
        for x in val:
            lines[pos[0]][pos[1]] = x
    return lines

def make_set(lista):
    out = set({})
    for x in lista:
        out.add(x)
    return out