# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:55:52 2019

@author: morei
"""

def genealogy(l):
    l = sorted(l, key=lambda person: person[0])
    l = sorted(l, key=lambda person: ["sibling", "parent", "cousin", "grandparent"].index(person[1]))
    return l