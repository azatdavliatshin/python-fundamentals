### Task 4.1
# Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa.

def replaceQuotes(str):
    result = "";
    for char in str:
        appendix = char
        if char == "\"":
            appendix = "\'"
        if char == "\'":
            appendix = '\"'
        result += appendix

    return result;

print(replaceQuotes("Hello, \"Space Invader\"! Welome to \'Moon\'"));
assert replaceQuotes("Hello, \"Space Invader\"! Welome to \'Moon\'") == "Hello, \'Space Invader\'! Welome to \"Moon\"";