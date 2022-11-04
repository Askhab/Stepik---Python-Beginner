# function declaration
def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


# reading inputs
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# function call
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)
