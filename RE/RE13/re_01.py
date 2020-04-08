# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:41:36 2020

@author: morei
"""

from urllib import request
import string

def longest_word(url):
    
    # Tratamento Web
    response = request.urlopen(url)
    html = response.read().decode()
    print(type(html))
    for cmd in string.punctuation.replace("-", ""):
        html = html.replace(cmd, " ")
    words = html.split()    
    words = set(words)
    
    
    # Tratamento Ficheiro
    
    with open("words", "r") as file:
        dic = file.read().split()
    dic = set(dic)
    
    final = words & dic
    final = sorted(list(final), key=lambda x: (-len(x), x))

    
    return final[0]