# Finding bugs and code review

# Version 1 of the program: We go through all the numbers from 2 to num - 1 and check the divisibility of the number num by i
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False

if num > 1 and flag:
    print("Prime number")
else:
    print("Not a prime number")

# If the program is given a prime number num = 1934234249 as input, then it will run for approximately 270 seconds = 4.5 minutes.

# Version 2 of the program: It is easy to understand that it makes no sense to sort through all the numbers from 2 to num - 1. It is enough to check numbers from 2 to num // 2 + 1.
num = int(input())
flag = True

for i in range(2, num // 2 + 1):
    if num % i == 0:
        flag = False

if num > 1 and flag:
    print("Prime number")
else:
    print("Not a prime number")
# If the program is given a prime number num = 1934234249 as input, then it will run for approximately 130130 seconds = 2.22.2 minutes. In fact, we have doubled the running time of the program!


# Version 3 of the program: The right bound of num // 2 + 1 checks can be improved by noting that any composite   number has a divisor (other than 1) that does not exceed the square root of the number. Thus, it makes sense to   iterate over divisors from 22 to sqrt(n + 1)
num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False

if num > 1 and flag == True:
    print("Prime number")
else:
    print("Composite number")
# If the program is given a prime number num = 1934234249 as input, then it will run for approximately 0.0660.066 seconds. In fact, we have improved the running time of the program by 4000 times!


# Version 4 of the program: Previous optimizations dealt with the case when the number being tested is prime. If the number is composite, and we have found its first divisor (other than 1), we break the loop with the break statement
num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
        break

if num > 1 and flag:
    print("Prime number")
else:
    print("Composite number")
