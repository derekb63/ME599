#!/usr/bin/env python

class Cash:
    def __init__(self, dollars=0, cents=0):
        self.cents = int(round(dollars * 100 + cents))

    def __str__(self):
        if self.cents < 0:
            return '-${0:.2f}'.format(abs(self.cents / 100.0))
        else:
            return '${0:.2f}'.format(self.cents / 100.0)

    # Arithmetic operations    
    def __add__(self, other):
        try:
            return Cash(0, self.cents + other.cents)
        except:
            return self + Cash(other)

    def __radd__(self, other):
        return self + other
        
    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Cash(0, -self.cents)

    def __mul__(self, other):
        return Cash(0, self.cents * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    # Divide by cash, return float.  Divde by a number, return Cash
    def __div__(self, other):
        try:
            return float(self.cents) / float(other.cents)
        except:
            return Cash(0, self.cents / other)

    # Comparison operators
    def __lt__(self, other):
        try:
            return self.cents < other.cents
        except:
            return self < Cash(other)

    def __gt__(self, other):
        try:
            return self.cents > other.cents
        except:
            return self > Cash(other)

    def __eq__(self, other):
        return not self < other and not self > other

    def __ne__(self, other):
        return self < other or self > other

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other


if __name__ == '__main__':
    a = Cash(1.23)
    b = Cash(3.23)

    print a < b
    print b < a

