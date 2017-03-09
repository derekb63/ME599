#!/usr/bin/env python


from rps import *


if __name__ == '__main__':
    players = [Obsessive(), Random(), TitForTat()]
    
    tournament(players, 10000, False)
    tournament(players, 10000, True)
    
