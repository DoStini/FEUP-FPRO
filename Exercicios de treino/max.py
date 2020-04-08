# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:25:51 2019

@author: morei
"""


def max_val(alist):
    max_ = 0
    if len(alist) == 1:
        return alist[0]
    else:
        if alist[0] > max_:
            max_ = alist[0]
        val = max_val(alist[1:])
        if val is not None and val > max_:
            max_ = val
    return max_