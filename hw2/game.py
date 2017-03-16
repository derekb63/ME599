#!/usr/bin/env python


from rps import *
from beande import MyPlayer

if __name__ == '__main__':
    players = [TitForTat(), Obsessive(), MyPlayer(), Random()]
    tournament(players, 10000, False)
    tournament(players, 10000, True)
    
