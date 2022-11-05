from random import *


def start_game():
    border = int(input("Введите границу чисел для игры: "))
    n = randint(1, border)
    try_count = 0
    print("Добро пожаловать в числовую угадайку")

    def is_valid(value):
        return value.isdigit() and 1 <= int(value) <= 100

    while True:
        gamers_try = input(f"Введите целое число от 1 до {border} чтобы отгадать загаданное! ")

        if not is_valid(gamers_try):
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue
        else:
            gamers_try = int(gamers_try)

        if gamers_try < n:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            try_count += 1
            continue
        elif gamers_try > n:
            print("Ваше число больше загаданного, попробуйте еще разок")
            try_count += 1
            continue
        else:
            print("Вы угадали, поздравляем!")
            print(f"Число попыток угадать - {try_count}")
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            new_game = input("Хотите сыграть еще раз? (наберите да или нет): ").lower()

            if new_game == "да":
                start_game()
            else:
                break


start_game()
