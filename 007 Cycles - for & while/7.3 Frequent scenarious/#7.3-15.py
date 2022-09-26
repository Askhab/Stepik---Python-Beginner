n = int(input())
count = 1
fibo = 0

for i in range(n):
    bank = count
    if fibo == 0:
        print(count, end=" ")
        fibo += 1
    else:
        print(fibo, end=" ")
        count = fibo
        fibo = count + bank
