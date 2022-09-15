print('a', 'b', 'c')
print('d', 'e', 'f')

# additional parameter - sep
print('a', 'b', 'c', sep='*')
print('e', 'd', 'f', sep='**')

# additional parameter - end
print('a', 'b', 'c', end='@')
print('d', 'e', 'f', end='@@')
print()

# sep & end - both
print('a', 'b', 'c', sep='*', end='finish')
print('d', 'e', 'f', sep='**', end='^__^')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='#')
print('m', 'n', 'o', sep='/', end='!')
print()

# removing all additional symbols
print('a', 'b', 'c', sep='', end='\n')


# VARIABLES

variable_name = input()
print('Вы ввели текст:', variable_name)

# multiple variable assignment - 1 version
name, surname = 'Timur', 'Guev'
print('Name:', name, 'Surname:', surname)

# multiple variable assignment - 2 version
name, surname = input(), input()
print('Имя:', name, 'Фамилия:', surname)

# swap the values of two variables
name1 = 'Alyx'
name2 = 'Gvido'
name1, name2 = name2, name1
print('Name1:', name1)
print('Name2:', name2)
