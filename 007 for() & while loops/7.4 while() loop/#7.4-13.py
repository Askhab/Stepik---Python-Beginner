num = int(input())
total = 0
while not num < 0 and not num > 5:
    if num == 5:
        total += 1
    else:
        total += 0
    num = int(input())
print(total)
