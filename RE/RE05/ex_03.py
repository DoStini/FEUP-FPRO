# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:44:45 2019

@author: morei
"""

def find_dtype(atuple, data_type):
    out_ = ()
    for thing in atuple:
        if type(thing).__name__ == data_type:
            out_ += (thing,)
    return out_