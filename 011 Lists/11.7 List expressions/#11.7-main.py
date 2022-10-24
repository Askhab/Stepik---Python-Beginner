# List expressions

# Creating lists
# To create a list of 1010 zeros we can use the following code:
zeros = []
for i in range(10):
    zeros.append(0)

# In Python, however, there is an easier and more compact way to create such a list. We can use the operator to multiply a list by a number:
zeros = [0] * 10

# To create lists populated according to more complex rules, we have to explicitly use a for loop.

# For example, to create a list of integers from 00 to 99, we have to write code like this:
numbers = []
for i in range(10):
    numbers.append(i)
# Such a code, although not complex, is rather cumbersome.


# Using List expressions
# Python has a mechanism for creating lists of non-repeating elements. This mechanism is called a (list comprehension).

# The previous code can be written as follows:
numbers = [i for i in range(10)]

# The general form of a list expression is as follows:
# [expression for variable in subsequence]
# where a variable is the name of some variable, a sequence is a sequence of values that it takes (a list, a string or an object obtained using the range function), an expression is some expression, as a rule, depending on the variable used in the list expression, which will fill the elements of the list .


# Examples of using list expressions
# 1. You can also create a list filled with 10 zeros using a list expression:
zeros = [0 for i in range(10)]

# 2. You can create a list filled with squares of integers from 0 to 9 like this:
squares = [i ** 2 for i in range(10)]

# 3. You can create a list filled with cubes of integers from 10 to 20 like this:
cubes = [i ** 3 for i in range(10, 21)]

# 4. Create a list filled with characters of the string:
chars = [c for c in "abcdefg"]
print(chars)


# Reading input
# When solving many problems from the previous lessons, we read the initial data (strings, numbers) and filled the list with them. Using list expressions, the process of populating a list can be significantly reduced.

# For example, if you first enter the number n - the number of lines, and then the lines themselves, then you can create a list like this:
n = int(input())
lines = [input() for _ in range(n)]
# You can omit the description of the variable n:
lines = [input() for _ in range(int(input()))]
# If you want to read a list of numbers, then you need to add a type conversion:
numbers = [int(input()) for _ in range(int(input()))]
# Note that we use the symbol _ as the name of the loop variable because it is not used.

# List expressions are often used to initialize lists. It's not customary in Python to create empty lists and then populate them with values if you can avoid it.


# Conditions in list expression
# You can use the conditional operator in list expressions. For example, if we want to create a list of even numbers from 0 to 20, then we can write the following code:
evens = [i for i in range(21) if i % 2 == 0]
# Important: in order to get a list consisting of even numbers, it is better to use the range(0, 21, 2) function. The previous example is provided to demonstrate the possibility of using conditions in list expressions.


# Nested loops
# You can use nested loops in a list expression.
numbers = [i * j for i in range(1, 5) for j in range(2)]
print(numbers)   # [0, 1, 0, 2, 0, 3, 0, 4]
# This code equal to next example:
numbers = []

for i in range(1, 5):
    for j in range(2):
        numbers.append(i * j)
print(numbers)


# Summarizing
# Let:
# word = 'Hello'
# numbers = [1, 14, 5, 9, 12]
# words = ['one', 'two', 'three', 'four', 'five', 'six']

# 1 - [0 for i in range(10)]   - [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 2 - [i ** 2 for i in range(1, 8)]    - [1, 4, 9, 16, 25, 36, 49]

# 3 - [i * 10 for i in numbers]   - [10, 140, 50, 90, 120]

# 4 - [c * 2 for c in word]   - ['HH', 'ee', 'll', 'll', 'oo']

# 5 - [m[0] for m in words]   - ['o', 't', 't', 'f', 'f', 's']

# 6 - [i for i in numbers if i < 10]   - [1, 5, 9]

# 7 - [m[0] for m in words if len(m) == 3]   - ['o', 't', 's']
