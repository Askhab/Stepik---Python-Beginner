num = int(input())
check = 0
flag = True

while num != 0:
    last_num = num % 10
    if last_num >= check:
        flag = True
        num //= 10
    else:
        flag = False
        num = 0
    check = last_num

if flag:
    print("YES")
else:
    print("NO")
