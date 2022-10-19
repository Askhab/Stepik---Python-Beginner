n = int(input())
a = []

for i in range(n):
    word = input()
    if word not in a:
        a.append(word)

print(*a, sep="\n")
