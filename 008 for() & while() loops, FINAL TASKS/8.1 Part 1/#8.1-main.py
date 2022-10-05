# 1 What sequence of numbers will give you a function call range(6)
# 1 answer - 0, 1, 2, 3, 4, 5


# 2 What sequence of numbers will give you a call to the function range(2, 6)
# 2 answer - 2, 3, 4, 5


# 3 What sequence of numbers will give you a function call
# 3 answer - 0, 100, 200, 300, 400, 500


# 4 What sequence of numbers will give you a function call
# 4 answer - 10, 9, 8, 7, 6


# 5 Determine what the following code snippet will output?

# for i in range(10, 25):
#     print('Python awesome!')

# 5 answer - 15 times Python awesome! on every line


# 6 Determine what problem the following code snippet solves:

# n = int(input())
# counter = 0
#
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 7 != 0:
#         counter += 1
# print(counter)

# 6 answer -  prints the number of numbers from 1 to n that are multiples of 3 but not multiples of 7


# 7 Build program that calculating the sum of numbers from 11 to the entered natural number n.
# 7 answer -
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     total += i
# print(total)


# 8 What number should be written instead of the ellipsis so that the loop is executed exactly 7 times?
# i = ...
# while i <= 10:
#     print('Python!')
#     i += 1
# 8 answer - 4


# 9 Determine what problem the following code snippet solves:
# n = int(input())
# res = 1
# i = 2
#
# while i <= n:
#     res *= i
#     i += 1
# print(res)
# 9 answer - prints the factorial of the number n


# 10 Determine what problem the following code snippet solves:
# 10 answer -
# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# print(i)


# 11 Write a program that calculates the sum of the digits of a given natural number.
# 11 answer -
# n = int(input())
# total = 0
#
# while n != 0:
#     last_digit = n % 10
#     total += last_digit
#     n //= 10
# print(total)


# 12 Build a program that calculates the number of digits of an input natural number.
# NOTE. First increase the counter.
# 12 answer -
# n = int(input())
# counter = 0
#
# while n > 0:
#     counter += 1
#     n //= 10
# print(counter)
