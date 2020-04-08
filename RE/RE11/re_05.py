# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:15:43 2019

@author: morei
"""

def longest_prefix(words):
    if len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return checker(words)
    else:
        val1 = longest_prefix(words[:2])
        val2 = longest_prefix(words[2:])
        return checker([val1, val2])

def checker(words):
    for idx, val in enumerate(words[0]):
        if idx > len(words[1]) - 1:
            return words[1]
        elif val != words[1][idx]:
            return words[0][:idx]
    return words[0]


#def gen_ran_dict(prefix, word_size, n):
#    dic = []
#    
#    for _ in range(n):
#        rng = random.Random()
#        asc = list(string.ascii_lowercase) * 10
#        rng.shuffle(asc)
#        
#        dic.append(prefix + "".join(asc[:word_size]))
#        
#    return dic