# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:27:46 2019

@author: morei
"""

def anagrams(alist):
    group = []
    check = []
    x = 0
    for _ in range(len(alist)):
        check.append(False)
    for idx1, item1 in enumerate(alist):
        group.append([])
        group[x].append(item1)
        item1 = list(item1.replace(" ", "").lower())
        item1 = sorted(item1)
        for idx2, item2 in enumerate(alist):
            item2 = list(item2.replace(" ", "").lower())
            item2 = sorted(item2)
            if idx1 < idx2 and item1==item2 and not check[idx2]:
                check[idx1] = True
                check[idx2] = True
                group[x].append(alist[idx2])
        x += 1
    aux = 0
    final = []
    while aux < len(group):
        if len(group[aux]) >= 2:
            group[aux] = sorted(group[aux], key=lambda item: item.replace(" ","").lower())
            final.append(group[aux])
        aux += 1
    if False in check:
        idx = check.index(False)
        final.append([alist[idx]])
    final = sorted(final, key=lambda item: "".join(item).replace(" ","").lower())
    return final