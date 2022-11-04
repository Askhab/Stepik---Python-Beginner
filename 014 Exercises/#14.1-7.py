# function declaration
def number_to_words(num):
    list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    list_11 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    list_21 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

    if 0 <= num <= 10:
        return list_1[num - 1]
    elif num < 20:
        return list_11[num % 10 - 1]
    elif num > 19 and num % 10 == 0:
        return list_21[num // 10 - 2]
    elif num <= 99:
        return f"{list_21[num // 10 - 2]} {list_1[num % 10 - 1]}"


# reading inputs
n = int(input())

# function call
print(number_to_words(n))
