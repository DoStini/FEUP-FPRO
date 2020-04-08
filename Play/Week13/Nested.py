# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:55:02 2020

@author: morei
"""

def nested_exceptions(tree):
    out = []
    for func in tree:
        if callable(func):
            try:
                func()
                out.append(False)
            except Exception as err:
                out.append(True)
        else:
            out.append(nested_exceptions(func))
    return tuple(out)