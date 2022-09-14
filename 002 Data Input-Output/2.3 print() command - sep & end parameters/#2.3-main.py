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
print('a', 'b', 'c', sep='', end='')


# VARIABLES

variable_name = input()
print('Вы ввели текст:', variable_name)

# multiple variable assignment
name, surname = 'Timur', 'Guev'
print('Name:', name, 'Surname:', surname)
