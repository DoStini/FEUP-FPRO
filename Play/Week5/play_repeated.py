# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:37:28 2019

@author: morei
"""

def repeated_letter(s):
    for _ in s:
        if s.count(_) != 1:
            return _