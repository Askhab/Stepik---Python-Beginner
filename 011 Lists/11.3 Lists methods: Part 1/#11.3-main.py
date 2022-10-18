# Adding elements

# append() - Method
# To add a new element to the end of the list, use the append() method.
numbers = [1, 1, 2, 3, 5, 8, 13]

numbers.append(21)
numbers.append(34)

print(numbers)    # [1, 1, 2, 3, 5, 8, 13, 21, 34]


# extend() - Method
numbers = [0, 2, 4, 6, 8, 10]
odds = [1, 3, 5, 7]

numbers.extend(odds)
print(numbers)   # [0, 2, 4, 6, 8, 10, 1, 3, 5, 7]


# The difference between the append() and extend() methods comes into play when adding a string to a list.
words1 = ["iq option", "stepik", "beegeek"]
words2 = ["iq option", "stepik", "beegeek"]

words1.append("python")
words2.extend("python")

print(words1)   # ['iq option', 'stepik', 'beegeek', 'python']
print(words2)   # ['iq option', 'stepik', 'beegeek', 'p', 'y', 't', 'h', 'o', 'n']


# Removing elements
# Using the del operator, you can remove elements of a list at a specific index.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[5]

print(numbers)   # [1, 2, 3, 4, 5, 7, 8, 9]

# The del operator also works with slices: we can remove an entire range of list items
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[2:7]

print(numbers)   # [1, 2, 8, 9]

# We can remove all elements at even positions (0, 2, 4, ...) of the original list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]

print(numbers)   # [2, 4, 6, 8]
