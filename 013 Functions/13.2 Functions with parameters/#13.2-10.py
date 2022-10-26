# function declaration
def print_digit_sum(num):
    summary = 0
    while num > 0:
        summary += num % 10
        num //= 10
    print(summary)


# reading input
n = int(input())

# function execution
print_digit_sum(n)
