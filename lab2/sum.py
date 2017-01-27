#! usr/bin/env python

# Derek Bean
# ME 599
# 1/24/2017


# Find the sum of a list of numbers using a for loop
def sum_i(list_in):
        if type(list_in) != list or not(all(isinstance(i, (int, float))
                                        for i in list_in)):
                print('The input variable was not a list of ints or floats.')
                return None

        list_sum = 0
        for i in list_in:
                list_sum += i
        return list_sum


# Caclulate the sum of a list of numbers using recursion
def sum_r(list_in):
        if type(list_in) != list or not(all(isinstance(i, (int, float))
                                        for i in list_in)):
                print('The input variable was not a list of ints or floats.')
                return None

        list_sum = 0
        if len(list_in) == 1:
                list_sum = list_in[0]
                return list_sum
        else:
                list_sum = list_in[0] + sum_r(list_in[1:])
        return list_sum


if __name__ == '__main__':

        correct_list = [1, 2, 3, 4, 5, 6]
        if sum_i(correct_list) != sum(correct_list):
                print 'The function sum_i has returned an incorrent value'
        else:
                print 'sum_i returned the correct value'

        if sum_r(correct_list) != sum(correct_list):
                print 'The function sum_r has returned an incorrent value'
        else:
                print 'sum_r returned the correct value'

        incorrect_list = ['a', [1, 2], 3, (4, 5)]
        if sum_i(incorrect_list) is not None:
                print('The fuction sum_i did not identify an incorrect input')
        else:
                print('sum_i identified an incorrect input')
        if sum_r(incorrect_list) is not None:
                print('The fuction sum_r did not identify an incorrect input')
        else:
                print('sum_r identified an incorrect input')
