#!/usr/bin/env python


import sys
from random import randint
from itertools import product
from cash import Cash
from interval import Interval


class Item:
    def __init__(self, name, period, cost):
        self.name = name
        self.period = int(period)
        #self.cost = float(cost)
        self.cost = Cash(float(cost))
        #self.cost = Interval(float(cost) * 0.9, float(cost) * 1.1)
        #self.cost = Interval(Cash(float(cost) - 0.02), Cash(float(cost) + 0.02))

    def __str__(self):
        return '{0} ({1}), every {2} months'.format(self.name, self.cost, self.period)


# Load in the list of stuff from the file.  We're going to convert it
# to a tuple before returning it, so that the order is fixed and can't
# be changed (tuples are not mutable).
def load_stuff(filename):
    stuff = []
    with open(filename, 'r') as f:
        for line in f:
            stuff.append(Item(*line.split(',')))

    print 'Got', len(stuff), 'items'
    return tuple(stuff)


def calculate_discount(n):
    if n >= 5:
        return 0.85
    else:
        return 1.0


def evaluate_offsets(stuff, offsets, eval_period=12):
    counts = [0] * eval_period
    costs = [0.0] * eval_period

    # Find out how many items ship in each month, and a monthly cost
    for item,off in zip(stuff, offsets):
        for i in xrange(off, eval_period, item.period):
            counts[i] += 1
            costs[i] += item.cost

    # Figure out the discounts for the months that make quota
    discount = [calculate_discount(x) for x in counts]
    costs = [c * d for c,d in zip(costs, discount)]
    
    # What proportion of months did we miss the discount?
    misses = sum([x > 0.9 for x in discount])
    
    # Return the proportion of misses, and the average monthly cost
    return float(misses) / eval_period,sum(costs) / eval_period


def generate_random_offsets(stuff):
    return [randint(0, item.period - 1) for item in stuff]


def monte_carlo_best_offsets(stuff, n=1000, eval_period=12):
    # Get the initial values
    best_offsets = [0] * len(stuff)
    best_miss,best_cost = evaluate_offsets(stuff, best_offsets, eval_period)

    for i in xrange(n):
        offsets = generate_random_offsets(stuff)
        miss,cost = evaluate_offsets(stuff, offsets)

        if cost < best_cost:
            best_miss = miss
            best_cost = cost
            best_offsets = offsets

    return best_offsets


def exhaustive_best_offsets(stuff, eval_period=12):
    # Get the initial values
    best_offsets = [0] * len(stuff)
    best_miss,best_cost = evaluate_offsets(stuff, best_offsets, eval_period)

    # Build a list of lists for itertools
    all_combinations = [range(p) for p in [item.period for item in stuff]]

    # Iterate through all permutations
    for offsets in list(product(*all_combinations)):
        miss,cost = evaluate_offsets(stuff, offsets, eval_period)
        if cost < best_cost:
            best_miss = miss
            best_cost = cost
            best_offsets = offsets

    return best_offsets


def visualize(stuff, offsets, eval_period=12):
    print 'Missed: {0:.2f}, Cost: {1}'.format(*evaluate_offsets(stuff, offsets))
    w = max([len(x.name) for x in stuff])
    for item,offset in zip(stuff, offsets):
        print ('  {0:' + str(w) + 's} {1: 2}').format(item.name, offset),
        print ('.' * offset + ('X' + '.' * (item.period - 1)) * (eval_period/item.period))[:eval_period]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'stuff'

    stuff = load_stuff(filename)
    default_offsets = [0] * len(stuff)
    visualize(stuff, default_offsets, 36)
    
    print
    best_offsets = monte_carlo_best_offsets(stuff, 100, 36)
    visualize(stuff, best_offsets, 36)
 
    print
    best_offsets = exhaustive_best_offsets(stuff, 36)
    visualize(stuff, best_offsets, 36)
