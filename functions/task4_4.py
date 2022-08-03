### Task 4.4
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.
# Examples:
# ```python
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]

# >>> split_by_index("no luck", [42])
# ["no luck"]
# ```

def split_by_index(s, indexes):
    result = []
    substring_acc = ""
    current_index = 0

    for i, char in enumerate(s):
        if current_index < len(indexes) and i == indexes[current_index]:
            result.append(substring_acc)
            substring_acc = ""
            current_index += 1
        
        substring_acc += char
        
    result.append(substring_acc);
    
    return result


assert split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]) == ["python", "is", "cool", ",", "isn't", "it?"]
assert split_by_index("no luck", [42]) == ["no luck"]