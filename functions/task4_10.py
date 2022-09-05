# ### Task 4.10
# Implement a function that takes a number N as an argument and returns a dictionary, where the key is a n (n ∈ [1, N]) and the value is the square of n (n**2).
# ```python
# print(generate_squares(5))
# >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ```

def generate_squares(n):
    return {num: num ** 2 for num in range(1, n + 1)}

assert generate_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}