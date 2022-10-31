# FUNCTION WITH RETURN VALUE
# A function with a return value is similar to a function without a return value in that:

# - it is a set of instructions that performs a specific task;
# - When a function needs to be executed, it is called.

# However, when a return function terminates, it returns a value to the part of the program that called it. The return value from the function is used like any other: it can be assigned to a variable, displayed on the screen, used in a mathematical expression (if it is a number), etc.

# We have already seen many return functions:

# function int() - converts a string to an integer and returns it;
# float() function - converts a string to a real number and returns it;
# range() function - returns a sequence of integers 0, 1, 2, ...;
# abs() function - returns the absolute value of a number (number modulus);
# len() function returns the length of a string or list.

# A function with a return value is written in the same way as without, but it must have a return statement.

# Here is the general format of a function definition with a return value in Python:

# def function_name():
#     code block
#     return expression

# The function must have a return statement that takes the form:

# return expression

# The value of the expression that follows the return keyword will be sent to the part of the program that called the function. It can be a variable or an expression, for example, a mathematical one.

# When studying real numbers, we solved the problem of converting degrees Fahrenheit to degrees Celsius using the formula C = (5 / 9) * (F - 32)

# Let's write a function that performs the translation:

def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result


# The task of this function is to take one number temp as an argument - the number of degrees Fahrenheit, and return another - the number of degrees Celsius.

# Let's take a look at her work. The first statement in the function block assigns the value (5 / 9) * (temp - 32) to the variable result. The return statement is then executed, which ends the function and sends the value from the result variable back to the part of the program that called the function.

# function to convert degrees Fahrenheit to degrees Celsius
def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result


# # main program
temp = float(input('Enter Fahrenheit degrees: '))
celsius = convert_to_celsius(temp)
print(celsius)  # degrees Celsius


# The main program receives a single number from the user, the value in degrees Fahrenheit, and calls the function, passing the value of the temp variable as an argument. The value returned from the convert_to_celsius function is assigned to the celsius variable.


# MAKING THE MOST OF THE return STATEMENT
# Let's take another look at the convert_to_celsius() function:

def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result


# Note that two things happen inside this function: first, the value of the expression (5 / 9) * (temp - 32) is assigned to the result variable, and second, the value of the result variable is returned from the function. This function does its job well, but it can be simplified. Since the return statement returns the value of the expression, we eliminate the result variable and rewrite the function as follows:

def convert_to_celsius(temp):
    return (5 / 9) * (temp - 32)


# This version of the function does not store the value (5 / 9) * (temp - 32) in a separate variable, but immediately returns the value of the expression using the return statement. Does the same as the previous version, but in one step.


# USING MULTIPLE return
# There can be any number of return statements in one function. Consider the convert_grade() function, which converts a 100 grade to a 5 grade:

def convert_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70:
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1


# # main program
grade = int(input('Enter your 100 grade: '))
print(convert_grade(grade))


# The convert_grade() function uses 5 return instructions. Each of them returns the corresponding value and exits the function.

# The convert_grade() function can be rewritten with a single return statement:

def convert_grade(grade):
    result = -1
    if grade >= 90:
        result = 5
    elif grade >= 80:
        result = 4
    elif grade >= 70:
        result = 3
    elif grade >= 60:
        result = 2
    else:
        result = 1

    return result


# PROBLEM SOLVING
# Task 1. Write a function that returns the length of the hypotenuse of a right triangle given the known values of its legs.

# Solution. To find the length of the hypotenuse, we need to apply the Pythagorean theorem: the square of the
# hypotenuse of a right triangle is equal to the sum of the squares of its legs. In other words, if a, b - are the
# lengths of the legs, and c - is the length of the hypotenuse, then the equality takes place: c ** 2 = a ** 2 + b ** 2 ==> c = sqrt(a ** 2 + b ** 2)

# A function that calculates the length of the hypotenuse might look like this:
def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


# NOTE: To extract the square root, we used the exponentiation operator. Recall that the result of both expressions: math.sqrt(c) and c ** 0.5 is the same number

print(compute_hypotenuse(3, 4))  # 5.0
print(compute_hypotenuse(5, 12))  # 13.0
print(compute_hypotenuse(1, 1))  # 1.4142135623730951

