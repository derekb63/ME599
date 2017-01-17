#!/usr/bin/env python


from volumes import cylinder_volume, torus_volume
from close import close
from words import letter_count

from me499 import GradingHarness,is_close

from math import pi
from random import uniform,random,choice
from string import ascii_letters


class Grader(GradingHarness):
    total_points = 10
    
    def t1_cylinder(self):
        tests = 1000
        points = 0

        for i in xrange(tests):
            r = uniform(0.1, 10.0)
            h = uniform(0.1, 10.0)
            try:
                if is_close(cylinder_volume(r, h), pi * r * r * h, 1e-10):
                    points += 1
            except:
                pass

        return ('Legal cylinder volumes', points, tests)

    def t2_cylinder_illegal(self):
        tests = 1000
        points = 0

        # Try 1000 possibly illegal values
        for i in xrange(tests):
            r = h = 10
            while r > 0 and h > 0:
                r = uniform(-10.0, 10.0)
                h = uniform(-10.0, 10.0)
            if cylinder_volume(r, h) == None:
                points += 1

        return ('Illegal cylinder volumes', points, tests)

    def t3_torus(self):
        tests = 1000
        points = 0

        for i in xrange(tests):
            r = uniform(0.1, 10.0)
            R = uniform(0.1, 10.0)
            try:
                if is_close(torus_volume(R, r), 2.0*pi**2*r**2*R, 1e-10):
                    points += 1
            except:
                pass

        return ('Legal torus volumes', points, tests)
        
    def t4_torus_illegal(self):
        tests = 1000
        points = 0

        # Try 1000 possibly illegal values
        for i in xrange(tests):
            r = h = 10
            while r > 0 and h > 0:
                r = uniform(-10.0, 10.0)
                R = uniform(-10.0, 10.0)
            if torus_volume(R, r) == None:
                points += 1

        return ('Illegal torus volumes', points, tests)

    def t5_close(self):
        tests = 1000
        points = 0

        for i in xrange(tests):
            epsilon = random()
            a = uniform(-1.0, 1.0)
            b = uniform(-1.0, 1.0)
            is_close = abs(a-b) <= epsilon

            if close(a, b, epsilon) == is_close:
                points += 1

        return ('Close', points, tests)

    def t6_letters(self):
        tests = 1000
        points = 0

        for i in xrange(tests):
            words = ''.join([choice(ascii_letters) for i in xrange(1000)])
            search = choice(ascii_letters)
            answer = len([ch for ch in words.lower() if ch == search.lower()])
            if letter_count(words, search) == answer:
                points += 1
                
        return ('Letter count', points, tests)

def tar_arguments():
    return ['volumes.py', 'close.py', 'words.py']

