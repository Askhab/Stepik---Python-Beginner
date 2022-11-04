# function declaration
def solve(a, b, c):
    d = b ** 2 - 4 * a * c

    if d == 0:
        return (b * -1) / (2 * a), (b * -1) / (2 * a)
    elif d > 0:
        q1, q2 = (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
        return min(q1, q2), max(q1, q2)


# reading inputs
a, b, c = int(input()), int(input()), int(input())

# function call
x1, x2 = solve(a, b, c)
print(x1, x2)
