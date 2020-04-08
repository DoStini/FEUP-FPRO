# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:48:23 2019

@author: morei
"""

def academy_awards(alist):
    dic = {}
    for award in alist:
        dic[award[1]] = dic.get(award[1], 0) + 1
    return dic