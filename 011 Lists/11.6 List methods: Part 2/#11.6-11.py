s = input()
a = s.split()
a = [int(x) for x in a]

a.sort()
print(*a)
a.sort(reverse=True)
print(*a)
