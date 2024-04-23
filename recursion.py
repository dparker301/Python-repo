# factorial
# 3! = 1 * 2 * 3 = 6
# 5% = 1 * 2 * 3* 4 * 5 = 120


#  a function that calculates the factorial for a given number.
# iterative
def get_factorial(number):
    factorial = 1   # first define factorial to be equal to one.
    for x in range(1, number + 1):      # use a for loop to iterate over all numbers from one to the given number and we multiply the
        factorial *= x  # factorial by all of these numbers.
    return factorial

# This approach to writing functions is often called iterative, because inside the function we use a for loop to iterate a sequence of numbers.    
print(get_factorial(6))  #


# recursion
def get_factorial_recursive(number):  # inside the function will return the number from the parameter multiplied by the return value of
    if number <= 1:  # same function for number minus one.
        return 1
    return number * get_factorial_recursive(number - 1)

get_factorial_recursive(6)