#!/usr/bin/env python


import sys
import os.path
from os import remove
import argparse
import getpass
import inspect

from subprocess import call,Popen,PIPE


def is_close(a, b, epsilon=1e-6):
    return abs(a - b) < epsilon


# The grading harness.
class GradingHarness:
    def __init__(self):
        # Generate a list of derived class functions
        base_methods = [f for f in dir(GradingHarness) if callable(getattr(GradingHarness, f))]
        self.graders = sorted([f for f in dir(self)
                               if callable(getattr(self, f)) and
                               f not in base_methods])

    def set_cwd(self, cwd):
        self.cwd = cwd

    def run(self, command):
        p = Popen(command.split(), stdout=PIPE, cwd=self.cwd)
        output = p.communicate()

        return output[0]

    def grade(self):
        actual_grade = 0
        possible_grade = 0
        remaining_grade = 0

        for grader in self.graders:
            name,actual,possible = getattr(self, grader)()
            if actual == None:
                remaining_grade += possible
                print '  {0} needs to be graded by a TA ({1} possible)'.format(name, possible)
            else:
                actual_grade += actual
                possible_grade += possible
                print '  {0}: {1} out of {2}'.format(name, actual, possible)
        print '{0:0.2f}%, {1:0.2f} points out of {2:0.2f}'.format(100.0 * actual_grade / possible_grade, float(actual_grade) * self.total_points / possible_grade, self.total_points)

        if remaining_grade != 0:
            print '{0:.2f} still to be allocated by a TA'.format(remaining_grade)

        return actual_grade


# Set the utility path
def set_utility_path(number):
    # Set paths
    path = os.path.dirname(sys.argv[0]) + '/'
    sys.path.append(path + number)
    sys.path.append(path + number + '/.utility/')


# Run the grading scripts over a given lab.
def grade(number):
    set_utility_path(number)
    from utility import Grader

    print 'Grading', number
    g = Grader()
    g.set_cwd(number)
    g.grade()


# Create a tarball for a given lab.
def submit(number):
    set_utility_path(number)
    from utility import tar_arguments

    user = getpass.getuser()

    call(['ln', '-s', number, user])
    call(['tar', '-czf', '{1}-{2}.tgz'.format(base_dir, user, number)] + 
         ['{0}/{1}'.format(user, f) for f in tar_arguments()])
    call(['rm', user])

    #call(['tar', 'czf', 'foo.tgz'] + tar_arguments(), cwd=foo)

    print 'Tarball created:', '{0}-{1}.tgz'.format(user, number)


# Download the files for a given lab.
def create(number):
    filename = '{0}.tgz'.format(number)

    # Remove the file if it exists
    try:
        remove(filename)
    except OSError:
        pass

    # Get the new file, unpack it, and remove it
    call(['wget', 'http://web.engr.oregonstate.edu/~smartw/me499/assignments/{0}'.format(filename)])
    call(['tar', 'xzf', filename])
    remove(filename)


if __name__ == '__main__':
    # Absolute pathname of the directory where the script lives.
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Parse the command line arguments.
    parser = argparse.ArgumentParser(description='ME 499/599 utility script')
    parser.add_argument('action', choices=['grade', 'submit', 'create'])
    parser.add_argument('number', 
                        choices=['lab{0}'.format(i) for i in xrange(10)] +
                        ['hw{0}'.format(i) for i in xrange(1, 6)])

    args = parser.parse_args()

    # Since the functions have the same name as the arguments, we can
    # just look them up in the globals dictionary, and then call them
    # with the approptiate argument.
    globals()[args.action](args.number)
