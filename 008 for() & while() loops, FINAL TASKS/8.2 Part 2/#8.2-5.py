n = int(input())

while not n < 1000:
    n //= 10
else:
    print(n % 10)
