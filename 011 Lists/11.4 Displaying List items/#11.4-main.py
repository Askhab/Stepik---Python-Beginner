# Displaying List items

# Output with a for loop
# Option 1. If element indexes are needed:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numbers)):
    print(numbers[i])

# Option 2. If indexes are not needed:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num)

# If you want to print the list items on one line, separated by a space, then we can use the optional end parameter of the print() function:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num, end=' ')


# Output using list unpacking
# Python has a convenient way to print the elements of a list without using a for loop.

# Option 1. Displaying list items with a single space character:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(*numbers)   # 0 1 2 3 4 5 6 7 8 9 10

# Option 2. Displaying the elements of the list, each on a separate line
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(*numbers, sep='\n')
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# Since strings contain characters, just as lists contain elements, we can use string unpacking in the same way as list unpacking.
s = "Python"

print(*s)
print()
print(*s, sep="\n")

# P y t h o n

# P
# y
# t
# h
# o
# n
