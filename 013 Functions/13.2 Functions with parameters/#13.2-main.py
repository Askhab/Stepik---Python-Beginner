# FUNCTIONS WITH PARAMETERS
# In the previous tutorial, we defined the draw_box() function, which draws a star box with dimensions 5 times 7x7:
def draw_box():
    for i in range(5):
        print("*" * 7)


# It would be much more convenient if the draw_box() function would draw a rectangle with arbitrary sizes. Indeed, functions can accept input parameters, which makes them more flexible.

# Functions with parameters are declared in the same way as functions without parameters, only with parentheses:

# Let's rewrite the previous version of the draw_box() function so that it takes parameters that specify the height and width of the rectangle:
def draw_box(height, width):
    for i in range(height):
        print("*" * width)


draw_box(5, 7)
print()
draw_box(10, 15)
draw_box(3, 3)
print()
draw_box(3, 3)
print()
draw_box(3, 3)

# Instead of parameters, we can substitute not only integer constants, but also the values of variables. The following program code:
n = 3
m = 9
draw_box(n, m)


# MORE EXAMPLES
# Let's write a print_hello(n) function that takes one natural number nn and prints the word Hello exactly nn times.
def print_hello(n):
    print("Hello" * n)


print_hello(3)  # HelloHelloHello
print_hello(5)  # HelloHelloHelloHelloHello
times = 2
print_hello(times)  # HelloHello


# The print_hello() function can be made more flexible by passing one more parameter to it - the text for output:
def print_text(txt, n):
    print(txt * n)


print_text("Hello", 5)  # HelloHelloHelloHelloHello
print_text("A", 10)  # AAAAAAAAAA


# PARAMETERS VS ARGUMENTS
# An argument is any piece of data that is passed to a function when the function is called.
# A parameter is a variable that receives an argument passed to a function.

def draw_box(height, width):
    for i in range(height):
        print("*" * width)


# the parameters are the height and width variables.

# At the moment the draw_box(height, width) function is called:
height = 10
draw_box(height, 9)


# the arguments are height and 9.

# Function parameters are often called parametric variables.

# MAKING CHANGES TO SETTINGS
# When an argument is passed to a function, the function's parametric variable will refer to the value of that argument. However, any changes that are made to the parametric variable will not affect the argument.
def draw_box(height, width):
    height = 2
    width = 10
    for i in range(height):
        print("*" * width)


n = 5
m = 7
draw_box(n, m)
print(n, m)

# In the body of the function, changes are made to the values of the parametric variables height and width, but this did not affect the value of the variables n and m from the main program, which were passed as arguments to the draw_box() function.
