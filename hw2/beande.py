#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:27:16 2017

@author: aero-10
"""
import random
from collections import Counter


class Beande:
    def __init__(self, name='beande'):
        self.name = name
        self.plays = {'Rock': 0, 'Paper': 1, 'Scissors': 2}
        self.opp_history = []
        self.seed = 'Paper'
        random.seed(self.plays[self.seed])

    def play(self, name):
	play = random.randint(0, 2)
        return play

    def learn(self, opp_name, opp_move):
        self.opp_history.append(opp_move)
        enough_games = len(self.opp_history)%10 == 0
        if enough_games is True:
            same_move = len(set(self.opp_history)) == 1
            if same_move is True:
                same_move_as_seed = set(self.opp_history).pop()
                if same_move_as_seed is True:
                    random.seed(random.choice(self.plays.keys()))


if __name__ == '__main__':
    player = Beande()
    print player.play('beande')
