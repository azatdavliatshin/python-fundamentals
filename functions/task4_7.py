### Task 4.7
# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.
# Example:
# ```python
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]

# >>> foo([3, 2, 1])
# [2, 3, 6]
# ```

import math


def transformList(input_list):
    result = []
    for index, _ in enumerate(input_list):
        result.append(math.prod([digit for i, digit in enumerate(input_list) if i != index]))
    return result

assert transformList([1,2,3,4,5]) == [120, 60, 40, 30, 24]
assert transformList([3,2,1]) == [2,3,6]