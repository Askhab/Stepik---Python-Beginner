even_num = 0
odd_num = 0

for i in range(10):
    num = int(input())
    if num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
if odd_num > 0:
    print("NO")
else:
    print("YES")
