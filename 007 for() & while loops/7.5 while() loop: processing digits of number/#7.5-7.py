num = int(input())
num_summary = 0
num_digits = 0
num_prod = 1
num_average = 0
num_last_digit = num % 10
num_first_digit = 0
num_sum_first_last_digits = 0

while num > 0:
    last_digit = num % 10
    num_summary += last_digit
    num_digits += 1
    num_prod *= last_digit
    num_first_digit = last_digit
    num //= 10

num_average = num_summary / num_digits
num_sum_first_last_digits = num_last_digit + num_first_digit

print(num_summary)
print(num_digits)
print(num_prod)
print(num_average)
print(num_first_digit)
print(num_sum_first_last_digits)
