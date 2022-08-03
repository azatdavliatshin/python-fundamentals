### Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of
# any reversing functions is prohibited. To check your implementation you can use
# strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

def isStringPalindrome(str):
    i = 0
    j = len(str) - 1

    while (i < j):
        if str[i].lower() != str[j].lower():
            return False
        i += 1
        j -= 1
    return True;

assert isStringPalindrome("Test") == False
assert isStringPalindrome("racecar") == True
assert isStringPalindrome("radar") == True