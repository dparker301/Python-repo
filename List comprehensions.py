
# Creating a variable with a list inside 
#numbers = [1, 2, 3, 4]  #  square brackets for numbers

# This is a lot of space this way
"""
numbers = []  # First we create a empty list
for i in range(1, 101):  # we added a for loop to the range 1 to 100
    numbers.append(i)  # appendeach number to the list
print(numbers)
"""

# Feature called List comprehension.
# We moved the square brackets into the list 
"""
numbers = [i for i in range(1, 101)]  # Controled value i into the loop
print(numbers)
"""

# The syntax is shorter. We added an if statment for the control variable after a space
numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)