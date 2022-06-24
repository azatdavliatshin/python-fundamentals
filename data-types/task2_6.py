# Task 2.6
# Write a Python program to print all unique values of all dictionaries in a list.

# Examples:

# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: ['S005', 'S002', 'S007', 'S001', 'S009']

import json


def execute_task():
    print("a Python program to print all unique values of all dictionaries in a list\n");
    list = json.loads(input("Provide list of dict-s\n"));
    print("Output is {}\n".format(get_all_unique_values(list)))

def get_all_unique_values(input_list):
    result = set();
    for dict in input_list:
        for value in dict.values(): result.add(value);
    return sorted(result);

expected_result = ["S001", "S002", "S005", "S007", "S009"];
assert get_all_unique_values([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == expected_result;