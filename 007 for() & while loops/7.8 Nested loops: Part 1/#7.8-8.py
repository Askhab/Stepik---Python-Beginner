from math import ceil, floor

num = int(input())
ceil_num = ceil(num / 2)
floor_num = floor(num / 2)
count = 1
check = 1

for i in range(num):
    if count < ceil_num and not check == ceil_num:
        for j in range(count):
            print("*", end="")
        count += 1
        check += 1
    else:
        for k in range(count):
            print("*", end="")
        count -= 1
    print()
