# function declaration
def is_password_good(password):
    upper = False
    lower = False
    digit = False

    if len(password) < 8:
        return False
    else:
        for i in password:
            if not upper and i.isupper():
                upper = True
            elif not lower and i.islower():
                lower = True
            elif not digit and i.isdigit():
                digit = True

    if upper and lower and digit:
        return True
    else:
        return False


# reading inputs
txt = input()

# function call
print(is_password_good(txt))
