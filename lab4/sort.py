#! usr/bin/env python

# Derek Bean
# ME 599
# lab 4
# 2/7/2017

from time import time
import numpy as np
import random
import matplotlib.pyplot as plt


def bubblesort(to_sort):
    if is_sorted(to_sort) == True:
        return to_sort
        
    for x in range(len(to_sort)):
        for idx in range(len(to_sort)-1):
            if to_sort[idx] > to_sort[idx+1]:
                to_sort[idx+1], to_sort[idx] = to_sort[idx], to_sort[idx+1]
    return to_sort


def is_sorted(check_list):
    if all([check_list[x] <= check_list[x+1] for x in range(len(check_list)-1)]):
        return True
    else:
        return False


def quicksort(to_sort):
    if is_sorted(to_sort) == True:
        return to_sort
        
    elif len(to_sort) == 2:
        sorted_list = [min(to_sort), max(to_sort)]
        return sorted_list
        
    elif len(to_sort) == 3:
        min_val = to_sort.pop(to_sort.index(min(to_sort)))
        max_val = to_sort.pop(to_sort.index(max(to_sort)))
        mid_val = to_sort
        sorted_list = [min_val, mid_val, max_val]
        return sorted_list
        
    pivot = random.choice(to_sort)
    smaller = [i for i in to_sort if i < pivot]
    larger = [i for i in to_sort if i >= pivot]
    
    sorted_list = quicksort(smaller) + quicksort(larger)
    return sorted_list

   
def insertion_sort(to_sort):
    if is_sorted(to_sort) == True:
        return to_sort
        
    for x in range(len(to_sort)+1):
        key = to_sort[x-1]
        j = x-2
        while j >= 0 and to_sort[j] > key:
            to_sort[j+1], to_sort[j] = to_sort[j], to_sort[j+1]
            j = j-1
        to_sort[j+1] = key
    return to_sort
if __name__ == '__main__':

    list_sizes = np.arange(10, 200, 10)
    # Check to see if the sort functions work
    for x in list_sizes:
        test_list = list(np.random.randint(10, size=x))
    
        if is_sorted(bubblesort(test_list[:])) is False:
            print 'bubblesort did not sort test list of length {0}'.format(x)
    
        if is_sorted(quicksort(test_list[:])) is False:
            print 'quicksort did not sort test list of length {0}'.format(x)
    
        if is_sorted(insertionsort(test_list[:])) is False:
            print 'insertion did not sort test list of length {0}'.format(x)

    # Plot the time taken for 10 bubblesorts
    bubble_time = []
    for i in range(10):
        start = time()
        bubblesort(list(np.random.randint(10, size=list_sizes[-1])))
        bubble_time.append(time()-start)
    print 'The average time for bubble sort on a random list of length' + \
          ' {0} is {1:.4f} seconds for 10 runs'.format(list_sizes[-1],
                                                       np.mean(bubble_time))
