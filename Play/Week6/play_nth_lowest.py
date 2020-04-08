# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:05:20 2019

@author: morei
"""

def nth_lowest(lnum, n):
    lnum = sorted(lnum)
    print(lnum)
    return lnum[n-1]