# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:21:32 2020

@author: morei
"""

def raise_exception(alist, value):
    out = []
    for x in alist:
        try:
            if x <= value:
                raise ValueError(f'{x} is not greater than {value}')
        except ValueError as error:
            out.append(error)
    return out