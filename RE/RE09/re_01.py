# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:38:15 2019

@author: morei
"""

sort_by_f = lambda alist: sorted(alist, key=lambda x: x if x>=5 else 5-x, reverse=True)