# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:54:47 2019

@author: morei
"""

def palindrome(astring):
    subs = sub_strings(astring)
    counter = 0
    for sub in subs:
        if sub == sub[::-1]:
            counter += 1
    return "The string '{0}' contains {1} palindrome substrings.".format(astring, counter)
    
    
def sub_strings(astring):
    len_ = len(astring)
    list_ = []
    for x in range(len_):
        for y in range(len(astring)):
            byte = astring[y: x+1]
            if len(byte) != 0 and len(byte) != 1:
                list_.append(byte)
    return(list_)
print(sub_strings("ababa"))
print(palindrome("ababa"))