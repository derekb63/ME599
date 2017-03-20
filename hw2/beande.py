#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:27:16 2017

@author: beande
"""
import random


class MyPlayer:
    def __init__(self, name='beande'):
        self.name = name
        self.opp_history = []
        self.history = [random.randint(0,2)]
        random.seed = 1

    def next_move(self):
        other_move = self.history[0]
        if other_move is 0:
            play = 1
        elif other_move is 1:
            play = 2
        else:
            play = 0
        return play

    def play(self, name):
        try:
            play = self.move
        except:
            play = random.randint(0, 2)
        self.history.append(play)
        return play

    def learn(self, opp_name, opp_move):
        del opp_name
        self.opp_history.append(opp_move)
        # For dealing with the obsessive player
        same_move = len(set(self.opp_history)) is 1 and len(self.opp_history) is 5
        if same_move is True:
            move_name = set(self.opp_history).pop()
            if move_name is 0:
                self.move = 1
            elif move_name is 2:
                self.move = 0
            elif move_name is 1:
                self.move = 2  
        # Detect the tit for tat player
        elif self.history.pop(-2) is opp_move:
            self.move = self.next_move()
        # If it is not either player default to random with the init seed
        else:
            try:
                del self.move
            except:
                pass
            self.opp_history = []

if __name__ == '__main__':
    player = MyPlayer()
    print player.play('beande')
