n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

smallest = min(a)
largest = max(a)

for s in a:
    if s == smallest or s == largest:
        continue
    else:
        print(s)
