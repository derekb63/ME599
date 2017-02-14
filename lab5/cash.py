#!/usr/bin/env python


class Cash:
    # Initialization.  Takes dollars, or dollars and cents, and
    # converts it to cents internally.
    def __init__(self, dollars=0, cents=0):
        self.cents = int(dollars * 100 + cents)

    # String representation of the amount.  Note that there's a
    # special case if the value is less than zero, since the negative
    # sign goes before the $
    def __str__(self):
        if self.cents < 0:
            retval = '-'
        else:
            retval = ''
        return '{0}${1:.2f}'.format(retval, abs(self.cents / 100.0))
        #return '${0:.2f}'.format(self.cents / 100.0)

    # Standard addition: Cash + something
    def __add__(self, other):
        try:
            return Cash(0, self.cents + other.cents)
        except:
            return self + Cash(other)

    # Right-associative addition: something + Cash
    def __radd__(self, other):
        return self.__add__(other)

    # Standard subtraction, defined in terms of addition
    def __sub__(self, other):
        return self.__add__(-other)

    # Right-associative subtraction, defined in terms of addition
    def __rsub__(self, other):
        return -self + other

    # Negation, to allow subtraction to work
    def __neg__(self):
        return Cash(0, -self.cents)

    # Some function that answers a question you might have
    def a_lot(self):
        if self.cents > 1000:
            return True
        else:
            return False

if __name__ == '__main__':
    a = Cash(1.01)

    print a
    print a + a
    print a + 1
    print 1 + a
    print a - 1
    print 1 - a
