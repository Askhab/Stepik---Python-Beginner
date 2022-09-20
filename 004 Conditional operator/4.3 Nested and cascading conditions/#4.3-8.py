number1 = int(input())
number2 = int(input())
operator = input()

if operator != '+' and operator != '-' and operator != '*' and operator != '/':
    print('Invalid operation')
elif number2 == 0:
    print("Can't divide by zero!")
elif operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/':
    print(number1 / number2)
