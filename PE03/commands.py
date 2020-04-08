# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 11:04:45 2019

@author: morei
"""

def process(commands):
    dic = {"|": lambda x,y: x | y, "-":lambda x,y: x - y, "&": lambda x,y: x & y, "x":lambda x,y: cart(x,y)}
    
    if len(commands) == 1:
        return commands[0]
    else:
        s1,c,s2 = commands[0], commands[1], commands[2]
        out = dic[c](s1,s2)
        if len(commands) == 3: 
            return out
        else:
            val2 = process(commands[4:])
            out = dic[commands[3]](out,val2)
        return out    



def cart(s1,s2):
    out = set({})
    for x in s1:
        for y in s2:
            out.add((x,y))
    return out