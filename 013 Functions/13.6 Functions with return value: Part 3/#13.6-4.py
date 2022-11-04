from math import pi


# function declaration
def get_circle(radius):
    return 2 * pi * radius, pi * (radius ** 2)


# reading inputs
r = float(input())

# function call
length, square = get_circle(r)
print(length, square)
