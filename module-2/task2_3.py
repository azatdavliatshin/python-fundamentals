# Task 2.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
# Examples:

# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white']

def execute_task():
    print("Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form\n")
    sequence = input("Provide comma seprated (without spaces) sequence of words:\n")
    print("Output is {}\n".format(normalize_list(sequence.split(","))))

def normalize_list(list, reverse=False):
    return sorted(set(list), reverse=reverse);

expected_result = ['black', 'green', 'red', 'white']
assert normalize_list(['red', 'white', 'black', 'red', 'green', 'black']) == expected_result

expected_result.reverse();
assert normalize_list(['red', 'white', 'black', 'red', 'green', 'black'], True) == expected_result

assert normalize_list([1,1,9,5,3,7,2,2,8,6,3,4,2]) == list(range(1, 10))

