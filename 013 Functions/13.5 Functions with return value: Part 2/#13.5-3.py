# function declaration
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


# reading inputs
n = int(input())

# function's call
print(is_prime(n))
