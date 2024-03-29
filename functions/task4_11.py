# ### Task 4.11
# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
# Dict values ​​should be summarized in case of identical keys

# ```python
# def combine_dicts(*args):
#     ...

# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}

# print(combine_dicts(dict_1, dict_2)
# >>> {'a': 300, 'b': 200, 'c': 300}


# print(combine_dicts(dict_1, dict_2, dict_3)
# >>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}
# ```

def combine_dicts(*dicts):
    result = {key: 0 for dict in dicts for key in dict}

    for dict in dicts:
        for key in dict.keys():
            result[key] = result[key] + dict[key]
    return result

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

assert combine_dicts(dict_1, dict_2) == {'a': 300, 'b': 200, 'c': 300}

assert combine_dicts(dict_1, dict_2, dict_3) == {'a': 600, 'b': 200, 'c': 300, 'd': 100}