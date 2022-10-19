n = int(input())
a = []
aq = []

for i in range(n):
    a.append(int(input()))

for q in a:
    aq.append(q ** 2 + 2 * q + 1)

print(*a, sep="\n")
print()
print(*aq, sep="\n")
