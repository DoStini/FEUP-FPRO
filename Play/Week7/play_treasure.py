# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:24:46 2019

@author: morei
"""

def treasure(clues):
    x = tuple((0,0))
    analyse = []
    while True:
        if clues[x] not in clues:
            return clues[x]
        elif x in analyse:
            return x
        else:
            analyse.append(x)
            x = clues[x]