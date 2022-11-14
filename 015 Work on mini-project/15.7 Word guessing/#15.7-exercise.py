from random import choice

word_list = ["человек", "слово", "лицо", "дверь", "земля", "корабль", "ребенок", "история", "женщина", "развитие",
             "пщеница", "хозяйство", "поселение", "спектакль", "автомобиль", "экономика", "литература", "граница",
             "магазин", "заграница", "ячмень", "республика", "личность"]


def get_word(words):
    return choice(words).upper()


def letter_in_word(letter, word):
    output = ""
    for i in word:
        if i == letter:
            output += letter
        else:
            output += "_"

    return output


def display_hangman(tries):
    stages = [
        '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ ⎞
                   |    
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ 
                   |
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |
                   |
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼
                   |
                   |
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |      ▼
                   |
                   |
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''']
    return stages[tries]


chosen_word = get_word(word_list)


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print("Let's play in word guessing game!")
    print(f"In start of the game we have: {display_hangman(tries)} \n and {tries} - tries. Let's go!")
    print(f"We guessed {word_completion} word, guessed word length = {len(word_completion)} letters.")

    print(f"THE WORD IS - {word}")

    while tries < 6 or not guessed:
        try_word = input("Enter your word or letter! ").upper()

        if not try_word.isalpha() or len(try_word) < 1:
            print("Please enter only english alphabetical letters and try again!")
            continue

        if try_word in guessed_words or try_word in guessed_letters:
            print("You already tried this. This try didn't count.")
            continue

        if len(try_word) == 1 and try_word in word and not guessed:
            guessed_letters.append(try_word)
            tries -= 1

            print(f"You're guessed letter. But didn't guessed word. You have {tries} tries left.")
            print(f"Your progress is {letter_in_word(try_word, word)}")
            print(display_hangman(tries))
        else:
            tries -= 1
            print(f"The entered letter is not in the guessed word. You have {tries} tries left.")
            print(display_hangman(tries))

        if try_word == word:
            print("Congratulations, you guessed the word! You won!")
        else:
            tries -= 1
            guessed_words.append(try_word)
            print(f"You didn't guessed the word. You have {tries} tries left. Try again.")
    else:
        print(display_hangman(tries))
        print("You failed to guess the word.")
        print(f"The word was - {word}")


play(chosen_word.upper())
