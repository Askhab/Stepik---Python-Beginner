from math import factorial

n = int(input())
summary = 0

for i in range(1, n + 1):
    summary += factorial(i)
print(summary)
