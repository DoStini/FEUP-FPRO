# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 08:28:22 2020

@author: morei
"""

def diff(filename1, filename2):
    
    with open(filename1) as f1:
        f1 = f1.read().split("\n")[:-1]
    with open(filename2) as f2:
        f2 = f2.read().split("\n")[:-1]
    out = []
    
    for idx in range(len(f1) if len(f1) > len(f2) else len(f2)):
        if idx < len(f1) and f1[idx] not in f2: out.append("- " + f1[idx])
        if idx < len(f2) and f2[idx] not in f1: out.append("+ " + f2[idx])
    return "\n".join(out)