#! usr/bin/env python

# Derek Bean
# ME 599
# lab 4
# 2/7/2017

from time import time
import numpy as np
import matplotlib.pyplot as plt

# Implement the bubblesort algorithm that takes a list of numbers and returns the sorted version of the list

def bubblesort(to_sort):
	start = time()
	for x in range(len(to_sort)):
		for idx in range(len(to_sort)-1):
			if to_sort[idx] > to_sort[idx+1]:
				to_sort[idx+1], to_sort[idx] = to_sort[idx], to_sort[idx+1]
	return to_sort, time()-start


def is_sorted(check_list):
	if check_list == sorted(check_list):
		return True
	else:
		return False


def quicksort(to_sort):
	if len(to_sort) == 1 or len(to_sort) == 0:
		return to_sort
	pivot = to_sort[int(len(to_sort)/2)]
	smaller = [ i for i in to_sort if i <= pivot]
	larger = [ i for i in to_sort if i > pivot]
	sorted = quicksort(smaller) + pivot + quicksort(larger)
	return sorted


if __name__ == '__main__':
	list_sizes = np.arange(100, 200, 100) 

	for x in list_sizes:
		test_list = list(np.random.randint(10, size=x))
		# Test if a list is sorted
		if is_sorted(bubblesort(test_list)[0]) is False:	
			print 'bubblesort did not sort test list #{0}'.format(x)
	test_list = list(np.random.randint(10, size=10))
	print test_list
	print quicksort(test_list)
	



