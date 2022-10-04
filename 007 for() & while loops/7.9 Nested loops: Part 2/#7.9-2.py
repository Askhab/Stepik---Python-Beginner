n = int(input())

for i in range(n + 1):
    for j in range(i):
        print(j + 1, end="")
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()
