num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
res1 = 0
res2 = 0
if num1 > num2:
    res1 = num2
else:
    res1 = num1
if num3 > num4:
    res2 = num4
else:
    res2 = num3
if res1 > res2:
    print(res2)
else:
    print(res1)
