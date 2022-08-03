### Task 4.6
# Implement a function `get_longest_word(s: str) -> str` which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
# the string with a same length return the word that occures first.
# Example:
# ```python

# >>> get_longest_word('Python is simple and effective!')
# 'effective!'

# >>> get_longest_word('Any pythonista like namespaces a lot.')
# 'pythonista'
# ```

def get_longest_word(s):
    return sorted(s.split(" "), key=len, reverse=True)[0];

assert get_longest_word('Python is simple and effective!') == 'effective!'
assert get_longest_word('Any pythonista like namespaces a lot.') == 'pythonista'