def is_valid_password(password):
    data = password.split(":")
    is_palindrom = False
    is_prime = False
    is_even = False

    if len(data) > 3:
        return False

    if data[0] == data[0][::-1]:
        is_palindrom = True
    else:
        return False

    if int(data[1]) > 1:
        for i in range(2, int(data[1])):
            if (int(data[1]) % i) == 0:
                return False
        else:
            is_prime = True
    else:
        return False

    if int(data[2]) % 2 == 0:
        is_even = True
    else:
        return False

    if is_palindrom and is_prime and is_even:
        return True


psw = input()

print(is_valid_password(psw))
