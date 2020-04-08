# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:35:26 2019

@author: morei
"""

def fetch_middle(llists):
    out = []
    for lisp in llists:
        len_ = len(lisp)
        if len_ % 2 == 0:
            idx = [int(len_/2-1), int(len_/2)]
            print(idx)
            out.append((lisp[idx[0]] + lisp[idx[1]]) / 2)
        else:
            idx = int((len_ - 1) / 2)
            out.append(lisp[idx])
    return out