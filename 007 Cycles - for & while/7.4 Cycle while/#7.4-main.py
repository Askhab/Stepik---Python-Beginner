# while() loop
# while(condition):
#     code block

# Let's see code that prints "Hello" ten times
i = 0
while i < 10:
    print('Hello')
    i += 1

# Let's write a program that reads numbers and prints their squares until -1 is entered
num = int(input())
while num != -1:
    print('The square of your number is:', num * num)
    num = int(input())

# for() loop vs while() loop
for i in range(101):
    print(i)

i = 0
while i < 101:
    print(i)
    i += 1

# Let's write a program that prints all numbers divisible by 3 using a for and while loop
for i in range(0, 100, 3):
    print(i)

i = 0
while i < 100:
    print(i)
    i += 3

# Reading data up to the stop value
text = input()
total = 0
while text != 'stop':
    num = int(text)
    total += num
    text = input()
print('Sum of numbers is:', total)

# Infinite loops
# An example of an infinite loop
# i = 0
# total = 0
# while i < 10:
#     total += i
