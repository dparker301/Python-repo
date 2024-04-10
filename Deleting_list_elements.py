# Deleting list; will delete the second element. Will result with all the elements just removed Singapore
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[2]
print(top_cities)

# Keeping the first three elements in the list and deleting the remainder. Will result with element 0,1,2
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[3:]   ## Delete Top cities starting at index three onwards and print the list afterwards.
print(top_cities)

# delete all elements from a list using a slice with both indices omitted. Will result in a empty list
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[:]
print(top_cities)

# Del is not a funtion its a call to an instruction. The print invocation here throws an error because after we delete the list, the variable is no longer
# available. Need to be followed by brackets to be a function. 
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities
print(top_cities)