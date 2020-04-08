# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:04:20 2019

@author: morei
"""
def local_minima(alist, n):
    output_ = []
    n = int(n/2)
    border = len(alist) - 1
    x = 0
    y = 1
    last_min = True
    for x in range(border +1):
        for y in range(1, n + 1):
            step = True
            if x + y <= border:
                if alist[x] > alist[x + y]:
                    step = False
                    last_min = False
                    break
            if x - y >= 0:
                if alist[x] > alist[x - y]:
                    step = False
                    last_min = False
                    break
        if not step:
            continue
        if (x != 0 and not(last_min and alist[:x].count(alist[x]) != 1)) or x == 0:
            output_.append(tuple([alist[x], x]))
            last_min = True
            
    return output_