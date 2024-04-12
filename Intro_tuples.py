# Tuples are created with round brackets, and list are square brackets
empty_tuple = ()
one_el_tuple_a = (1,)  #comma needed so python know you are creating a tuple and not a single value
one_el_tuple_b = 1,


# The last comma is optional
three_el_tuple = 1, 2, 3,

# With or without the brackets in the statement the print command will present the brackets
print(three_el_tuple)


##### Mutability

user_data = ('John', 'American', 1964)

user_data = ('Katya', 'Russian', 1980)

# Tuples do not allow append. We deleted elements from lists with the Del instruction. This will not work with tuples either.
#user_data.append('teacher')

# Printing out the first name 
print(user_data[0])

message = 'welcome'

message = 'Welcome'

# W string object does not support item assignment.
message[0] = 'w'