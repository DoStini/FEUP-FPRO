# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:46:09 2019

@author: morei
"""

def recursive_dot(l1, l2):
    sum_ = 0
    if len(l1) == 0:
        return 0
    if type(l1[0]) == int:
        sum_ += l1[0] * l2[0]
    else:
        val = recursive_dot(l1[0], l2[0])
        if val is not None:
            sum_ += val

    val = recursive_dot(l1[1:], l2[1:])
    if val is not None:
        sum_ += val
    return sum_