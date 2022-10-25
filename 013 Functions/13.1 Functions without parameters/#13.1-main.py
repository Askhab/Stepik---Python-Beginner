# FUNCTIONS WITHOUT PARAMETERS
# Functions
# In previous lessons, we have used the built-in Python functions print(), input(), int(), str(), len(), and many others. It's time to start writing your own functions.

# At the very beginning of the course, you were asked to solve a problem in which you needed to draw a star rectangle with dimensions 5 \times 75×7 (55 rows and 77 columns).

# Our first version of the code looked something like this:
print('*******')
print('*******')
print('*******')
print('*******')
print('*******')

# Next, we learned the operator for multiplying a string by a number (the repetition operator) and would write the code:
print('*' * 7)
print('*' * 7)
print('*' * 7)
print('*' * 7)
print('*' * 7)

# And finally, we studied the cycles, after which the code would look like:
for _ in range(5):
    print('*' * 7)

# And now imagine that such rectangles need to be drawn not one, but several, say 3 pieces.

# Then the program code will look like:
for _ in range(5):
    print('*' * 7)

print()

for _ in range(5):
    print('*' * 7)

print()

for _ in range(5):
    print('*' * 7)


# And although the previous code completely solves the problem, it is not without flaws. Firstly, it is quite cumbersome due to the repetition of the part of the code responsible for drawing the rectangle. Secondly, if you need to change the dimensions of the rectangle, you will have to change them three times, in each part of the code that draws the rectangle.

# Instead of repeating the code to draw the rectangle, you can move it into a separate function and call it 3 times.
#
# To create a function, we write the following code:
def draw_box():
    for _ in range(5):
        print('*' * 7)


# When a function is created, to see the result of its work, you need to call it by name:
draw_box()

# Now, to draw 3 rectangles, you can write the code:
draw_box()
print()
draw_box()
print()
draw_box()


# The code has become shorter, more readable (due to the apt name of the function), and most importantly, if other rectangle sizes are required, it will be enough to change only the draw_box() function itself.


# FUNCTION NAMING
# Functions are named in exactly the same way as variables. The function name should be descriptive enough that anyone reading your code can guess what the function does.

# Python requires the same rules here as when naming variables:

# 1 - the function name uses only latin letters a-z, A-Z, numbers and the underscore character (_);

# 2 - a function name cannot start with a number;

# 3 - the name of the function, if possible, should reflect its purpose;

# 4 - upper and lower case characters are different.

# Remember: Python is a case sensitive language. For naming variables and functions, it is customary to use the lower_case_with_underscores style (lowercase words with underscores).

# Because functions perform actions, most programmers prefer to use verbs in function names. For example:

# 1 - a function that draws a rectangle can be called draw_box();
# 2 - the function that prints the check can be called print_check();
# 3 - a function that calculates wages before deductions can be called calculate_gross_pay().

# Each of these names gives a description of what the function does.


# FUNCTION DECLARATION
# So, a function is a separate, functionally independent part of a program that performs a specific task.

# Functions are declared using the def keyword (from the word define). The def keyword is followed by the name of the function, parentheses () , and a colon :.
# def function_name():
#     code block

# The first line of a function declaration is called the function header.

# The next line is a block of code - the body of the function. It is a set of instructions that make up one unit and are executed every time the function is called.

# Note that each line in the body of the function is indented.

# Python programmers typically use four spaces to indent lines of a block of code, in accordance with the PEP 8 standard.

# Consider a function declaration
def print_message():
    print("I'm - Arthur")
    print("king of the british")


# FUNCTION CALL
print_message()
