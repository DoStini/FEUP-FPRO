# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:41:19 2020

@author: morei
"""

def rec_exceptions(alist):
    out = []
    
    for f in alist:
        try:
            if type(f()) == list:
                out.extend(rec_exceptions(f()))
        except Exception as error:
            out.append(error)
    return out
