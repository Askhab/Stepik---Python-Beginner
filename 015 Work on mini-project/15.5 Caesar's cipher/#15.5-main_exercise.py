def encrypt_decrypt():
    program_mode = input("Хотите зашифровать сообщение или расшифровать  его? (введите 'шифр' или 'дешифр') ").lower()

    while program_mode != "шифр" and program_mode != "дешифр":
        program_mode = input("Хотите зашифровать сообщение или расшифровать  его? (введите 'шифр' или 'дешифр') ").lower()

    using_language = input("Выберите язык для шифрования/дешифрования. (введите 'англ' или 'рус') ").lower()

    while using_language != "англ" and using_language != "рус":
        using_language = input("Выберите язык для шифрования/дешифрования. (введите 'англ' или 'рус') ").lower()

    shear_step = int(input("Введите шаг сдвига (число от 1 до 100) "))

    while shear_step <= 0 or shear_step > 100:
        shear_step = int(input("Введите шаг сдвига (число от 1 до 100) "))

    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

    def out_of_length(step, lang):
        if step >= len(lang):
            return step % len(lang)
        else:
            return step

    def lower_or_upper(symbol, language, step):
        if program_mode == "шифр" and symbol.isupper():
            return language[out_of_length(language.find(symbol.lower()) + step, language)].upper()
        elif program_mode == "шифр" and symbol.islower():
            return language[out_of_length(language.find(symbol) + step, language)]
        elif program_mode == "дешифр" and symbol.isupper():
            return language[out_of_length(language.find(symbol.lower()) - step, language)].upper()
        elif program_mode == "дешифр" and symbol.islower():
            return language[out_of_length(language.find(symbol) - step, language)]

    def encryption(text, language, step):
        encrypted_text = ""
        if language == "англ":
            for i in text:
                if i.lower() in eng_alphabet:
                    encrypted_text += lower_or_upper(i, eng_alphabet, step)
                else:
                    encrypted_text += i

        if language == "рус":
            for i in text:
                if i.lower() in rus_alphabet:
                    encrypted_text += lower_or_upper(i, rus_alphabet, step)
                else:
                    encrypted_text += i

        print(encrypted_text)

    def decryption(text, language, step):
        decrypted_text = ""
        if language == "англ":
            for i in text:
                if i.lower() in eng_alphabet:
                    decrypted_text += lower_or_upper(i, eng_alphabet, step)
                else:
                    decrypted_text += i

        if language == "рус":
            for i in text:
                if i.lower() in rus_alphabet:
                    decrypted_text += lower_or_upper(i, rus_alphabet, step)
                else:
                    decrypted_text += i

        print(decrypted_text)

    if program_mode == "шифр":
        encryption(input("Введите текст который вы хотели бы зашифровать: "), using_language, shear_step)
    elif program_mode == "дешифр":
        decryption(input("Введите текст который вы хотели бы расшифровать: "), using_language, shear_step)


encrypt_decrypt()
