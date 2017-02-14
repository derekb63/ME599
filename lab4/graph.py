#! usr/bin/env python

# Derek Bean
# ME 599
# lab 4
# 2/7/2017

from time import time
import timeit
import numpy as np
import matplotlib.pyplot as plt
from sort import bubblesort, quicksort, insertion_sort

def graph(list_sizes=np.arange(1, 1000, 100)):
    bubble_time = []
    sorted_time = []
    quicksort_time = []
    insert_time = []

    for x in list_sizes:
        test_list = list(np.random.randint(10, size=x))

        bubble_time_start = time()
        bubblesort(test_list)
        bubble_time.append(time()-bubble_time_start)

        sort_time_start = time()
        sorted(test_list)
        sorted_time.append(time()-sort_time_start)

        quicksort_time_start = time()
        quicksort(test_list)
        quicksort_time.append(time()-quicksort_time_start)
        
        insert_time_start = time()
        insertion_sort(test_list)
        insert_time.append(time()-insert_time_start)
        
    plt.loglog(list_sizes, bubble_time, '-o')
    plt.loglog(list_sizes, sorted_time, '-s')
    plt.loglog(list_sizes, quicksort_time, '-v')
    plt.loglog(list_sizes, insert_time, '-x')

    plt.xlabel('List Length')
    plt.ylabel('Sort Time (s)')
    plt.title('List Sort Time for Various Methods')
    plt.legend(['Bubble Sort', 'Sorted', 'Quicksort', 'Insertion Sort'], loc=2)

    plt.show()

if __name__ == '__main__':
    graph()
