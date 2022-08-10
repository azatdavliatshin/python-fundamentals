### Task 4.8
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.
# Example:
# ```python
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]

# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

# >>> get_pairs([1])
# None
# ```

def get_pairs(lst):
    if len(lst) == 1 or len(lst) == 0:
        return None
    else:
        result = []
        for i, element in enumerate(lst):
            if i != len(lst) - 1:
                result.append((element, lst[i+1]))
        return result

assert get_pairs([1]) == None
assert get_pairs(['need', 'to', 'sleep', 'more']) == [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]