# Task 2.4
# Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:

# Input: 60
# Output: [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]

def execute_task():
    print("Program that asks the user for a number and then prints out a list of all the divisors\n")
    num = int(input("Enter a number\n"))
    print("Output is {}\n".format(find_divisors(num)))

def find_divisors(num):
    divisors = [1]
    for digit in range(2, num):
        if num % digit == 0:
            divisors.append(digit)
    divisors.append(num)
    return divisors

assert find_divisors(60) == [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]