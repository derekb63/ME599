#!/usr/bin/env python


def f(a, b=0):
    print a
    print b
    print
    
def g(a, b=0, *c):
    print a
    print b
    print c
    print

def h(a, b=0, *c, **d):
    print a
    print b
    print c
    print d
    print


if __name__ == '__main__':
    f(1)
    f(1, 2)
    #f(1, 2, 3)

    x = (1, 2)
    f(x)
    f(*x)

    #y = (1, 2, 3)
    #f(*y)

    z = {'a':2, 'b':3}
    f(**z)

    z['foo'] = 12
    #f(**z)
    
    g(1)
    g(1, 2)
    g(1, 2, 3)
    g(1, 2, 3, 4)
    
    h(1)
    h(1, 2)
    h(1, 2, 3)
    h(1, 2, 3, 4)
    h(1, 2, 3, 4, foo=5)
    h(**z)
