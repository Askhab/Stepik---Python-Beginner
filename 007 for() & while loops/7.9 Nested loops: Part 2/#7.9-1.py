n = int(input())
count = 1

for i in range(n + 1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()
