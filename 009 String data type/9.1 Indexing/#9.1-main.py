# Create a string. To create strings, we use double quotes '' or ""
# s1 = 'Python'
# s2 = 'Pascal'

# Reading a line. To read text data into a string variable, we use the input() function
# s = input()  # reading text
# num = int(input())  # reding text and converting it into integer

# Empty string. To create an empty string, we write s = '' or s = "". The empty string is analogous to the number 0.

# String length. To determine the length of a string (number of characters), we use the built-in len() function.
# s = "Hello"
# n = len(s)  # variable value is 5
# print(n)

# Concatenation and multiplication by a number. The + and * operators can be used on strings. The + operator concatenates two or more strings. This is called string concatenation. The * operator repeats a string a specified number of times.
# "AB" + "cd" - "ABcd"
# "A" + "7" + "B" - "A7B"
# "Hi" * 4 - "HiHiHiHi"

# Membership operator in. With the in operator, we can check if one string is within another. That is, whether one string is a substring of another
s = "All you need is love"
if 'love' in s:
    print('❤️')
else:
    print('💔')


# String indexing
# s = "Python"
# s[0] - "P"
# s[0] - "y"
# s[0] - "t"
# s[0] - "h"
# s[0] - "o"
# s[0] - "n"

# with negative indexes
# s[-6] - "P"
# s[-5] - "y"
# s[-4] - "t"
# s[-3] - "h"
# s[-2] - "o"
# s[-1] - "n"

#    0,  1,  2,  3,  4,  5
#    P,  y,  t,  h,  o,  n
#   -6, -5, -4, -3, -2, -1


# String iteration
# using for() loop - with indexes of symbols
s = "abcdef"
for i in range(len(s)):
    print(s[i])

# shorter version - without indexes of symbols
s = "abcdef"
for c in s:
    print(c)
