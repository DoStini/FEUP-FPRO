# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:21:55 2019

@author: morei
"""

from math import log


def tfidf(documents):
    documents = list(map(lambda x: x.lower(), documents))
    dic = {}
    for x, sentence in enumerate(documents):
        sentence = sentence.split()
        for word in sentence:
            if word not in dic:
                dic[word] = []
                for y in range(len(documents)):
                    dic[word].append(0)
    for word in dic:
        for x in range(len(dic[word])):
            dic[word][x] = documents[x].split().count(word)
            
    for word in dic:
        word_counter = 0
        for val in dic[word]:
            if val != 0:
                word_counter += 1
        #word_counter = dic[word].count()
        print(word_counter)
        for x, val in enumerate(dic[word]):
            dic[word][x] = round(dic[word][x] * log(len(documents) / word_counter), 3)
    return dic
