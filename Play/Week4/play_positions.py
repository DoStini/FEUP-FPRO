# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:01:31 2019

@author: morei
"""


def get_positions(sentence, word_list):
    sentence = sentence.split()
    output = ""
    check = []
    for x in word_list:
        check.append(False)
    if sentence[0] in word_list and sentence[1] in word_list and len(sentence) == 2 and len(word_list) == 3:
        for word in sentence:
            for idx, b in enumerate(word_list):
                if word == b and not check[idx]:
                    check[idx] = True
                    output += str(idx) + " "
                    break
        return output
    else:
        return("")