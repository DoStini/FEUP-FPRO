# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:19:41 2019

@author: morei
"""

def summary_ranges(astring):
    astring = astring.split(",")
    output = []
    output.append([astring[0]])
    y = 0
    for x in range(0, len(astring) - 1):
        if x != len(astring) - 1:
            if int(astring[x + 1]) - int(astring[x]) == 1:
                output[y].append(astring[x + 1])
            else:
                y += 1
                output.append([])
                output[y].append(astring[x + 1])
    aux = []
    for a in output:
        if len(a) != 1:
            aux.append(f"{a[0]}->{a[len(a) - 1]}")
        else:
            aux.append(a[0])
    
    return ",".join(aux)