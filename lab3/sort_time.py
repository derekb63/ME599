#!usr/bin/env python

# Derek Bean
# ME 599
# 1/31/2017

# plot the time taken to sort lists of varying lengths

from random import randint
import time

def rand_list(length):
	random_list = []
	for i in range(length):
		random_list.append(randint(0,length))
	return random_list

list_length = [1, 10, 100, 1000, 10000, 100000, 1000000]

for val in list_length:
	sort_time = []
	sum_time = []
	to_sort = rand_list(val)
	sort_start = time.time()
	sorted(to_sort)
	sort_end = time.time()
	sort_time.append(sort_end-sort_start)

	sum_start = time.time()
	sum(to_sort)
	sum_end = time.time()
	sum_time.append(sum_end-sum_start)

print sort_time, sum_time
