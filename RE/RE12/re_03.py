# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:11:16 2019

@author: morei
"""

import cards, random

def card_value(card):
    score = 0
    if card[1].isalpha():
        score += 10
        if card[1] == "A":
            score += 1
    else:
        score += int(card[1])
    if card[0] in "♠♣":
        score *= 2
    return score    

def play(seed):
    random.seed(seed)
    deck = cards.create_deck(True)
    scores = {1:0, 2:0, 3:0, 4:0}
    hand = cards.deal_hands(deck)
    players = [1,2,3,4]
    start_player = cards.choose(players)
    player_order = cards.player_order(players, start_player)
    hand = {x:hand[x-1] for x in player_order}
    print(hand)
    print(player_order)
    for x in range(13):
        score = {1:0, 2:0, 3:0, 4:0}
        for player in hand:
            card = cards.choose(hand[player])
            #print(card, card_value(card), x, f"P{idx+1}")
            hand[player].remove(card)
            score[player] += card_value(card)
        win = max(list(score.values()))
        for player in score:
            if score[player] == win:
                scores[player] += 1
        print(score, scores)
    win = max(list(scores.values()))
    return " ".join(["P"+ str(x) for x in scores if scores[x] == win])
    #return hand