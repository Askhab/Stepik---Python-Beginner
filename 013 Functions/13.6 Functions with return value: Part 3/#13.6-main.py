# FUNCTIONS WITH MULTIPLE RETURNING VALUES
# In Python, functions are not limited to returning just one value. After the return statement, you can define many comma-separated expressions:

# return expression 1, expression 2, expression 3 ...

# The following code defines a get_powers(num) function that takes num as an argument and returns its square, cube, and fourth power.

def get_powers(num):
    return num ** 2, num ** 3, num ** 4


# The result of executing the following code:

a, b, c = get_powers(2)
print(a)  # 4
print(b)  # 8
print(c)  # 16


# Let's consider one more example. Let it be required to write a function that finds the intersection point of two non-parallel lines ax+by=eax+by=e and cx+dy = fcx+dy=f.

# The program code that solves the problem looks like this:
def solve(a, b, c, d, e, f):
    x = (d * e - b * f) / (a * d - b * c)
    y = (a * f - c * e) / (a * d - b * c)
    return x, y


# Next code:
xsol, ysol = solve(2, 3, 4, 1, 2, 5)
print("The solution of the system is numbers", "x =", xsol, "y =", ysol)   # The solution of the system is numbers x = 1.3 y = -0.2


# BENEFITS OF USING FUNCTION
# Breaking the programs into functions, we get:

# MORE SIMPLE CODE. The program code broken down into functions is simpler and easier to understand. Several small functions are much easier to read than one long sequence of instructions;
# CODE REUSE. Functions allow you to avoid repeated repetition of code in the program. If some operation in the program is performed in several places, then you can write a function for it once and then execute it when necessary.
# EASIER TESTING. When each task in a program is contained within its own function, programmers can individually test each function to determine if it performs its task correctly.
# FASTER DEVELOPMENT. Suppose a programmer or a team of programmers is developing many programs. They detect common tasks in different programs, such as finding out the username and password, displaying the current time. It doesn't make sense to write code for these tasks every time. For frequently encountered tasks, functions are written and included in any program that needs them.
# SIMPLIFY TEAMWORK. When a program is developed as a set of functions, different programmers can be assigned to write individual functions.

# WHAT TO HIGHLIGHT IN FUNCTIONS
# Any completed fragment of the program can be allocated to a function. You can refer to the recommendations:

# * When you write the same sequence of commands in a program several times, the need to introduce a function becomes an acute internal need;
# * Sometimes the abundance of trifles overshadows the main thing and it is useful to remove the details that hide the meaning of the main program into the function;
# * It is useful to break a long program into its component parts, as a book is broken into chapters, while the main program becomes like a table of contents;
# * It can be useful to debug complex private algorithms separately in small testing programs. It will be easy to include them in the main program if they are designed as functions. For example, sorting functions;
# * What is done well in one program, I want to transfer it to new ones. For reuse, it is better to immediately separate useful algorithms into separate functions in the program, and collect functions into packages.
