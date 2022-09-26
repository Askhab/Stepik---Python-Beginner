n = int(input())
pre_largest_num = 0
largest_num = 0

for i in range(n):
    num = int(input())
    if num > pre_largest_num:
        pre_largest_num = num
        if pre_largest_num > largest_num:
            largest_num, pre_largest_num = pre_largest_num, largest_num
print(largest_num)
print(pre_largest_num)
