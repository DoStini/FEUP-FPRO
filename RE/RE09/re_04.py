# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:56:01 2019

@author: morei
"""

#def override(l1, l2):
#    l2 += list(filter(lambda x: x[0] not in [y[0] for y in l2], l1))
#    return sorted(l2, key=lambda x: x[0])

override = lambda l1, l2: sorted(l2 + list(filter(lambda x: x[0] not in [y[0] for y in l2], l1)), key=lambda x: x[0])