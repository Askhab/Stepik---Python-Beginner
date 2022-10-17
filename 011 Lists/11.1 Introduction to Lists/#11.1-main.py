# Intro to Lists
# Lists
# A list is a sequence of elements, numbered from 0, like the characters in a string.

# List creation
# To create a list, you need to list its elements separated by commas in square brackets:
# numbers = [2, 4, 6, 8, 10]
# numbers[0] == 2;
# numbers[1] == 4;
# numbers[2] == 6;
# numbers[3] == 8;
# numbers[4] == 10.

# languages = ["Python", "C#", "C++", "Java"]
# languages[0] == 'Python';
# languages[1] == 'C#';
# languages[2] == 'C++';
# languages[3] == 'Java'.

# Empty List
# There are two ways to create an empty list:
# Use empty square brackets [];
# Use the built-in function called list.
# The following two lines of code create an empty list:
# myList = []
# myList = list()


# The list built-in function
# Python has a built-in list() function that, in addition to creating an empty list, can convert certain types of objects to lists.

# For example, we know that the range() function creates a sequence of integers within a given range. To convert this sequence into a list, we write the following code:
# numbers = list(range(5))

# When this code is executed, the following happens:
# 1 - The range() function is called, passing the number 5 as an argument;
# 2 - This function returns the sequence of numbers 0, 1, 2, 3, 4;
# 3 - The sequence of numbers 0, 1, 2, 3, 4 is passed as an argument to the list() function;
# 4 - The list() function returns the list [0, 1, 2, 3, 4];
# 5 - The list [0, 1, 2, 3, 4] is assigned to the numbers variable.

# Here is another example:
# even_numbers = list(range(0, 10, 2))  # the list contains even numbers 0, 2, 4, 6, 8
# odd_numbers = list(range(1, 10, 2))   # the list contains odd numbers 1, 3, 5, 7, 9

# Similarly, with the list() function, we can create a list from the characters of a string. To convert a string to a list, we write the following code:
# s = 'abcde'
# chars = list(s) # list contains characters 'a', 'b', 'c', 'd', 'e'

# When this code is executed, the following happens:
# 1 - The list() function is called, passing the string 'abcde' as an argument;
# 2 - The list() function returns the list ['a', 'b', 'c', 'd', 'e'];
# 3 - The list ['a', 'b', 'c', 'd', 'e'] is assigned to the chars variable.


