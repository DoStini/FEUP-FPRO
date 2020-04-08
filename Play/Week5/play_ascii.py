# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:42:27 2019

@author: morei
"""

def greatest_member(atuple):
    total = 0
    for a in atuple:
        sum_ = 0
        if type(a) == str:
            for b in a:
                sum_ += ord(b)
        else:
            sum_ += sub_tuple(a)
        if sum_ > total:
            win = a
            total = sum_
    return win
            

def sub_tuple(in_tup):
    total = 0
    for a in in_tup:
        if type(a) == str:
            for b in a:
                total += ord(b)
        else:
            total += sub_tuple(a)

    return total