# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:43:51 2019

@author: morei
"""

def rm_letter_rev(l, astr):
    rv = ""
    len_ = len(astr)
    for x in range(len_):
        if l not in astr[len_ - 1 - x].lower():
            rv += astr[len_- 1 - x]
    return rv

print(rm_letter_rev("s", "A style guide is about consistency"))