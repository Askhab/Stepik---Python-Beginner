number = int(input())
first = number // 100
middle = (number % 100) // 10
last = number % 10
print(first, middle, last)
print(first, last, middle)
print(middle, first, last)
print(middle, last, first)
print(last, first, middle)
print(last, middle, first)
