#! usr/bin/env python

# Derek Bean
# ME 599
# Homework 1
# 1/24/2017

from types import LambdaType
import numpy as np
import matplotlib.pyplot as plt
'''
Integrate uses the right rectangle rule to determine the definite integral of
the input function
    Inputs:
        f: a lambda function to be inetgrated
        a: the lower bound of the variables
        b: the upper bound of the variables
        step: the step size or delta used for the integration

    Outputs:
        value: the value resulting from the definite integration
'''


def integrate(f, a, b, step=0.001):
    if isinstance(f, LambdaType) is False:
        print 'The input function is not of type: LambdaType'
        return None
#    elif len(a) != len(b):
#        print 'The interval variables a and b do not have the same length'
#        return None
    try:
        float(step)
    except:
        print 'The step size is not one of the accepted types: int or float'
        return None
    else:
        # This try block is for computing the integral of an n variable
        # function f(x,y,z,...,n) with except block being for a function
        # of x only.
        try:
            value = 0
            limits = []
            delta = [step]*len(a)
            try:
                for i in xrange(len(a)):
                    limits.append([a[i], b[i]])
            except:
                limits = [a, b]
            interval = []
            for idx, val in enumerate(limits):
                interval.append(np.arange(val[0], val[1]+step, step))
            interval = np.transpose(interval)
            for i in interval:
                value += f(*i)*np.prod(delta)
            return value
        except:
            interval = np.arange(a, b+step, step)
            for i in interval:
                value += f(i)*step
            return value


# Function to define the implicit eqution of a circle
def circle(x, y):
    return x * x + y * y - 1


def line(x):
    return x

if __name__ == '__main__':
    # Test the integral of a circle
    test_function = circle
    a = (-1, -1)
    b = (1, 1)

    area_circle = integrate(test_function, a, b)
    print 'Circle Error : ', abs(area_circle)

    # Test the integral of a line at different steps
    area_line = []
    steps = np.linspace(1e-6, 0.1, 1000)
    for i in steps:
        area_line.append(integrate(line, 0, 1, i))
    error = [abs(i-0.5) for i in area_line]
    plt.plot(steps, error, '-k')
