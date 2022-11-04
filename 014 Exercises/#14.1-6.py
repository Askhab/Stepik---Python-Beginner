from math import factorial


# function declaration
def compute_binom(n, k):
    n_fac = factorial(n)
    k_fac = factorial(k)
    min_fac = factorial(n - k)
    return int(n_fac / (k_fac * min_fac))


# reading inputs()
n = int(input())
k = int(input())

# function call
print(compute_binom(n, k))
