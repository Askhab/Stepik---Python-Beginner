# LOCAL AND GLOBAL VARIABLES

# LOCAL VARIABLES
# Local variables are variables declared inside a function and accessible only to the function itself. Program code outside the function does not have access to them.

# Consider the print_texas() function, which prints information about the number of birds living in Texas.
def print_texas():
    birds = 5000
    print('It lives in Texas', birds, 'birds.')


# In the body of the function, we create the birds variable, which is assigned a value of 5000. This variable is local to the print_texas() function. Whenever a value is assigned to a variable within a function, a local variable is created as a result. It belongs to the function in which it is created, and only the program code of this function can access it.

# If the program code of one function tries to access a local variable belonging to another function, an error will occur.
#
# Consider the following program code:
#
def print_texas():
    birds = 5000
    print('It lives in Texas', birds, 'birds.')


def print_california():
    print('California lives', birds, 'birds.')


# The print_california() function accesses the birds local variable of the print_texas() function. Calling the print_california() function results in an error:

# NameError: name 'birds' is not defined

# Local variables are hidden from other functions, so other functions can have their own local variables with the same name. For example,

def print_texas():
    birds = 5000
    print('It lives in Texas', birds, 'birds.')


def print_california():
    birds = 9000
    print('California lives', birds, 'birds.')


# Each of these two functions has a local variable called birds. But they are never visible at the same time, as they are in different functions.

# When the print_texas() function is executed, the birds variable is visible, whose value is 5000. When the print_california() function is executed, the birds variable is visible, whose value is 9000.


# VARIABLE SCOPE
# The scope of a variable is the part of the program in which it can be accessed, the function where it was created. A variable is visible only to code within its scope. No statement outside the function can access such a variable.

# A local variable cannot be accessed by code that appears inside a function before the variable has been created.

# For example, if you swap the lines of code in the print_texas() function:
def print_texas():
    print('It lives in Texas', birds, 'birds.')
    birds = 5000


# then when calling this function we get an error:
# UnboundLocalError: local variable 'birds' referenced before assignment

# The error occurred as a result of a premature access to the yet undeclared local variable birds.


# SCOPE OF PARAMETRIC VARIABLE
# The scope of a parametric variable is the function in which this parameter is used. The entire program code of this function has access to the parametric variable.

# Consider the function we already know:
def draw_box(height, width):
    for i in range(height):
        print('*' * width)


# Parametric variables here are height, width. Inside the function, one local variable i is declared.


# GLOBAL VARIABLES
# Global variables are variables declared in the main program and available both to the program and to all its functions.

# Consider the following program code:
birds = 5000  # global variable


def print_texas():
    print('It lives in Texas', birds, 'birds.')


def print_california():
    print('California lives', birds, 'birds.')


# At the very beginning of the program, we create a global variable birds, the value of which is equal to 5000. Next, we describe two functions that access the global variable. The result of executing the following code:

print_texas()
print_california()

# will be:
# There are 5,000 birds in Texas.
# There are 5,000 birds in California.

# A function can use any global variables except those with the same names as its local variables. If a local variable with the same name as one of the globals is declared in a function, then this global variable becomes inaccessible in this function, and when specifying the variable identifier, the local variable of the function will be referred to, and not the global variable of the same name.

# Consider the following program code:

birds = 5000  # global variable


def print_texas():
    birds = 1000  # local variable
    print('It lives in Texas', birds, 'birds.')


def print_california():
    birds = 7000  # local variable
    print('California lives', birds, 'birds.')


# At the very beginning of the program, we create a global variable birds, whose value is 5000. Next, we describe two functions that create local variables with the same name birds. Thus, when accessing the birds variable inside functions, the local variable will be accessed.

# The result of executing the following code:
print_texas()
print_california()


# will be:
# There are 1000 birds in Texas.
# There are 7,000 birds in California.


# GLOBAL VARIABLES ARE EVIL
# Most programmers agree that global variables should be limited or not used at all. The reasons are as follows.

# Global variables make it difficult to debug a program. The value of a global variable can be changed by any instruction in the program file. If you find that a global variable is holding a bad value, you'll have to look up all the instructions that access it to determine where the bad value is coming from. In a program with thousands of lines of code, this is not easy to do.
# Functions that use global variables usually depend on those variables. If you need to use such a function in another program, you will most likely need to redesign this function so that it does not rely on a global variable.
# Global variables make the program difficult to understand. A global variable can be modified by any instruction in the program. If you need to understand some part of the program that uses a global variable, you will have to learn about all other parts of the program that access this global variable.


# GLOBAL CONSTANTS
# Although you should avoid using global variables, you can use global constants in your program. A global constant is a global name that refers to an immutable value. Because the value of a global constant cannot be changed at runtime, you don't have to worry about the potential dangers usually associated with using global variables.

# Although Python does not allow you to create true global constants, you can simulate them using global variables. If a global variable is not declared using the global keyword within a function, then the value assigned to it cannot be changed within that function.


# global - KEYWORD
# If you want an instruction within a function to assign a value to a global variable, then an extra step is required. In this case, the global variable must be declared within the function.

# Consider the following program code:
def print_texas():
    global birds
    birds = 5000
    print('It lives in Texas', birds, 'birds.')


def print_california():
    print('California lives', birds, 'birds.')


print_texas()
print_california()

# The result of executing the following code:
#
print_texas()
print_california()

# will be:
# There are 5,000 birds in Texas.
# There are 5,000 birds in California.
