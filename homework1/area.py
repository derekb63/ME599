#! usr/bin/env python

# Derek Bean
# ME 599
# Homework 1
# 1/24/2017

'''
The function area usies Monte Carlo Integration to deterine the area of a shape
Specifically, it uses rejection sampling to find the density

    Inputs:
        f: the function for which the area is calculated
        p1: defines the forst corner of the bounding box around the area
        p2: defines the second corner of the bounding box around the area
        samples: sets how many samples to use for the integration

    Outputs:
        area: the area of the arbitrary shape input to the function
'''

from types import LambdaType
import numpy as np
import matplotlib.pyplot as plt

'''
The function area usies Monte Carlo Integration to deterine the area of a shape
Specifically, it uses rejection sampling to find the density

    Inputs:
        f: the function for which the area is calculated
        p1: defines the forst corner of the bounding box around the area
        p2: defines the second corner of the bounding box around the area
        samples: sets how many samples to use for the integration

    Outputs:
        area: the area of the arbitrary shape input to the function
'''


def area(f, p1, p2, samples=1e4):
    if isinstance(f, LambdaType) is False:
        print 'The input function is not of type LambdaType'
        return None
    # Create an array of random points
    limits = []
    for i in xrange(len(p1)):
        limits.append([p1[i], p2[i]])

    test_area = abs(limits[0][0]-limits[0][1])*abs(limits[1][0]-limits[1][1])

    test_points = []
    for i in limits:
        test_points.append((max(i) - min(i)) *
                           np.random.random_sample((int(samples), 1)) + min(i))
    test_points = np.transpose(test_points)
    count = 0
    for j in test_points[0]:
        if f(*j) <= 0:
            count += 1

    area = (test_area/float(samples))*count
    return area


# Function to define the implicit eqution of a circle
def circle(x, y):
    return x * x + y * y - 1


if __name__ == '__main__':
    p1 = (-2, -2)
    p2 = (2, 2)

    error = []
    samples = np.linspace(10, 1e4, 100)
    for k in samples:
        a = area(circle, p1, p2, k)
        error.append(abs(np.pi - a)/np.pi)
    plt.loglog(samples, error)
    plt.xlabel(r'Number of random samples')
    plt.ylabel(r'Error')
    plt.title(r'Error for Monte Carlo Estimation of $\pi$')
    plt.show()
