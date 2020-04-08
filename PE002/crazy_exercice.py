# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 08:43:59 2019

@author: morei
"""

def exactly(s):
    good_pairs = tuple()
    for idx1, val1 in enumerate(s):
        if val1.isdigit():
            for idx2, val2 in enumerate(s[idx1+1:]):
                if val2.isdigit() and int(val1) + int(val2) == 10:
                    if s[idx1:idx1+idx2+1].count("?") == 3:
                        good_pairs += (val1+val2, )
                    else:
                        return f"The sequence {s} is NOT OK with first violation with pair: {(val1+val2,)}"
    return f"The sequence {s} is OK with the pairs: {good_pairs}"
        