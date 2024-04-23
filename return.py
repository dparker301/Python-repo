# 
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average #change our last instruction, which was printing the average to the following return Note the syntax. We don't use brackets around the keyword return because return is not a function.
    

# We can also save the return value in a variable and then later use it in our code somehow. 
print('The average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))

# The keyword return actually does two things at the same time. It gives the result as you could see, but it also immediately exits the function. This means that any instruction after the return statement will be ignored.
average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')
    
    
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me!')

get_average([2])


def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
        
