# break, continue & else

# Loop break statement

# Write a program to determine if a number is prime
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
        break

if flag:
    print("Prime number")
else:
    print("Not a prime number")

# Let's write a program that uses a for loop that reads 10 numbers and sums them up until it finds a negative number. In this case, the execution of the loop is interrupted by the break command.
result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break
    result += num
print(result)

# The loop interrupt operator break is convenient in conjunction with signal marks: when, after checking a certain condition, it makes no sense for us to continue executing the loop.
# Let's write a program that determines whether the number entered by the user contains the number 7.
num = int(input())
number = num
flag = False

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break
    num //= 10

if flag:
    print('Number', number, 'contains digit 7')
else:
    print('Number', number, 'does not contain digit 7')

# Infinite loops
# while True:
#    print('Python awesome!')
# result of this code is endless printing words - Python awesome


# Operator - continue
# Another standard looping idiom is to skip individual elements while iterating. The continue statement allows you to move to the next iteration of a for or while loop before all commands in the loop body have completed.
#
# Let's write a program that prints all the numbers from 1 to 100, except for the numbers 7, 17, 29 and 78.
for i in range(1, 101):
    if i == 7 or i == 17 or i == 29 or i == 78:
        continue
    print(i)


# Block else in loops
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop ended.')
# this code prints
# 4
# 3
# 2
# 1
# 0
# Loop ended.

# another example
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop ended.')
# this code prints
# 4
# 3
# 2

# Let's write a program that determines whether the number entered by the user contains the number 7. Instead of the program code written earlier
num = int(input())
n = num
flag = False

while n != 0:
    last = n % 10
    if last == 7:
        flag = True
        break
    n //= 10

if flag:
    print('Number', num, 'contains digit 7')
else:
    print('Number', num, 'does not contain 7')

# we can use
num = int(input())
n = num
while n != 0:
    last = n % 10
    if last == 7:
        print("Number", num, 'contains digit 7')
        break
    n //= 10
else:
    print('Number', num, 'does not contain digit 7')
