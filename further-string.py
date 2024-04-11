
fav_band = 'Green Day'
print(fav_band[6])


print(fav_band[:6])

# Failed
#fav_band[6] = 'M'

# give you back a new string with uppercase or lowercase letters respectively.
text = 'please capitlise me'
text_cap = text.upper()
print(text_cap)



# True or fales to verify is numernic 
user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')
    
