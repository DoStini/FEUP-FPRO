# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:57:35 2019

@author: morei
"""

def permuta(alist, step=0):
    lista = []
    for x in range(len(alist)):
        alist_copy = alist.copy()
        alist_copy[x] = alist[0]
        alist_copy[0] = alist[x]
        if alist_copy not in lista:     
            lista.append(alist_copy)
        new_list = [alist_copy[0]]
        lists = permuta(alist_copy[1:])
        for val in lists:
            if val is not None:
                lista.append(new_list + val)
    output = []
    for x in lista:
        if x not in output:
            output.append(x)
    return output