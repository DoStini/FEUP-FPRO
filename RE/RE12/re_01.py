# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:50:05 2019

@author: morei
"""

def number_of_collisions(objects):
    col = 0
    for obj1 in objects:
        for obj2 in objects:
            if obj1 == obj2:
                pass
            else:
                if (obj1["x1"] > obj2["x2"] or obj1["x2"] < obj2["x1"]):
                    pass
                elif (obj1["y1"] > obj2["y2"] or obj1["y2"] < obj2["y1"]):
                    pass
                else:
                    col += 1
    return col//2