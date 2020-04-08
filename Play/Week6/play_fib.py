# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:05:02 2019

@author: morei
"""

def fib(n):
    fib_dic = [0, 1]
    result = [0, 1]
    if n == 1:
        return result[:1]
    elif n == 2:
        return result
    for x in range(n-2):
        sum_ = fib_dic[0] + fib_dic[1]
        result.append(sum_)
        fib_dic[0] = fib_dic[1]
        fib_dic[1] = sum_
    return(result)