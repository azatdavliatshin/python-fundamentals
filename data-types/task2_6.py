# Task 2.6
# Write a Python program to print all unique values of all dictionaries in a list.

# Examples:

# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: ['S005', 'S002', 'S007', 'S001', 'S009']

import json


def execute_task():
    print("a Python program to print all unique values of all dictionaries in a list\n");
    input_list = json.loads(input("Provide list of dict-s\n"));
    print("Output is {}\n".format(get_unique_values(input_list)))

def get_unique_values(input_list):
    return sorted(set((value for dict in input_list for value in dict.values())))


assert get_unique_values([
    {"V":"S001"}, 
    {"V": "S002"}, 
    {"VI": "S001"}, 
    {"VI": "S005"}, 
    {"VII":"S005"}, 
    {"V":"S009"},
    {"VIII":"S007"}
]) == ['S001', 'S002', 'S005', 'S007', 'S009']