number = int(input())
first = number // 1000
second = (number % 1000) // 100
third = (number % 100) // 10
last = number % 10

if first + last == second - third:
    print("Yes!")
else:
    print("No!")
