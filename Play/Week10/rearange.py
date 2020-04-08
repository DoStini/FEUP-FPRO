# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:10:19 2019

@author: morei
"""

rearrange = lambda l: [x for x in l if x <= 0] + [x for x in l if x > 0]