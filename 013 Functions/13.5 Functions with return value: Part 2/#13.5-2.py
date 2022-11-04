# function declaration
def is_valid_triangle(side1, side2, side3):
    if (side1 + side2) > side3 and (side2 + side3) > side1 and (side1 + side3) > side2:
        return True
    else:
        return False


# reading inputs
a, b, c = int(input()), int(input()), int(input())

# call of the function
print(is_valid_triangle(a, b, c))
