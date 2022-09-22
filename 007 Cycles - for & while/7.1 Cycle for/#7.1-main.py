# Cycle for
# There are two main types of loops in Python
# - loops that repeat a certain number times - counting loops - for
# - loops that repeat until a certain event occurs - conditional loops - while

for i in range(10):
    print('Hello')

# entering data with input() command using for loop
for i in range(5):
    num = int(input())
    print('The square of your number is: ', num * num)
print('Cycle finished')

# for loop examples
print('A')
print('B')
for i in range(5):
    print('C')
    print('D')
print('E')


print('A')
print('B')
for i in range(5):
    print('C')
for i in range(5):
    print('D')
print('E')

