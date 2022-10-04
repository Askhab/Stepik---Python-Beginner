# Nested loops
# Consider a loop that partially models a digital clock. It shows seconds from 0 to 59
for seconds in range(60):
    print(seconds)

# You can add the minutes variable and nest the above loop inside another loop that repeats 60 times.
for minutes in range(60):
    for seconds in range(60):
        print(minutes, ':', seconds)

# In order to make the model complete, you can add one more variable to count the hours.
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)


# break & continue statements in nested loops
# Consider this code
for i in range(3):
    for j in range(3):
        print(i, j)

# Let's change the code by adding a conditional statement with a break statement to the nested loop
for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)

# Let's change the interrupt statement break to the continue statement
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)


# Using nested loops to solve equations

# Task 1. Find all pairs of natural numbers (and their number) that are the solution of the equation 12x+13y=777.

# Solution. Since by the condition the numbers xx and yy are natural, then x ≤ 64,y ≤ 59 . Let's write a program that goes through all possible pairs of numbers (x;y) and checks for them the condition 12x+13y=777

total = 0
for x in range(1, 65):
    for y in range(1, 60):
        if 12 * x + 13 * y == 777:
            total += 1
            print("x =", x, "y =", y)
print("Total number of natural solutions =", total)

# As a result of executing this code, we get
# x = 3 y = 57
# x = 16 y = 45
# x = 29 y = 33
# x = 42 y = 21
# x = 55 y = 9
# Total number of natural solutions = 5


# Task 2. Find all pairs of natural numbers (and their number) that are the solution of the equation x^2+y^2+z^2 = 2020

# Solution. Since by the condition the numbers x, y and z are natural, then x, y, z <= sqrt(2020) = 45. Let's write a program that iterates over all possible triples of numbers (x; y; z) and checks for them the condition x^2 + y^2 + z^2 = 2020.
total = 0
for x in range(1, 45):
    for y in range(1, 45):
        for z in range(1, 45):
            if x ** 2 + y ** 2 + z ** 2 == 2020:
                total += 1
                print("x =", x, "y =", y, "z =", z)
print("The total number of natural solutions =", total)

# As a result of executing this code, we get
# x = 18 y = 20 z = 36
# x = 18 y = 36 z = 20
# x = 20 y = 18 z = 36
# x = 20 y = 36 z = 18
# x = 36 y = 18 z = 20
# x = 36 y = 20 z = 18
# Total number of natural solutions = 6
