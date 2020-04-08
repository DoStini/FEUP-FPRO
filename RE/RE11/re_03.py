# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:04:40 2019

@author: morei
"""

def binary_tree(key, tree):
    while True:
        if key > tree[0]:
            tree = tree[3]()  
            
        elif key < tree[0]:
            tree = tree[2]()
            
        else:
            return tree[1]