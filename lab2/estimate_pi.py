#! usr/bin/env python

# Derek Bean
# ME 599
# 1/24/2017

import math
import numpy as np


def estimate_pi():
    k = 0
    constant = np.divide(2*np.sqrt(2), 9801)
    while summation > 1e-15:
        summation = np.divide((math.factorial(4*k))*(1103+26390*k),
                              np.power(math.factorial(k), 4)*np.power(396, 4*k))
        k += 1
    
    return pi_estimate
if __name__ == '__main__':
    print(estimate_pi())