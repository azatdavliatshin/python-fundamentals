### Task 4.3
# Implement a function which works the same as `str.split` method (without using `str.split` itself, ofcourse).

def split(str, char):
    # find all index of char
    indexes = [i for i, ch in enumerate(str) if ch == char]
    result = []
    current_index = 0
    sub_string_acc = ""

    for i, ch in enumerate(str):
        if current_index < len(indexes) and i == indexes[current_index]:
            result.append(sub_string_acc)
            sub_string_acc = ""
            current_index += 1
            continue

        sub_string_acc += ch

    result.append(sub_string_acc)
    return result

assert split("1,2,3,4,5", ",") == "1,2,3,4,5".split(",")
assert split("1,2,3,4,5", "3") == "1,2,3,4,5".split("3")