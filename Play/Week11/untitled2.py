# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:40:00 2019

@author: morei
"""

def try_rec(points, step=0):
    l1, l2 = points[:len(points)//2], points[len(points)//2:]
    if len(l1) != len(l2):
        print("end",step)
        return points
    else:
        val1 = try_rec(l1, step+1)
        val2 = try_rec(l2, step-1)
        return val1, val2