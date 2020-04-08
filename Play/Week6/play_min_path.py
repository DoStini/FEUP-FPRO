# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:04:50 2019

@author: morei
"""

def min_path(path):
    stack = []
    for a in path:
        if len(stack) != 0 and opposite(a) == stack[-1]:
            stack.pop()
        else:
            stack.append(a)
    return stack


def opposite(dir_):
    if dir_ == "UP":
        return "DOWN"
    elif dir_ == "DOWN":
        return "UP"
    elif dir_ == "RIGHT":
        return "LEFT"
    elif dir_ == "LEFT":
        return "RIGHT"