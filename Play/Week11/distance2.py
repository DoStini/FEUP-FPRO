# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:57:08 2019

@author: morei
"""

from math import sqrt

def closest_pair(points):
    points = sorted(points, key=lambda x: x[0])

    def recursive(points):
        min_ = 999999999999
        if len(points) <= 3:
            for x in points:
                for y in points:
                    if x!=y:
                        if dist(x,y) < min_:
                            min_ = dist(x,y)
            return min_
        else:
            l1, l2 = points[:len(points)//2], points[len(points)//2:]
#            if len(l1) != len(l2):
#                l1.append(l2[0])
            val1 = recursive(l1)
            val2 = recursive(l2)
            xdis = recursive([l1[-1],l2[0]])
            min_ = min((val1,val2, xdis))
#            for x in l1:
#                for y in l2:
#                    if abs(x[0] - y[0]) < min_ and dist(x, y) < min_:
#                        min_ = dist(x, y)        
        return min_  
    def dist(p1, p2):
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    l1, l2 = points[:len(points)//2], points[len(points)//2:]
    min_ = recursive(points)
    for x in l1:
        for y in l2:
            if abs(x[0] - y[0]) < min_ and dist(x, y) < min_:
                min_ = dist(x, y)
    return round(min_)
