#! usr/bin/env python

# Derek Bean
# ME 599
# lab 5
# 2/14/2017


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
            return Complex(self.re * other.re, self.im * other.im)

        except:
            return Complex(self.re * Complex(other).re,
                           self.im * Complex(other).im)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if Complex(other).im == 0:
            try:
                return Complex((self.re / other.re), self.im)

            except:
                return Complex((self.re / Complex(other).re), self.im)
        else:
            try:
                return Complex(self.re / other.re, self.im / other.im)

            except:
                return Complex(self.re / Complex(other).re,
                               self.im / Complex(other).im)

    def __rdiv__(self, other):
        return self.__div__(other)

    __repr__ = __str__

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
