# Wich functions that are available
user_data = ('John', 'American', 1964)
print(len(user_data))


# If statement
user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes from the US!')
    
# For loop statement
user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)

# Tuples can also be added together or multiplied by an integer.
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)

# The elements are repeated ten times.
numbers = (0, 1) * 10
print(numbers)

# Each element in this list is a different name, but all the elements are strings and all of them represent
male_name = ['Adam', 'Jerry', 'Mark']

# Each element is a float that represents the temperature in a balloon on a different day.
berlin_temps = [13.0, 17.5, 12.0]

# The name and nationality are strings, while the airborne is an integer, but all three elements are
user_data = ('John', 'American', 1964)

# You can also see that tuples elements can be variables first and second are variables and not literals.
# And this way we are able to perform a swap operation in a single line.
first = 5
second = 7
first, second = second, first