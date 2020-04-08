# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:49:50 2019

@author: morei
"""

def flatten(alist):
    new_list = []
    for val in alist:
        if type(val) == list:
            new_list.extend(flatten(val))
        else:
            new_list.append(val)
    return new_list