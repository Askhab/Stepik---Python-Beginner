n = int(input())
max_num = 0
min_num = 0

while n != 0:
    last_digit = n % 10
    if last_digit > min_num and last_digit > max_num:
        max_num = last_digit
    elif last_digit < max_num and last_digit < min_num:
        min_num = last_digit
    n //= 10
print("The maximum digit is", max_num)
print("The minimum digit is", min_num)
