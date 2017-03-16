#!/usr/bin/env python


from rps import *
from beande import Beande
from cowand import cowand

if __name__ == '__main__':
    players = [cowand(), Beande()]

    tournament(players, 10000, False)
    tournament(players, 10000, True)
    
