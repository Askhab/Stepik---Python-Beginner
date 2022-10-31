def get_days(month):
    even = [1, 3, 5, 7, 8, 10, 12]
    odd = [4, 6, 9, 11]
    if month == 2:
        return 28
    elif month in even:
        return 31
    elif month in odd:
        return 30


num = int(input())

print(get_days(num))
