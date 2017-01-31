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

num_samples = [10, 100, 1000, 10000, 100000, 1000000]

# Limits of the values of a sum of numbers between 0 and 1
x_range = [0, 10]


def gen_hist_val(num_samples):
	hist_vals = []
	for i in range(num_samples):
		hist_vals.append(uniform_sum())
	return hist_vals

plt.figure(1)
plt.subplot(611)
n, bins, patches = plt.hist(gen_hist_val(num_samples[0]), num_samples[0]/10)
plt.subplot(612)
n, bins, patches = plt.hist(gen_hist_val(num_samples[1]), num_samples[1]/10)
plt.subplot(613)
n, bins, patches = plt.hist(gen_hist_val(num_samples[2]), num_samples[2]/10)
plt.subplot(614)
n, bins, patches = plt.hist(gen_hist_val(num_samples[3]), num_samples[3]/10)
plt.subplot(615)
n, bins, patches = plt.hist(gen_hist_val(num_samples[4]), num_samples[4]/10)
plt.subplot(616)
n, bins, patches = plt.hist(gen_hist_val(num_samples[5]), num_samples[5]/10)
plt.xlabel('Value of sum')
plt.ylabel('Number of occurrences')
plt.axes(xmin=0, xmax=10)

plt.show()
