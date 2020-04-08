# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:06:28 2019

@author: morei
"""

from functools import reduce

#
#def map_filter_reduce(lst, f1, f2, f3):
#    lst = filter(f1, lst)
#    lst = map(f2, lst)
#    return reduce(f3, lst)


map_filter_reduce = lambda lst, f1, f2, f3: reduce(f3, map(f2, filter(f1, lst)))