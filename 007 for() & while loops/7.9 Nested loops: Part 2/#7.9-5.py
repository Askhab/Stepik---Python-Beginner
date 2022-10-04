n = int(input())

while n > 9:
    last_digit = n % 10
    n = (n // 10) + last_digit
else:
    print(n)
