# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:47:15 2019

@author: morei
"""

def intervale(alist1, alist2):
    final = []
    if len(alist1) <= len(alist2):
        list1 = alist1
        list2 = alist2
    else:
        list1 = alist2
        list2 = alist1
    for idx, val in enumerate(list1):
        if type(val) != list:
            final.append(val)
            final.append(list2[idx])
        else:
            final.extend(intervale(val, list2[idx]))
    return final