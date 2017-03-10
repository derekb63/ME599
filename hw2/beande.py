#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:27:16 2017

@author: aero-10
"""
import random


class Beande:
    def __init__(self, name='beande'):
        self.name = name
        self.plays = {'Rock': 0, 'Paper': 1, 'Scissors': 2}
        self.history = []
        self.seed = 'Scissors'
        random.seed(self.plays[self.seed])

    def play(self, name):
        return random.randint(0, 2)

    def learn(self, opp_name, opp_move):
        self.history.append(opp_move)
        enough_games = len(self.history) == 10
        if enough_games:
            same_move = len(set(self.history)) == 1
            if same_move:
                same_move_as_seed = set(self.history).pop()
                if same_move_as_seed:
                    random.seed(random.choice(self.plays.keys()))


if __name__ == '__main__':
    player = Beande()
    print player.play('beande')
