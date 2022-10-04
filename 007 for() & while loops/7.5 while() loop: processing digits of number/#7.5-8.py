num = int(input())

while num > 9:
    if 10 <= num < 100:
        print(num % 10)
    num //= 10
