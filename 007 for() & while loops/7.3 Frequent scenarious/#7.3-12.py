n = int(input())
sum = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        sum += i
    elif i % 2 == 0:
        sum -= i
    elif i == n:
        sum += ((-1 ** (n + 1)) * n)
print(sum)
