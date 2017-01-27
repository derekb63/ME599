#! usr/bin/env python

# Derek Bean
# ME 599
# 1/24/2017

# Write a function called gcd that takes parameters a and b and returns their
# greatest common divisor
# The greatest common divisor of a and b is the largest number that divides
# both with no remainder


def gcd(a, b):
    if a is not int and b is not int:
        print('The function only takes int values')
    else:
        if b is 0:
            return a
        else:
            # The divmod function returns a tuple (quotient, remainder) and
            # divmod(a,b)[1] returns the remainder of a/b
            greatest_common_divisor = gcd(b, divmod(a, b)[1])
        return greatest_common_divisor
if __name__ == "__main__":
    a = 12
    b = 8
    if gcd(a, 0) is a:
        print('gcd returned the correct value')
    else:
        print('gcd did not return the correct value')

    if gcd(a, b) is 4:
        print('gcd returned the correct value')
    else:
        print('gcd did not return the correct value')
