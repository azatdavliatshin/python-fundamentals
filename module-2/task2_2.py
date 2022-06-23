# Task 2.2
#Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
#Examples:

# Input: 'Oh, it is python' 
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

def execute_task(): 
    print("Python program to count the number of characters (character frequency) in a string (ignore case of letters)\n")
    str = input("Enter a string:\n")
    print("Output is {}\n".format(calculate_characters_frequency(str)))

def calculate_characters_frequency(str):
    char_freq_map = {}
    str = str.lower()

    for char in str: 
        char_freq_map[char] = str.count(char)
    return char_freq_map

expected_result = {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
assert calculate_characters_frequency('Oh, it is python') == expected_result