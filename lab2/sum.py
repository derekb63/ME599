#! usr/bin/env python

# Derek Bean
# ME 599 
# 1/24/2017


# Find the sum of a list of numbers using a for loop
def sum_i(list):
	list_sum = 0
	for i in list:
		list_sum += i
	return list_sum
	

# Caclulate the sum of a list of numbers using recursion
def sum_r(list):
	list_sum = 0
	
	return list_sum
	
	
if __name__ == '__main__':
	example_list = [1, 2, 3, 4, 5, 6]
	if sum_i(example_list) != sum(example_list):
		print 'The function sum_i has returned an incorrent value'
	else:
		print 'sum_i returned the correct value'
		
	if sum_r(example_list) != sum(example_list):
		print 'The function sum_r has returned an incorrent value'
	else:
		print 'sum_r returned the correct value'