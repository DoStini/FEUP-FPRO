# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:35:51 2019

@author: morei
"""

def treasure(clues):
    pos = (0,0)
    used_clues = [pos]
    if pos not in clues:
        return pos
    while True:
        pos = clues[pos]
        if pos in clues and pos not in used_clues:
            used_clues.append(pos)
        else:
            return pos