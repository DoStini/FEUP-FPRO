# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:36:03 2019

@author: morei
"""

def rearrange(l):
    return [x for x in l if x <= 0] + [x for x in l if x > 0]