# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:36:03 2019

@author: morei
"""

def sort_by_value(dic):
    list_ = dic.items()
    list_ = sorted(list_, key = lambda x: x[1])
    return list_