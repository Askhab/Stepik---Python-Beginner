number = int(input())

if 1 <= number // 1000 <= 9 and (number % 7 == 0 or number % 17 == 0):
    print('YES')
else:
    print('NO')
