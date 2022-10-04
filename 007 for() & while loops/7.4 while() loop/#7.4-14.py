num = int(input())
total = 0
while num > 0:
    if num // 25 != 0:
        total += num // 25
        num = num % 25
    elif num // 10 != 0:
        total += num // 10
        num = num % 10
    elif num // 5 != 0:
        total += num // 5
        num = num % 5
    elif num // 1 != 0:
        total += num // 1
        num = num % 1
print(total)
