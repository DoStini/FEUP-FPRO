# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:54:14 2019

@author: morei
"""
l, s = int(input()), int(input())
r = l

if not (r > s):
    l = r
    r = s
    s = l
    
while True:
    if not (s > r):
        r -= s
        continue
    if not r == 0:
        l = r
        r = s
        s = l
        continue
    print(s)
    break