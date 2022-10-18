n = int(input())
a = []
s = ""

for i in range(n):
    a.append(input())

k = int(input())

for i in range(len(a)):
    if len(a[i]) < k:
        continue
    else:
        s += a[i][k - 1]

print(s)
