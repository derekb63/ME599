#!/usr/bin/env python


from time import time

count = 0

def fib(n):
    global count
    count += 1

    if type(n) != type(1) or n < 0:
        return None

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

class FibGenerator:
    def __init__(self):
        self.fib = {}
        
        # Load the file if we can.  If not, seed the dictionary with
        # the values that we know already
        try:
            with open('fibfile', 'r') as f:
                for line in f:
                    k,v = line.split()
                    self.fib[int(k)] = int(v)
        except IOError:
            self.fib[0] = 0
            self.fib[1] = 1


    def __del__(self):
        with open('fibfile', 'w') as f:
            for k,v in self.fib.iteritems():
                f.write('{0} {1}\n'.format(k, v))

    def calculate(self, n):
        global count
        count += 1
        try:
            return self.fib[n]
        except KeyError:
            retval =  self.calculate(n - 1) + self.calculate(n -2)
            self.fib[n] = retval
            return retval

if __name__ == '__main__':
    count = 0

    start_time = time()
    print fib(35)
    end_time = time()
    print end_time - start_time, 'seconds'
    print count

    f = FibGenerator()

    print

    count = 0
    start_time = time()
    print f.calculate(35)
    end_time = time()
    print end_time - start_time, 'seconds'
    print count
