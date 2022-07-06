# Task 2.7
# Write a Python program to convert a given tuple of positive integers into an integer. 

# Examples:

# Input: (1, 2, 3, 4)
# Output: 1234

from ast import literal_eval as make_tuple

def execute_task():
    print("a Python program to convert a given tuple of positive integers into an integer\n");
    input_tuple = make_tuple(input(("Enter tuple of positive integers\n")));
    print("Output is {}\n".format(stringify_tuple(input_tuple)));


def stringify_tuple(input_tuple):
    return int(''.join((str(digit) for digit in input_tuple)));

assert stringify_tuple((1,2,3,4)) == 1234