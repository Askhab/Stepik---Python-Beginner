a = int(input())
b = int(input())

for i in range(a, b + 1):
    check = 0
    if i == 1:
        continue
    for j in range(i, 0, -1):
        if i % j == 0:
            check += 1
    if check > 2:
        continue
    else:
        print(i)
