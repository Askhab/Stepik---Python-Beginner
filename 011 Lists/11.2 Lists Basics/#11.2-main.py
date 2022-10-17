# Lists Basics

# len() - Function
# The length of a list is the number of its elements. In order to calculate the length of a list, we use the built-in function len() (from the word length - length).

# numbers = [2, 4, 6, 8, 10]
# languages = ['Python', 'C#', 'C++', 'Java']

# print(len(numbers)) # print the length of the numbers list - 5
# print(len(languages)) # print the length of the languages list - 4

# print(len(['apple', 'banana', 'cherry'])) # print the length of a list of 3 elements - 3


# Membership operator - in
# numbers = [2, 4, 6, 8, 10]
#
# if 2 in numbers:
#     print("The numbers list contains number 2")
# else:
#     print("The numbers list doesn't contain number 2")


# Indexing
# When working with strings, we used indexing, that is, referring to a specific character of a string by its index. Similarly, lists can be indexed.

# To index lists in Python, square brackets [] are used, which indicate the index (number) of the desired element in the list:

# Let numbers = [2, 4, 6, 8, 10].

# numbers[0] - 2 - first element of the list
# numbers[1] - 4 - second element of the list
# numbers[2] - 6 - third element of the list
# numbers[3] - 8 - fourth element of the list
# numbers[4] - 10 - fifth element of the list

# Just like in strings, negative indexes are allowed for numbering from the end.

# numbers[-1] - 10 - fifth element of the list
# numbers[-2] - 8 - fourth element of the list
# numbers[-3] - 6 - third element of the list
# numbers[-4] - 4 - second element of the list
# numbers[-5] - 2 - first element of the list

# As with strings, an attempt to access a list element at a non-existent index:
# print(numbers[17])
# will throw an error:
# IndexError: index out of range
# Translated with Google (Russian → English)


# Slices
# Consider the list numbers = [2, 4, 6, 8, 10].

# With slicing, we can get multiple elements of a list by creating a colon-separated index range numbers[x:y].

# The following program code:
# print(numbers[1:3])   - [4, 6]
# print(numbers[2:5])   - [6, 8, 10]

# The numbers[:] slice returns a copy of the original list.


# Using slices to change elements in a given range
# Slicers can be used to modify an entire range of list items. For example, if we want to translate the names of fruits 'banana', 'cherry', 'kiwi' into Russian, then this can be done using a slice.

# fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
# fruits[2:5] = ['банан', 'вишня', 'киви']
# print(fruits)

# displays:
# ['apple', 'apricot', 'банан', 'вишня', 'киви', 'lemon', 'mango']


# The operation of concatenation + and multiplication by a number *
# print([1, 2, 3, 4] + [5, 6, 7, 8])   - [1, 2, 3, 4, 5, 6, 7, 8]
# print([7, 8] * 3)   - [7, 8, 7, 8, 7, 8]
# print([0] * 10)   - [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# For generating lists consisting of strictly repeating elements, multiplying by a number is the shortest and most correct method.


# Built-in functions sum(), min(), max()
# The built-in function sum() takes a list of numbers as a parameter and calculates the sum of its elements.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('Sum of all elements of the list =', sum(numbers))
# displays - Sum of all elements of the list = 55


# The built-in functions min() and max() take a list as a parameter and find the minimum and maximum elements, respectively.
# numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
# print('Minimum element =', min(numbers))
# print('Max element =', max(numbers))

# display:
# Minimum element = -7
# Max element = 3333


# Difference between lists and strings
# Despite all the similarities between lists and strings, there is one very important difference: strings are immutable objects, while lists are mutable.
# String
# s = 'abcdefg'
# s[1] = 'x' # trying to change character 2 (at index 1) of the string

# results in an error:
# object does not support item assignment

# List
# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers[1] = 101 # change element 2 (at index 1) of the list
# print(numbers)

# outputs:
# [1, 101, 3, 4, 5, 6, 7]
