# Function range()
# 1 - function range() with one parameter
for i in range(10):
    print('Hello', i)

# The value that we specify in brackets of the range() function indicates the number of iterations of the loop, while the variable i takes on the following values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# function range() with two parameters
range(1, 5)  # prints 1, 2, 3, 4 - right side is not inclusive

# iterate over numbers from 100 to 999
for i in range(100, 1000):
    if i % 10 == 7:  # prints those number that ends in 7
        print(i)

# function range() with three parameters
range(1, 10, 2)  # 1, 3, 5, 7, 9
range(5, 30, 5)  # 5, 10, 15, 20, 25

# third parameter in range() function remains - stepping

# Negative generation step
range(20, 16, -1)  # 20, 19, 18, 17
range(20, 10, -3)  # 20, 17, 14, 11

for i in range(5, 0, -1):
    print(i, end=' ')
print('We take of!!!')
# 5 4 3 2 1 We take of!!!
