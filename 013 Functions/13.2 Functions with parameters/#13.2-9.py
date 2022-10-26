# function declaration
def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep="")


# reading inputs
name, surname, patronymic = input(), input(), input()

# executing function
print_fio(name, surname, patronymic)
