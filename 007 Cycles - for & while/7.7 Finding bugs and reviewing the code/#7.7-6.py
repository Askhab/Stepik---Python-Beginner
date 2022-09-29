n = int(input())
max_digit = 0
count = 0

while n > 0:
    digit = n % 10
    if digit == 0 or digit % 3 == 0 and digit > max_digit:
        max_digit = digit
        count += 1
    n //= 10

if count == 0:
    print('NO')
else:
    print(max_digit)
