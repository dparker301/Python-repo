
# we iterate over numbers from 1 to 3 with a control variable named I.
def get_number():
    for i in range(1, 4):  # the loop we use a new keyword yield.
        yield i   # Whenever you use the keyword yield instead of the keyword return, your function becomes a generator.
        

# The function returned a special kind of object for us. A generator. We can now ask the generator to provide us with values one by one, using a special instruction.
print(get_number())


generator = get_number()
print(next(generator))  # We use a special function named next with the generator variable as its argument.
print(next(generator))  # Now, whenever we use the print function, we get a new value one, two and three.
print(next(generator))
print(next(generator))


for x in get_number():
    print(x)
    

# generators is turn them into lists using the list function.
numbers = list(get_number())
print(numbers)