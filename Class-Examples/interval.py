#!/usr/bin/env python

# Interval arithmetic, which we can tie in to error propagation.

class Interval:
    def __init__(self, a, b=None):
        if not b:
            b = a

        self.low = min(a, b)
        self.high = max(a, b)

    def __repr__(self):
        return '[{0}; {1}]'.format(self.low, self.high)

    def __str__(self):
        return self.__repr__()

    def __contains__(self, n):
        return self.low <= n and n <= self.high

    # Arithmetic operators
    def __add__(self, other):
        try:
            return Interval(self.low + other.low, self.high + other.high)
        except:
            return Interval(self.low + other, self.high + other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        try:
            return Interval(self.low - other.high, self.high - other.low)
        except:
            return Interval(self.low - other, self.high - other)

    def __rsub__(self, other):
        return -self + other

    def __neg__(self, other):
        return Interval(-self.low, -self.high)

    def __mul__(self, other):
        try:
            return Interval(min(self.low * other.low, self.low * other.high,
                                self.high * other.low, self.high * other.high),
                            max(self.low * other.low, self.low * other.high,
                                self.high * other.low, self.high * other.high))
        except:
            return Interval(self.low * other, self.high * other)

    # This does not handle intervals containing zero
    def __div__(self, other):
        try:
            return self.__mul__(Interval(1 / other.high, 1 / other.low))
        except:
            return Interval(self.low / other, self.high / other)

    # Comparison operators
    def __lt__(self, other):
        try:
            return self.high < other.low
        except:
            return self < Interval(other)

    def __gt__(self, other):
        try:
            return self.low > other.high
        except:
            return self < Interval(other)

    def __eq__(self, other):
        return not self < other and not self > other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other


if __name__ == '__main__':
    #i = Interval(1.0, 2.0)
    #print i / 2

    kg = Interval(79.5, 80.5)
    m = Interval(1.795, 1.805)
    
    print kg / (m * m)

    print Interval(1, 2) < Interval(3, 4)
    print Interval(1, 2) < 1.3

    c = 0
    c += Interval(1, 2)
    
