from random import sample

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
ambiguous_symbols = "il1Lo0O"

chars = ""

number_of_passwords = int(input("Введите желаемое количество паролей которые будут сгенерированы (число от 1 до 10): "))
length_of_password = int(input("Введите желаемую длинну пароля (цифра от 1 и тд): "))
include_digits = input("Будут ли в пароле использоваться цифры? (да / нет) ")
include_uppercase = input("Будут ли в пароле использоваться заглавные буквы? (да / нет) ")
include_lowercase = input("Будут ли в пароле использоваться строчные буквы? (да / нет) ")
include_punctuation = input("Будут ли в пароле использоваться символы? (да / нет) ")
include_ambiguous_symbols = "Будут ли в пароле использоваться неоднозначные символы? (да / нет) "

if include_digits == "да":
    chars += digits

if include_uppercase == "да":
    chars += uppercase_letters

if include_lowercase == "да":
    chars += lowercase_letters

if include_punctuation == "да":
    chars += punctuation

if include_ambiguous_symbols == "да":
    chars += ambiguous_symbols


def generate_password(length, symbols):
    password = "".join(sample(symbols, length))
    return password


for _ in range(number_of_passwords):
    print(generate_password(length_of_password, chars))
