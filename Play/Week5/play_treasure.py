# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:29:59 2019

@author: morei
"""

def map(pos, steps) :
    steps = steps.split("-")
    pos = list(pos)
    pos[1] += steps.count("up")
    pos[1] -= steps.count("down")
    pos[0] += steps.count("right")
    pos[0] -= steps.count("left")
    return(tuple(pos))