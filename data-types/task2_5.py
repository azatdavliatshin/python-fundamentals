# Task 2.5
# Write a Python program to sort a dictionary by key.

import json


def execute_task():
    print("a Python program to sort a dictionary by key\n")
    input_dict = json.loads(input("Provide stringified dictionary\n"))
    print("Output is {}\n".format({key: input_dict[key] for key in sorted(input_dict.keys())}))