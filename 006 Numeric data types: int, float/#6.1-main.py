# Numeric data types

# integer data type
# int - integer
n = 17  # integer data type
m = 7  # integer data type

# convert string into integer
# num = int(input())
# n = int('12345')

# Integer operators
a = 13
b = 7

total = a + b
diff = a - b
prod = a * b
div1 = a / b
div2 = a // b
mod = a % b
exp = a ** b

print(a, '+', b, '=', total)  # 13 + 7 = 20
print(a, '-', b, '=', diff)  # 13 - 7 = 6
print(a, '*', b, '=', prod)  # 13 * 7 = 91
print(a, '/', b, '=', div1)  # 13 / 7 = 1.8571428571428572
print(a, '//', b, '=', div2)  # 13 // 7 = 1
print(a, '%', b, '=', mod)  # 13 % 7 = 6
print(a, '**', b, '=', exp)  # 13 ** 7 = 62748517

# Long arithmetic
# A distinctive feature of the Python language is the unboundedness of the integer data type.
atom = 10 ** 80  # the number of atoms in the universe
print('Number of atoms =', atom)

# Delimiter character
num1 = 25_000_000
num2 = 25000000
print(num1)
print(num2)

# Floating point numbers
e = 2.71828  # floating point literal
pi = 3.1415  # floating point literal

# converting string to float
# num = float(input())
# n = float('1.2345')

# Float operators
a = 13.5
b = 2.0

total = a + b
diff = a - b
prod = a * b
div = a / b
exp = a ** b

print(a, '+', b, '=', total)  # 13.5 + 2.0 = 15.5
print(a, '-', b, '=', diff)  # 13.5 - 2.0 = 11.5
print(a, '*', b, '=', prod)  # 13.5 * 2.0 = 27.0
print(a, '/', b, '=', div)  # 13.5 / 2.0 = 6.75
print(a, '**', b, '=', exp)  # 13.5 ** 2.0 = 182.25


# Converting between int and float
# 1. Implicit conversion. Any integer (type int) can be used where a floating point number (type float) is expected,
#  since Python automatically converts integers to floats when necessary.

# 2. Explicit conversion. A floating point number cannot be implicitly converted to an integer. For such a conversion, you must use an explicit conversion using the int() command.

num1 = 17.89
num2 = -13.56
num3 = int(num1)
num4 = int(num2)
print(num3)
print(num4)
