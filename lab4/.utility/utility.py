#!/usr/bin/env python


from me499 import GradingHarness,is_close
from sort import is_sorted,bubblesort,quicksort

try:
    from sort import insertion_sort
except:
    pass

try:
    from sort import mergesort
except:
    pass

from random import random,randint


class Grader(GradingHarness):
    total_points = 7

    def q1_bubblesort(self):
        tests = 1000
        points = 0

        for i in xrange(tests):
            l = [random() for i in xrange(randint(20, 50))]
            if sorted(l) == bubblesort(l):
                points += 1
        return ('bubblesort', points, tests)

    def q2_is_sorted(self):
        tests = 1000
        points = 0

        for i in xrange(tests / 2):
            l = [random() for i in xrange(randint(20, 50))]
            if not is_sorted(l):
                points += 1
            elif sorted(l) == l:
                points += 1
            if is_sorted(sorted(l)):
                points += 1

        return ('is_sorted', points, tests)

    def q3_quicksort(self):
        tests = 1500
        points = 0

        for i in xrange(tests):
            l = [random() for i in xrange(randint(20, 50))]
            if sorted(l) == bubblesort(l):
                points += 1
        return ('quicksort', points, tests)

    def q4_insertion_sort(self):
        try:
            tests = 1000
            points = 0

            for i in xrange(tests):
                l = [random() for i in xrange(randint(20, 50))]
                if sorted(l) == insertion_sort(l):
                    points += 1
            self.total_points += 2
            return ('insertion_sort', points, tests)
        except:
            return('No insertion sort found', 0, 0)

    def q5_merge_sort(self):
        try:
            tests = 1000
            points = 0

            for i in xrange(tests):
                l = [random() for i in xrange(randint(20, 50))]
                if sorted(l) == mergesort(l):
                    points += 1
            self.total_points += 2
            return ('mergesort', points, tests)
        except:
            return ('No mergesort found', 0, 0)

    def q6_graph(self):
        return ('Graphs', None, 3)

def tar_arguments():
    return ['sort.py', 'graph.py']