# If we need to pass the numbers read from the keyboard to the program, then we write the following code:
x = int(input())
y = int(input())

hypotenuse = compute_hypotenuse(x, y)

print(hypotenuse)


# NOTE: The math module has a built-in function hypot(x, y) that returns the length of the hypotenuse of a right triangle with legs x and y.

# One of the main advantages of functions is the ability to reuse them to solve similar problems. Consider the problem of finding the distance between two points.


# Task 2. Write a function get_distance(x1, y1, x2, y2) that calculates the distance between (x1, y1) and (x2, y2)

# Solution: Distance between two points (x1, y1) and (x2, y2) is determined by the formula:
# p = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

# It is easy to see that the desired distance is the length of the hypotenuse of a right triangle with legs equal to |x1 - x2| and |y1 - y2|

# A function that calculates the distance between points can look like this:
def get_distance(x1, y1, x2, y2):
    return compute_hypotenuse(x1 - x2, y1 - y2)


# To calculate the desired distance, we use the compute_hypotenuse function we have already created, passing it the numbers x1 - x2 and y1 - y2 as arguments.

# The main program looks like:
x1, y1 = float(input()), float(input())  # read the coordinates of the first point
x2, y2 = float(input()), float(input())  # read the coordinates of the second point

print(get_distance(x1, y1, x2, y2))  # calculate and print distance between points


# Task 3. Write a function sum_digits(n) that takes a natural number as an argument and returns the sum of its digits.

# Solution. The sum_digits(n) function might look like:

def sum_digits(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result


# The main program looks like:

n = int(input())
print(sum_digits(n))  # calculate and print the sum of the digits of the read number


# Task 4. Write a function compute_average(numbers) that takes a list of numbers as an argument and returns the average of the elements in the list.

# Solution. To calculate the average value of the list elements, you need to calculate the sum of all elements and their number, that is, use the sum() and len() functions. The compute_average(numbers) function might look like:
def compute_average(numbers):
    return sum(numbers) / len(numbers)


# The main program looks like:
numbers = [1, 3, 5, 1, 6, 8, 10, 2]
print(compute_average(numbers))  # calculate and print the average of the list items

# The result of the work of such a program will be the number 4.5, which is the average value.


# MERGING TWO SORTED LISTS
# Merging two sorted lists into one is an important task in computer science. It naturally arises when sorting lists using merge sort.

# Let two lists of numbers, list1 and list2, sorted in ascending order, be given:
list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]


# The simplest solution to the list merging problem is using the sort() list method:

def merge(list1, list2):
    result = list1 + list2  # create the resulting list
    result.sort()  # sort the list with built-in sort() method
    return result  # return sorted list


list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = merge(list1, list2)  # call the function to merge two sorted lists
print(list3)


# The result of this code will be a list:
# [0, 3, 10, 11, 11, 12, 12, 20, 24, 26, 47, 47, 48, 53, 57, 58, 63, 65, 70, 77, 79, 80, 81, 84, 84 , 90, 95]

# And while the merge() function does its job perfectly, it absolutely does not take into account the fact that the two lists list1 and list2 are already sorted.


# QUICKLY MERGE TWO SORTED LISTS INTO ONE
# Suppose we have two lists list1 and list2 already sorted in ascending order.

# The quick merge algorithm is as follows:

# 1 - We create numerical pointers p1 = 0 and p2 = 0 to the beginnings of both lists list1 and list2, respectively;
# 2 -At each step, we take the smaller of the two elements list1[p1] and list2[p2];
# 3 - Write it to the resulting list;
# 4 - We increase the pointer to the first element of the list (p1 or p2) from which the element was taken by 11;
# 5 - When one of the initial lists has ended, we add all the remaining elements of the second list to the resulting
# list.
def quick_merge(list1, list2):
    result = []

    p1 = 0  # pointer to the first element of list1
    p2 = 0  # pointer to the first element of list2

    while p1 < len(list1) and p2 < len(list2):  # until at least one list ends
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # chaining the remainder
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


# The following program code:
list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = quick_merge(list1, list2)
print(list3)

# will output:
# [0, 3, 10, 11, 11, 12, 12, 20, 24, 26, 47, 47, 48, 53, 57, 58, 63, 65, 70, 77, 79, 80, 81, 84, 84 , 90, 95]
