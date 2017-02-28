#!/usr/bin/env python


from random import randint
from itertools import product


# Generate a list of stuff, buying period, and offset from a file
def load_stuff(filename):
    stuff = {}
    with open(filename, 'r') as f:
        for line in f:
            item,period = line.split(',')
            stuff[item] = (int(period), 0)

    print 'Got', len(stuff), 'items'
    
    return stuff


def evaluate_offsets(stuff, eval_period=12):
    counts = [0] * eval_period

    for item,times in stuff.iteritems():
        period,offset = times
        for i in xrange(offset, eval_period, period):
            counts[i] += 1

    # How many months have a bad number of items?  Return proportion
    # of months with this bad number.
    return float(len(filter(lambda x: x > 0 and x < 5, counts))) / eval_period


def generate_random_offsets(stuff):
    new_stuff = {}
    for item,times in stuff.iteritems():
        new_stuff[item] = (times[0], randint(0, times[0] - 1))
    return new_stuff


def monte_carlo_best_offsets(stuff, n=1000, eval_period=12):
    # This first evaluation lets us specify a default value
    best_offsets = stuff
    best_value = evaluate_offsets(stuff, eval_period)

    for i in xrange(n):
        new_stuff = generate_random_offsets(stuff)
        value = evaluate_offsets(new_stuff)
        if value < best_value:
            best_value = value
            best_offsets = new_stuff

        # Short-circuit the calculation.  Why not equal to zero?
        # Representation error!
        if abs(best_value) < 1.0 / eval_period:
            break
        
    # Why i and not n here?  Because it reports actual samples
    print 'Tried', i + 1, 'Monte Carlo samples'

    return best_offsets

def exhaustive_best_offsets(stuff, eval_period=12):
    items = [x for x in stuff]
    period = [x[1][0] for x in stuff.iteritems()]
    
    # Build a list of lists for itertools
    all_combinations = []
    for p in period:
        all_combinations.append(range(p))

    # Found this by Googling "permutations lists python"
    new_stuff = {}
    best_value = evaluate_offsets(stuff, eval_period)
    best_offset = stuff

    for offset in list(product(*all_combinations)):
        for i,o in zip(items, offset):
            new_stuff[i] = (stuff[i][0], o)
            
            value = evaluate_offsets(new_stuff, eval_period)
            if value < best_value:
                best_value = value
                best_offsets = new_stuff

            # Short-circuit the calculation.  Why not equal to zero?
            # Representation error!
            if abs(best_value) < 1.0 / eval_period:
                break

    return best_offsets


# Visualize as Xs
def visualize(stuff, eval_period=12):
    w = max([len(x) for x in stuff])
    for item,times in stuff.iteritems():
        period,offset = times
        print ('{0:' + str(w) + '}: {1}').format(item,
                                                 ('.' * offset + ('X' + '.' * (period - 1))) * (eval_period / period))

        
# What about incorporating the cash value of the items, to maximize
# the discount, then adding in filler items?  Can we calculate the
# filler automatically?
if __name__ == '__main__':
    stuff = load_stuff('stuff')
    visualize(stuff, 36)
    
    best_offsets = monte_carlo_best_offsets(stuff, 100000)
    #best_offsets = exhaustive_best_offsets(stuff)
    print
    visualize(stuff, 36)

    #print 'Value:', evaluate_offsets(best_offsets)
    #for item,number in best_offsets.iteritems():
    #    print '  {0}: every {1} months, offset {2}'.format(item, *number)

    
