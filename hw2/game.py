#!/usr/bin/env python


from rps import *
from beande import Beande

if __name__ == '__main__':
    players = [Beande(), TitForTat(), Obsessive(), Random()]

    tournament(players, 10000, False)
    tournament(players, 10000, True)
    
