!/usr/bin/env python


from random import randint
from itertools import combinations


ROCK,PAPER,SCISSORS = ROCK_PAPER_SCISSORS = range(3)
NAME = dict(zip(ROCK_PAPER_SCISSORS, 'Rock Paper Scissors'.split()))


WINNERS = {
    (ROCK, SCISSORS):'smashes',
    (PAPER, ROCK): 'covers',
    (SCISSORS, PAPER): 'cuts'
}


def winner(a, b):
    if (a,b) in WINNERS:
        return 1,0,WINNERS[(a,b)]
    elif (b,a) in WINNERS:
        return 0,1,WINNERS[(b,a)]
    else:
        return 0,0,'draws with'


def play(a, b, n=1, verbose=True):
    # Cumulative scores
    a_total = 0
    b_total = 0

    for i in xrange(n):
        # Each player selects a move
        a_move = a.play(b.name)
        b_move = b.play(a.name)
    
        # Allow the players to learn from experience
        a.learn(b.name, b_move)
        b.learn(a.name, a_move)

        # Figure out who won
        a_score,b_score,verb = winner(a_move, b_move)
        a_total += a_score
        b_total += b_score

        # Print out the results
        if verbose:
            if a_score > b_score:
                print a.name, 'wins:', NAME[a_move], verb, NAME[b_move]
            elif b_score > a_score:
                print b.name, 'wins:', NAME[b_move], verb, NAME[a_move]
            else:
                print NAME[a_move], verb, NAME[b_move]

    if verbose:
        if a_total > b_total:
            print a.name, 'wins with', a_total, 'out of', n
        elif b_total > a_total:
            print b.name, 'wins with', b_total, 'out of', n
        else:
            print "It's a draw!"

    return a_total,b_total


def tournament(players, n, for_real=True):
    totals = {}
    for p in players:
        totals[p.name] = 0

    # Run through all possible pairings
    for a,b in combinations(players, 2):
        # Play a round
        a_score,b_score = play(a, b, n, False)

        
        totals[a.name] += a_score
        totals[b.name] += b_score

    # Print out the winners, if it's for real
    if for_real:
        ordering = sorted(totals, key=totals.get, reverse=True)
        width = max([len(p) for p in ordering])

        title = 'place  name' + ' '*(width - 2) + 'score'
        print title
        print ''.join(['=' if c.isalpha() else c for c in title])
        for i,p in enumerate(ordering):
            print ('{0: 2}     {1:' + str(width) + 's}  {2}').format(i+1, p, totals[p])


# Always play the same (random) move
class Obsessive:
    def __init__(self, name='Obsessive'):
        self.name = name
        self.move = randint(0, 2)

    def play(self, name):
        return self.move

    def learn(self, name, move):
        pass


# Simple player that always returns a random move
class Random:
    def __init__(self, name='RandomRPS'):
        self.name = name

    def play(self, name):
        return randint(0,2)

    def learn(self, name, move):
        pass


# Play the last move your opponent played
class TitForTat:
    def __init__(self, name='TitForTat'):
        self.name = name
        self.opponent_last_move = randint(0,2)

    def play(self, name):
        return self.opponent_last_move

    def learn(self, name, move):
        self.opponent_last_move = move


if __name__ == '__main__':
    a = Random()
    b = TitForTat()
    c = Obsessive()

    play(a, c, 3)

