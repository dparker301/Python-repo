# operator indicates that the for loop should check every element in the happy message string.
"""
for char in 'happy message':
    print(char)
    
"""

# Script to check if the user name is in the list, and print welcome if it is or your not invited
"""
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited!')
"""

# Same script just not invited
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')