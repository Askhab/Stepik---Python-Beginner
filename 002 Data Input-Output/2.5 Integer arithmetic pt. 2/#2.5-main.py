# ** - Exponentiation
print('2 ** 0 =', 2 ** 0)  # 1
print('2 ** 1 =', 2 ** 1)  # 2
print('2 ** 2 =', 2 ** 2)  # 4
print('2 ** 3 =', 2 ** 3)  # 8
print('2 ** (-1) =', 2 ** (-1))  # 0.5

# ** - exponentiation is right-associative
# x ** y ** z   =>   x ** (y ** z).
print(2 ** 2 ** 3)     # 2 ** (2 ** 3) = 2 ** 8


# // - Integer division
print('10 // 3 =', 10 // 3)  # 3
print('10 // 4 =', 10 // 4)  # 2
print('10 // 5 =', 10 // 5)  # 2
print('10 // 6 =', 10 // 6)  # 1
print('10 // 12 =', 10 // 12)  # 0

# result of integer division - rounding is taken down
print('10 // 3 =', 10 // 3)  # 3
print('-10 // 3 =', -10 // 3)  # -4


# % - Remain of division
print('10 % 3 =', 10 % 3)  # 1
print('10 % 4 =', 10 % 4)  # 2
print('10 % 5 =', 10 % 5)  # 0
print('10 % 6 =', 10 % 6)  # 4
print('10 % 12 =', 10 % 12)  # 10
print('10 % 20 =', 10 % 20)  # 10


# getting the digits of two-digital numbers
num = 17
a = num % 10
b = num // 10
print(a)  # 7
print(b)  # 1

# getting the digits of three-digital numbers
num = 754
a = num % 10
b = (num % 100) // 10
c = num // 100
print(a)  # 4
print(b)  # 5
print(c)  # 7
