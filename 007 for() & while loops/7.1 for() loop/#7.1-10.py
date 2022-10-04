m = int(input())
p = int(input())
n = int(input())

for i in range(n):
    print(i + 1, m)
    r = m * (p / 100)
    m = m + r
