# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:47:08 2019

@author: morei
"""

def change(money):
    dic = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    for x in dic:
        dic[x] = round(money // x, 2)
        money = round(money%x, 2)
    return dic