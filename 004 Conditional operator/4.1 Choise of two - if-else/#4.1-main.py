# Operator if-else
answer = input('What is your favorite programming language? ')
if answer == 'Python':
    print('Correct! We are botting Python =)')
    print('Python - great programming language!')

# with else block
answer = input('What is your favorite programming language? ')
if answer == 'Python':
    print('Correct! We are botting Python =)')
    print('Python - great programming language!')
else:
    print('Not certainly in that way!')


# Comparison operators
num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'smaller than', num2)
if num1 > num2:
    print(num1, 'bigger than', num2)
if num1 == num2:
    print(num1, 'equals', num2)
if num1 != num2:
    print(num1, 'not equals', num2)

# Chains of comparison
age = int(input())
if 3 <= age <= 6:
    print("You're child")

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('The numbers are equals!')
else:
    print('Numbers are not equals!')
