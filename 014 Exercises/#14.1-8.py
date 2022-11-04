def get_month(language, number):
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

    if language == "en":
        return "".join([lng_en[i] for i in range(len(lng_en)) if i == number - 1])
    elif language == "ru":
        return "".join([lng_ru[i] for i in range(len(lng_ru)) if i == number - 1])


lan = input()
num = int(input())

print(get_month(lan, num))
