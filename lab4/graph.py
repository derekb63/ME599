#! usr/bin/env python

# Derek Bean
# ME 599
# lab 4
# 2/7/2017

from time import time
import numpy as np
import matplotlib.pyplot as plt
from sorting_functions import *


bubble_time = []
sorted_time = []
list_sizes = np.arange(100, 2000, 100)
for x in list_sizes:
    test_list = list(np.random.randint(10, size=x))
    # Test if a list is sorted
    bubble_time.append(bubblesort(test_list)[1])
    if is_sorted(bubblesort(test_list)[0]) is False:
        print 'bubblesort did not sort test list #{0}'.format(x)
    sort_time_start = time()
    sorted(test_list)
    sorted_time.append(time()-sort_time_start)
plt.loglog(list_sizes, bubble_time)
plt.loglog(list_sizes, sorted_time)
plt.xlabel('List Length')
plt.ylabel('Sort Time (s)')
plt.title('List Sort Time for Various Methods')
plt.legend(['Bubble Sort', 'Sorted'])
plt.show()
