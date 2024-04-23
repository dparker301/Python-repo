
#  Need to find the average from multiple numbers in a list.
#input_numbers = [5.0, 3.5,7.8, 9.9, 10.0]


def get_average(input_numbers): # This line will turn the code into a function. Adding (input_numbers) this is a parameter

    sum = 0.0  # creating a temporary sum variable equal to zero.
    
    # creating loop for number in input numbers. Here we create a function with a single parameter, and the code of the function sums all numbers from the parameter.
    for number in input_numbers:  
    
        sum += number   # add the value of the number to the sum.
        
    average = sum / len(input_numbers)  # find the average, which is the sum divided by the number of elements in the list
    
    print(average)
    
get_average([5.0, 3.5, 7.8, 9.9, 10.0]) # this value, the list is assigned to the parameter input numbers and the function sums all the values. inside () is called an argument


# create a simple example of a function that takes two parameters.
def print_letter_count(text, letter):  # takes a string and a letter parameter
    counter = 0  # 
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
    
# we count the number of times the letter E appears in the string.
print_letter_count('Welcome', 'e')


# a sentence like this and we count how many times the letter A appears in the string,
print_letter_count('People say nothing is impossible, but I do nothing every day.', 'a')


print_letter_count(text='Welcome', letter='e')