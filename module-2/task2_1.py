#Task 2.1
# Write a Python program to calculate the length of a string without using the `len` function.

def execute_task():
    print("Python program to calculate the length of a string without using the `len` function\n");
    str = input("\nEnter string:\n")
    print("Output is {}\n".format(calculate_string_length(str)))

def calculate_string_length(str):
    counter = 0;
    for _ in str: counter+=1;
    return counter;

assert calculate_string_length("test") == 4
assert calculate_string_length("This is a long string") == 21

