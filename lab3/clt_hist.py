#!usr/bin/env python

# Derek Bean
# ME 599
# 1/31/2017

# Show how the central limit theorem works using a histogram. 

from random import random
import matplotlib.pyplot as plt


# Calculate the sum of 10 random numbers from 0 to 1
def uniform_sum():
	sum = 0
	for i in range(10):
		sum += random()
	return sum

num_samples = 1000

# Limits of the values of a sum of numbers between 0 and 1
x_range = [0, 10]


def gen_hist_val(num_samples):
	hist_vals = []
	for i in range(num_samples):
		hist_vals.append(uniform_sum())
	return hist_vals

plt.figure(1)
n, bins, patches = plt.hist(gen_hist_val(num_samples), num_samples/10, color='blue')
plt.xlabel('Value of sum')
plt.ylabel('Number of occurrences')
plt.show()
