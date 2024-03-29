### Task 4.5
# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
# of a given integer's digits.
#Example:
# ```python
# >>> split_by_index(87178291199)
#(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
# ```

def split_by_index(digit):
    return tuple([int(char) for char in str(digit)])


print(split_by_index(87178291199))
assert split_by_index(87178291199) == (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)