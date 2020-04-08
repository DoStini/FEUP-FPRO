# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:44:17 2019

@author: morei
"""


def paint(n, boards):
    min_ = 10000
    if n == 1:
        return max(boards)
    for x in range(len(boards)):
        new_board = boards[:x]
        val = paint(n-1, boards[x:])
        if len(new_board) != 0 and val is not None:
            if max(new_board) + val < min_:
                min_ =  max(new_board) + val
        else:
            continue
    return min_

print(paint(3, [60, 70, 10, 20, 40, 50, 10, 40]))

#def paint(n, boards, step=0):
#    #board = recursive(n, boards)
#    #print("l", board)
#    current_max = 1000
#    current_list = []
#    if n == 1 and step != 0:
#        return boards
#    elif n == 1:
#        return max(boards)
#    for x in range(len(boards)):
#        painter = boards[:x+1]
#        next_painter = paint(n-1, boards[x+1:], step+1)
#        if len(next_painter) != 0:
##            print(painter, next_painter)
#            sum_ = max(painter) + val(next_painter)
#            if sum_ < current_max and len(painter) != 0 and len(next_painter) != 0:
#                current_max = sum_
#                current_list = []
#                current_list.append(painter)
#                current_list.append(next_painter)
#    print(step)
#    if step == 0:
#        return val(current_list)
#    else:
#        return current_list
#
#
#def val(board):
#    sum_ = 0
#    for x in board:
#        if type(x) == list:
#            sum_ += val(x)
#        else:
#            sum_ += max(board)
#            return sum_
#    return sum_