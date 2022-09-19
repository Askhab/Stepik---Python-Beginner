# Logical operators

# and - logical multiplication
# or - logical addition
# not - logical negation

# # Operator AND
# # First ( and ) operator using
# age = int(input('How old are you?: '))
# grade = int(input('What grade are you in?: '))
#
# if age >= 12 and grade >= 7:
#     print('Access granted')
# else:
#     print('Access denied')
#
# # Second ( and ) operator using - arbitrary number of conditions
# age = int(input('How old are you?: '))
# grade = int(input('What grade are you in?: '))
# city = input('What city do you live in?: ')
#
# if age >= 12 and grade >= 7 and city == 'London':
#     print('Access granted')
# else:
#     print('Access denied')
#
# # Operator OR
# # First ( or ) operator using
# city = input('What city do you live?: ')
# if city == 'London' or city == 'New-York' or city == 'Los-Angeles':
#     print('Access granted')
# else:
#     print('Access denied')

# # Using both AND & OR operators
# age = int(input('How old are you?: '))
# grade = int(input('What grade are you in?: '))
# city = input('What city do you live in?: ')
#
# if age >= 12 and grade >= 7 and (city == 'London' or city == 'New-York'):
#     print('Access granted')
# else:
#     print('Access denied')

# # Operator NOT
# age = int(input('How old are you?: '))
# if not (age <= 12):
#     print('Access granted')
# else:
#     print('Access denied')

# Priority of operators
# logical negation is performing first - NOT
# then logical multiplication - AND
# last performing logical addition - OR
