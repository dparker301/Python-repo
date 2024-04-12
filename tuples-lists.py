# Three separate variables with three separate cities, so it perhaps makes sense to have them in a single list
city_1 = ('London', 'UK', 8.98)

city_2 = ('Canberra', 'Australia', 0.4)

city_3 = ('Algiers', 'Algeria', 3.9)

capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9)]


# we can use a for loop for capital in capitals.print name and then capital zero, the first element in the tuple.
# Then after a comma country and then Capital One and then finally after a comma, population and capital two.

for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])
    
    
    
# Keep track of weight. A list inside a tuple
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])

# You can add append to add more elements
user_data[3].append(79.6)

print(user_data)