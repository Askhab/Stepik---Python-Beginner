a = int(input())
b = int(input())
max_num = 0
total = 0
for i in range(a, b + 1):
    check_total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            check_total += j
        if check_total >= total:
            total = check_total
            max_num = i
print(max_num, total)
