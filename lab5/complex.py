#! usr/bin/env python

# Derek Bean
# ME 599
# lab 5
# 2/14/2017

import numpy as np

class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im < 0:
            sign = '-'
        else:
            sign = '+'
        return '({0} {1} {2}i)'.format(self.re, sign, abs(self.im))

    def __add__(self, other):
        try:
            return Complex(self.re + other.re, self.im + other.im)

        except:
            return Complex(self.re + Complex(other).re,
                           self.im + Complex(other).im)

    def __radd__(self, other):
            return self.__add__(other)

    def __mul__(self, other):
        try:
            return Complex((self.re * other.re)-(self.im * other.im),
                           self.re * other.im + self.im * other.re)

        except:
            return Complex(self.re * other, self.im * other) 

    def __invert__(self):
        return Complex(self.re, -self.im)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        try:
            temp = self * other.__invert__()
            return  Complex(float(temp.re) / float((other * other.__invert__()).re),
                            float(temp.im) / float((other * other.__invert__()).re))

        except:
            temp = Complex(re=other, im=0)
            return self.__div__(temp)

    def __rdiv__(self, other):
        temp = Complex(re=other, im=0)
        return temp.__div__(self)

    __repr__ = __str__

def roots(a=0, b=0, c=0):
    if (a is 0 and b is not 0) or \
       (a is 0 and c is not 0) or \
       (a is 0 and b is 0 and c is 0):
        print 'The input is not a quaradtic equation'
    else:
        under_root = b**2 - (4*a*c)

        if under_root < 0: 
            return (Complex((float(-b) / (2*a)), np.sqrt(abs(under_root)) / (2 * a)),
                    Complex((float(-b) / (2*a)), -np.sqrt(abs(under_root)) / (2 * a)))

        elif (under_root == 0):
            return (-b / (2*a))

        elif (under_root > 0):
            return ((-b + np.sqrt(under_root)) / (2 * a),
                    (-b - np.sqrt(under_root)) / (2 * a))


if __name__ == '__main__':
    a = Complex(1, 2)
    b = Complex(3, 4)

    print 'a: ', a
    print 'b: ', b

    print 'a + b: ', a + b
    print 'a + 1: ', a + 1
    print '1 + a: ', 1 + a

    print '2 * a: ', 2 * a
    print 'a * 2: ', a * 2
    print 'a * b: ', a * b

    print '2 / a: ', 2 / a
    print 'a / 2: ', a / 2
    print 'a / b: ', a / b

    print '1, 2, -3: ', roots(1, 2, -3)
    print '1, -6, 9: ', roots(1, -6, 9)
    print '1, 3, 3: ', roots(1, 3, 3)
    
