"""
numbers = [1, 2, 3, 4]

countries = ['UK', 'US', 'Germany']

# Mixing data type, and not recommended
countries = [1, 'UK', 2, 'US']

# This outer list named cells contains two elements inside. The first element is a list with three strings inside.
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

cells[0]

cells[0][0]
"""

# Added a for loop

cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)
    
    
# Here is nested for loops
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)
        
# Using nested list for tables
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print('Element:', cell)
        
# table with a list
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()
    

# list for comphension
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)