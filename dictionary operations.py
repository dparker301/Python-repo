# Creating an empty dictionary
grades = {}

# Adding new elements to it
grades['John'] = 'A-'
grades['Anne'] = 'B'

print(grades)

# Updating the dictionary
grades['Anne'] = 'A'

print(grades)


grades.update({'John':'A'})
print(grades)
len(grades)

# To check if a given key is present in a dictionary, you can use the good old in operator.
if 'John' in grades:
    print('John got:', grades['John'])
    
# to delete a given key alongside its value, you can use the del operator.
del grades['John']
print(grades)

# if you use a simple for loop the same way as for lists, you will get access to the keys in the dictionary.
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

for el in grades:
    print(el)
    
# You will also achieve the very same result when you use the keys method on the dictionary.
for el in grades.keys():
    print(el)
    
# if you want to get access to the values instead and the values alone, you can use another method
for el in grades.values():
    print(el)
    
#  if you want to get access to both the keys and the values, you can use a third method named items.
for person, grade in grades.items():
    print(person, 'got', grade)