# Frequent scenarios
# counting the number
# Let's write a program that reads 10 numbers and determines how many of them are greater than 10.
# The key to counting is using a counter variable.
counter = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1
print('Was introduced', counter, 'numbers greater than 10.')

# let's count a number of introduced zeros
counter1 = 0
counter2 = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1
print('Was introduced', counter1, 'numbers greater than 10.')
print('Was introduced', counter2, 'zeros.')

# Example of count the number of numbers from the range 1 to 100 whose square ends in 4.
counter = 0
for i in range(1, 101):
    if i ** 2 % 10 == 4:
        counter = counter + 1
print(counter)

# Sum & product calculation
# Let's write a program that reads 10 numbers and determines the sum of those numbers that are greater than 10.
total = 0
for i in range(10):
    num = int(input())
    if num > 10:
        total = total + num
print('Sum of numbers greater than 10 is', total)

# Let's write a program that calculates the sum of natural numbers from 1 to 100:
total = 0
for i in range(1, 101):
    total = total + i
print('Sum is', total)

# write a program that asks for 10 integers and finds their average value
total = 0
for i in range(10):
    num = int(input())
    total = total + num
average = total / 10
print('The mean value is', average)

# Swapping variable values
# first we write
x = 3
y = 5
temp = x
x = y
y = temp
# OR we may write
x, y = y, x
# and in result will have swap x & y variables values

# Signal labels
# Let's write a program that determines that a natural number is prime.
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False

if num == 1:
    print('This is a unit, it is not simple and not composite')
elif flag:
    print('Prime number')
else:
    print('Composite number')

# Maximum & minimum
largest = -1
for i in range(10):
    num = int(input())
    if num > largest:
        largest = num
print('Largest number is', largest)

# another approach
largest = int(input())
for i in range(9):
    num = int(input())
    if num > largest:
        largest = num
print('Largest number is', largest)

# Extended assignment operators
# simple example of assignment
counter = counter + num
counter = counter + 1

# extended assignment operators
counter += num
counter += 1
