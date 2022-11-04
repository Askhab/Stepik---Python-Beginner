# FUNCTIONS WITH RETURN VALUE: PART 2

# RETURNING BOOLEAN VALUES
# Python allows you to write boolean functions that return either true (True) or false (False). A boolean function can be used to test a condition, then the True and False values will signal that it is true.

# Boolean functions are widely used to simplify complex conditions tested in decision structures and repetitive structures.
# For example, let's write a program that asks the user to enter a number and determines whether it is even or odd.

# This can be done like this:
number = int(input())
if number % 2 == 0:
    print('This number is even. ')
else:
    print('This number is odd.')


# This piece of code will be easier to understand if you write a boolean function is_even() that takes a number as an argument and returns True if it is even and False if it is odd.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# Now we can rewrite the if-else statement of the main program so that it calls the is_even() function to determine if the variable number is even:
number = int(input())

if is_even(number):
    print('This number is even. ')
else:
    print('This number is odd.')

# This makes the logic of the program easier to understand, and the function can be called in the program whenever it is necessary to check the evenness of a number.


# USING BOOLEAN FUNCTIONS TO VALIDATE INPUTS
# Boolean functions can also be used to simplify complex input validation code. For example, in a program that prompts the user to enter a product model number, where the only possible values are 100, 200, and 300, we can write code like this:
model = int(input())

while model != 100 and model != 200 and model != 300:
    print('Valid model numbers are 100, 200 and 300.')
    model = int(input())

# The validation loop uses a long compound boolean expression, and iterates until model equals 100 and 200 or 300.

# However, the validation loop can be simplified by writing a Boolean function to test the model variable and calling it in a loop. Let's write an is_invalid() function that takes one model parameter and returns True if the model is invalid and False otherwise. Then the validation loop can be rewritten as follows:
while is_invalid(model):
    print('Valid model numbers are 100, 200 and 300.')
    model = int(input())

# After this change, the cycle becomes easier to read. Now it is quite obvious that the cycle is repeated until the model number is invalid. The code snippet below shows how the is_invalid() function could be written. It takes a model number as an argument, and if the argument is not 100, 200, or 300, then this function returns True, saying it's invalid. Otherwise, the function returns False.
def is_invalid(model):
    if model != 100 and model != 200 and model != 300:
        return True
    else:
        return False

# NOTE: Creating functions that implement such simple logic is not always the best solution, as it increases the size of the code and leads to the time spent in calling the function and returning the result, which can affect the performance of the program.
