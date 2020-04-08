# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:08:04 2019

@author: morei
"""

def palindrome_index(s):
    if is_palindrome(list(s)):
        return -1
    s = list(s)
    for idx, val in enumerate(s):
        s.pop(idx)
        if is_palindrome(s):
            return idx
        else:
            s.insert(idx, val)
    return -1
    
def is_palindrome(s):
    t = clone_list(s)
    t.reverse()
    if t == s:
        return True
    else:
        return False
  
def clone_list(in_):
    clone = []
    for _ in in_:
        clone.append(_)
    return clone