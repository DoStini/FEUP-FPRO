# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:29:30 2019

@author: morei
"""

def greatest(num):
    out = ""
    len_ = len(str(num))
    num_ = split_num(num)
    while len(out) != len_:
        out += str(max(num_))
        num_.remove(max(num_))
        
    return int(out)
        
def split_num(num):
    result = [0]
    while num > 0:
        result.clear()
        result.append(num%10)
        num //= 10
    return(result)
    
print(greatest(012))