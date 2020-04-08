# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:00:19 2019

@author: morei
"""

def map(pos, steps):
    new_pos = tuple()
    dic = {"up":(0, 1), "down":(0, -1), "left":(-1, 0), "right":(1, 0)}
    if len(steps) == 1:
        new_pos = (dic[steps[0]][0] + pos[0], dic[steps[0]][1] + pos[1])
        return new_pos
    else:
        val = map(pos, steps[1:])
        new_pos += (val[0] + dic[steps[0]][0], val[1] + dic[steps[0]][1],)
        return new_pos