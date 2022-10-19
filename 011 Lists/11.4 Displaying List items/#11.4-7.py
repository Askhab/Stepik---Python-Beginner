n = int(input())
a = []
count = 0

for i in range(n):
    a.append(input())

k = int(input())
r = []

for q in range(k):
    r.append(input())

f = []

for i in a:
    count = 0
    for t in r:
        if t.lower() in i.lower():
            count += 1
        if count == len(r):
            f.append(i)

print(*f, sep="\n")
