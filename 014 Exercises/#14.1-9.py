def is_magic(date):
    day = date[0] + date[1]
    month = date[3] + date[4]
    last_num = date[-2] + date[-1]

    return int(day) * int(month) == int(last_num)


date = input()

print(is_magic(date))
