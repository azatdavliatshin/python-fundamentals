# Task 2.5
# Write a Python program to sort a dictionary by key.

import json


def execute_task():
    print("a Python program to sort a dictionary by key\n")
    input_dict = json.loads(input("Provide stringified dictionary\n"))
    print("Output is {}\n".format({key: input_dict[key] for key in sorted(input_dict.keys())}))

def sort_dict_by_keys(input_dict):
    return {key: input_dict[key] for key in sorted(input_dict.keys())}

assert sort_dict_by_keys({"a":2, "c": 1, "b": 3}) == {"c": 1, "b": 3, "a": 2}