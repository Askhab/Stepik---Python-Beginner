n = int(input())

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * 19)
    else:
        for j in range(1, 20):
            if j == 1 or j == 19:
                print("*", end="")
            else:
                print(" ", end="")
        print()
