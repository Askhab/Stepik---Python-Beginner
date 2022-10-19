n = int(input())
a = []
negatives = []
zeros = []
positives = []

for y in range(n):
    a.append(int(input()))

for i in a:
    if i < 0:
        negatives.append(i)
    elif i == 0:
        zeros.append(i)
    elif i > 0:
        positives.append(i)

print(*negatives, sep="\n")
print(*zeros, sep="\n")
print(*positives, sep="\n")
