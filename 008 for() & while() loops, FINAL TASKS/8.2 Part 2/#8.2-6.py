num = int(input())
three_count = 0
last_num_count = 0
odd_num_count = 0
bigger_than_5 = 0
bigger_than_7 = 1
zero_five_count = 0
last_num = num % 10

while num > 0:
    end_num = num % 10
    if end_num == 3:
        three_count += 1
    if end_num == last_num:
        last_num_count += 1
    if end_num % 2 == 0:
        odd_num_count += 1
    if end_num > 5:
        bigger_than_5 += end_num
    if end_num > 7:
        bigger_than_7 *= end_num
    if end_num == 5 or end_num == 0:
        zero_five_count += 1
    num //= 10
print(three_count)
print(last_num_count)
print(odd_num_count)
print(bigger_than_5)
print(bigger_than_7)
print(zero_five_count)
