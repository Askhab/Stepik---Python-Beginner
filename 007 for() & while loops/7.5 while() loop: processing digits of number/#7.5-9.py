num = int(input())
check = num % 10
flag = True

while num != 0:
    last_num = num % 10
    if last_num == check:
        flag = True
        num //= 10
    else:
        flag = False
        num = 0

if flag == True:
    print("YES")
else:
    print("NO")
