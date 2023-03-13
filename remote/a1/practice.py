import itertools

# Create a 2x2 table as a nested list
my_table = [["A", "B"], ["C", "D"]]

# Flatten the nested list using a list comprehension
my_list = [element for row in my_table for element in row]

# Alternatively, you can use the itertools.chain() function to flatten the nested list
my_list = list(itertools.chain.from_iterable(my_table))

# Print the resulting list
print(my_list)