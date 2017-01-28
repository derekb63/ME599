#! usr/bin/env python

# Derek Bean
# ME 599
# 1/24/2017

import math
import numpy as np


# Return the value of the sum for the input value k
def sum_term(k):
    return np.divide((math.factorial(4*k))*(1103+26390*k)*np.power(396, -4*k),
                     np.power(math.factorial(k), 4))


def estimate_pi():
    # Cacluate the constant in front of the summation term
    constant = np.divide(2*np.sqrt(2), 9801)
    # initialize the first summation term for a while loop initial comparator
    k = 0
    current_sum_term = sum_term(k)
    summation = current_sum_term

    while current_sum_term > 1e-15:
        k += 1
        current_sum_term = sum_term(k)
        summation += current_sum_term

    pi_estimate = np.divide(1, constant * summation)
    return pi_estimate

if __name__ == '__main__':

    print 'Pi est: ', estimate_pi()
    print 'Error: ', estimate_pi()-math.pi
