#! usr/bin/env python

# Derek Bean
# ME599
# Lab 2

# Write two functions one recursive and one iterative,
# that reverse the order of a list


#Iterative list reverse function
def reverse_i(list_in):
        if type(list_in) != list or not(all(isinstance(i, (int, float)) for i in list_in)):
                print('The input variable was not a list of ints or floats.')
                return None
        reversed_list = []
        for i in range(len(list_in)):
                reversed_list.append(list_in[-(i+1)])
        return reversed_list


#Recursive list reverse function
def reverse_r(list_in):
        if type(list_in) != list or not(all(isinstance(i, (int, float)) for i in list_in)):
                print('The input variable was not a list of ints or floats.')
                return None
        reverse_list=[]
        if len(list_in) == 1:
                reverse_list += list_in
                return reverse_list
        else:
                reverse_list = [list_in[-1]] + reverse_r(list_in[:-1])
        return reverse_list
 

if __name__ == '__main__':
        correct_list = [1, 2, 3, 4, 5, 6]
        reversed_correct_list = correct_list[:]
        reversed_correct_list.reverse()
        if reverse_i(correct_list) == reversed_correct_list:
                print('The function reverse_i returned the correct value')
        else:
                print('The function reverse_i has returned an incorrect value')
                
        if reverse_r(correct_list) == reversed_correct_list:
                print('The function reverse_r has returned the correct value')
        else:
                print('The function reverse_r returned an incorrect value')
                
        incorrect_list = ['a', [1, 2], 3, (4, 5)]
        if reverse_i(incorrect_list) != None:
                print('The fuction reverse_i did not identify an incorrect input')
        else:
                print('reverse_i identified an incorrect input')
        if reverse_r(incorrect_list) != None:
                print('The fuction reverse_r did not identify an incorrect input')
        else:
                print('reverse_r identified an incorrect input')
