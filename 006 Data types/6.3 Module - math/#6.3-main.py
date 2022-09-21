# Module math
# for using it write - import math
# import math
#
# num1 = math.sqrt(2)  # calculating square root of two
# num2 = math.ceil(3.8)  # rounding up
# num3 = math.floor(3.8)  # rounding down
#
# print(num1)  # 1.4142135623730951
# print(num2)  # 4
# print(num3)  # 3

# if you want to import all math functions use - from math import *
# if you want to use only sqrt() & ceil() functions - use from math import sqrt, ceil

from math import sqrt, ceil

print(sqrt(25))
print(ceil(34.7))

# print(floor(12.8))  # will result an error because floor() function is not connected

# List of the most commonly used functions of the math module
# ROUNDS
# int() - rounds number towards zero

# round(x) - rounds x to the nearest integer. If the fractional part of the number is 0.5, then the number is rounded  up to the nearest even number

# round(x, n) - rounds a number x to n decimal places

# floor(x) - rounds x down

# ceil(x) - rounds x up

# abs(x) - Modulus of x (absolute value)

# ROOTS, LOGARITHMS, POWERS & FACTORIAL
# sqrt(x) - Square root of x

# pow(x, n) - Raising a number x to the power n

# log(x) - The natural logarithm of the number x. The base of the natural logarithm is equal to the number e

# log10(x) - Decimal logarithm of x. The base of the decimal logarithm is equal to the number 10

# log(x, b) - Logarithm of x to base b

# factorial(n) - Factorial of a natural number n

# TRIGONOMETRY
# degrees(x) Converts angle x given in radians to degrees

# radians(x) Converts angle x given in degrees to radians

# cos(x) Cosine of angle x given in radians

# sin(x) Sine of angle x, given in radians

# tan(x) Tangent of angle x given in radians

# acos(x) Returns the angle in radians from 00 to π whose cos is x

# asin(x) Returns the angle in radians from -π / 2 to π / 2, sin of which is equal to x

# atan(x) Returns the angle in radians from π / 2 to π / 2, whose tan is equal to x

# atan2(y, x) Polar angle (in radians) of the point with coordinates (x, y)

# CONSTANT
# pi - π = 3.141592653589793
# e - e = 2.718281828459045
