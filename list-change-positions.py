# This will not work when swapping variables
"""
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first = second
second = first
print('After swapping:', first, second)
"""

# This will work when swapping variables but is the extended way
"""
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
temporary = first  # Added a temp variable 
first = second
second = temporary # Added a temp variable 
print('After swapping:', first, second)
"""

# using a temp line to swap the variables
"""
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)
"""

# Swaping cities 
"""
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)
"""

# Sorted cites by alaph
"""
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)
"""

# random numbers sorted from lowest to highest
"""
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)
"""

# Sort number greatest to the lowest
"""
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)
"""

# The difference between sort and sorted....
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)


