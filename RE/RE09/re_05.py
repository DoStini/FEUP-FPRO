# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:10:28 2019

@author: morei
"""

from functools import reduce


def reduce_map_filter(args):
    dic = {"map": lambda op, lista: list(map(op, lista)), 
           "filter": lambda op, lista: list(filter(op, lista)), 
           "reduce": lambda op, lista: reduce(op, lista)
           }
    if type(args[2]) == tuple:
        val = dic[args[0]](args[1], reduce_map_filter(args[2]))
    else:
        val = dic[args[0]](args[1], args[2])
    return val