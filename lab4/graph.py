#! usr/bin/env python

# Derek Bean
# ME 599
# lab 4
# 2/7/2017

from time import time
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from sorting_functions import bubblesort, quicksort, insertionsort


bubble_time = []
sorted_time = []
quicksort_time = []
insert_time = []
list_sizes = np.arange(1, 10000, 10)


for x in tqdm(list_sizes):
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
    insertionsort(test_list)
    insert_time.append(time()-insert_time_start)
    
plt.loglog(list_sizes, bubble_time)
plt.loglog(list_sizes, sorted_time)
plt.loglog(list_sizes, quicksort_time)
plt.loglog(list_sizes, insert_time)

plt.xlabel('List Length')
plt.ylabel('Sort Time (s)')
plt.title('List Sort Time for Various Methods')
plt.legend(['Bubble Sort', 'Sorted', 'Quicksort', 'Insertion Sort'])

plt.show()
