# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:54:48 2019

@author: morei
"""

def isomorphic(astring1, astring2):
    pos1 = {} # possible outcomes
    pos2 = {}
    for x, val in enumerate(astring1):
        out1 = True
        if x in pos1:
            if pos1[val] != astring2[x]:
                out1 = False
                break
        else:
            pos1[val] = astring2[x]
            
    for x, val in enumerate(astring2):
        out2 = True
        if x in pos2:
            if pos2[val] != astring1[x]:
                out2 = False
                break
        else:
            pos2[val] = astring1[x]
    if out1 and out2 and list(pos1.keys()) == list(pos2.values()) and list(pos1.values()) == list(pos2.keys()):
        output = []
        for x in pos1:
            output.append(tuple([x, pos1[x]]))
        return f"'{astring1}' and '{astring2}' are isomorphic because we can map:{output}"
    else:
        return f"'{astring1}' and '{astring2}' are not isomorphic"