# If you change one of the values, it will not affect the other one. 
"""
name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)
"""

# The same rule applies to other basic data types integers, floats, and booleans.  
# The same rule is not true for data collections like lists.
# This will not work but if you slice the code it will
"""
list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)
"""

# Slicing
"""
list_original = [1, 2, 3]
list_new = list_original[:]   # Adding slicing to the code
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)
"""

# Slicing with the first two elements
"""
list_original = [1, 2, 3]
list_new = list_original[:2]  # The two first elements from the list
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)
"""

#list_original = [1, 2, 3]
#list_new = list_original

list_original = [1, 2, 3]
list_new = list_original[:]