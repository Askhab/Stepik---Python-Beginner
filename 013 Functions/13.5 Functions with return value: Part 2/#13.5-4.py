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


def get_next_prime(num):
    while not is_prime(num + 1):
        num += 1
    else:
        return num + 1


# reading inputs
n = int(input())

# function call
print(get_next_prime(n))
