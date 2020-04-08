# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:45:40 2019

@author: morei
"""

import random


def bulls_cows(seed):
    random.seed(seed)
    player = random.randrange(10000)
    guess_list = list(str(player))
    
    def closure(correct):
        correct = list(str(correct))
        guess = guess_list
        print(guess, correct)
        cows, guess, correct = check_cows(guess, correct)
        bulls = check_bulls(guess, correct)
        return cows, bulls
    
    def check_cows(guess, correct):
        guess_, correct_ = guess.copy(), correct.copy()
        counter = 0
        for x in range(len(guess)):
            if guess[x] == correct[x]:
                counter += 1
                guess_.remove(guess[x])
                correct_.remove(guess[x])
        return counter, guess_, correct_
    
    def check_bulls(guess, correct):
        counter = 0
        for x in guess:
            if x in correct:
                counter += 1
                correct.remove(x)
        return counter
    
    return closure