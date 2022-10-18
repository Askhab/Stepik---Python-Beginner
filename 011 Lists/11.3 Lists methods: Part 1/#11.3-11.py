n = int(input())
c = 0
a = []

for i in range(n):
    t = int(input())
    if c == 0:
        c += t
    else:
        c += t
        a.append(c)
        c = t
print(a)
