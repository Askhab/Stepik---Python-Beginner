# while() loop, processing the digits of a number
# Let's write a program that reads a natural number (a positive integer) and processes its digits.
n = int(input())
while n != 0:  # while there are digits in the number
    last_digit = n % 10  # get last digit
    # last digit processing code
    n = n // 10  # remove the last digit from the number

# Anything can be used as a processing procedure: outputting digits, finding a sum, multiplying digits, finding the largest or smallest digit, counting digits that satisfy a certain condition, etc.

# Let's write a program that determines if the number contains the number 7.

num = int(input())
has_seven = False  # signal label

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven:
    print('YES')
else:
    print('NO')
