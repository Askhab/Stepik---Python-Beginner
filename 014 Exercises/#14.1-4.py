# function declaration
def draw_triangle():
    for i in range(8):
        print(" " * (8 - 1 - i) + "*" * (1 + i * 2))


# main program
draw_triangle()  # function call
