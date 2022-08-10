# ### Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:

# 1) characters that appear in all strings

# 2) characters that appear in at least one string

# 3) characters that appear at least in two strings

# 4) characters of alphabet, that were not used in any string

# Note: use `string.ascii_lowercase` for list of alphabet letters

# ```python
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*test_strings))
# >>> ('o',)
# print(test_1_2(*test_strings))
# >>> ('d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y',)
# print(test_1_3(*test_strings))
# >>> ('h', 'l', 'o',)
# print(test_1_4(*test_strings))
# >>> ('a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z',)

import string


def test_1_1(*strs):
    result = set()
    number_of_strings = len(strs)
    
    # characters that appear in all strings -> it's enough to go through only first string
    first_string = strs[0]
    other_strings = strs[slice(1, len(strs))]
    counter = 1
    for char in first_string:
        for os in other_strings:
            if char in os:
                counter += 1
            else:
                counter = 1
                break
        if counter == number_of_strings:
            result.add(char)
            counter = 1
    
    return sorted(result)
        

test_strings = ["hello", "world", "python", ]
assert test_1_1(*test_strings) == ['o']


def test_1_2(*strs):
    return sorted(list(set("".join(strs))))

assert test_1_2(*test_strings) == sorted(['d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'])

def test_1_3(*strs):
    result = set()
    
    # characters that appear in all strings -> it's enough to go through only first string
    first_string = strs[0]
    other_strings = strs[slice(1, len(strs))]
    counter = 1
    for char in first_string:
        for os in other_strings:
            if char in os:
                counter += 1
                break
        
        if counter == 2:
            result.add(char)
            counter = 1

    return sorted(result) 

assert test_1_3(*test_strings) == sorted(['h', 'l', 'o'])

def test_1_4(*strs):
    used_chars = test_1_2(*strs)
    return [char for char in string.ascii_lowercase if not char in used_chars]

assert test_1_4(*test_strings) == ['a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z']