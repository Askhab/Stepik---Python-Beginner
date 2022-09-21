# String data type
s1 = 'Python rocks!'
s2 = "Python rocks!"

s = input()  # variable is of the String data type

s1 = ''  # empty line
s2 = ' '  # a string consisting of a single space character

# Length of string - len() function
s1 = 'abcdef'
length1 = len(s1)
length2 = len('Python rocks!')
print(length1)  # 6
print(length2)  # 13


# Converting numbers into string - str() function
num1 = 1777
num2 = 17.77
s1 = str(num1)  # '1777'
s2 = str(num2)  # '17.77'

# String concatenation
s1 = 'ab' + 'bc'
s2 = 'bc' + 'ac'
s3 = s1 + s2 + '!!'
print(s1)  # abbc
print(s2)  # bcab
print(s3)  # abbcbcab!!

print('a', 'b', 'c', sep='*', end='!')
print()
print('a' + '*' + 'b' + '*' + 'c' + '!')

# Multiply string by a number
s = 'Hi' * 4
print(s)  # HiHiHiHi

print('-' * 75)  # ---------------------------------------------------------------------------

# Special operator - in
s = input()
if 'a' in s:
    print('Entered string contains character a')
else:
    print('The entered string does not contains character a')

# We can use in operator with logical operator - not
s = input()
if '.' not in s:
    print('Entered string does not contain the dot character')

