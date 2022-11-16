from random import choice

en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
word_list = ['air', 'animal', 'answer', 'area', 'bird', 'body', 'book', 'bottom', 'boy', 'brother', 'car', 'child', 'children', 'city', 'class', 'color', 'country', 'day', 'dog', 'door', 'east', 'example', 'eye', 'face', 'family', 'farm', 'father', 'feet', 'fire', 'fish', 'food', 'foot', 'friend', 'girl', 'hand', 'head', 'home', 'horse', 'house', 'idea', 'king', 'land', 'letter', 'life', 'line', 'list', 'love', 'men', 'money', 'month', 'mother', 'mountain', 'name', 'night', 'north', 'number', 'order', 'page', 'paper', 'pen', 'people', 'person', 'phone', 'picture', 'piece', 'place', 'plant', 'problem', 'product', 'question', 'river', 'rock', 'room', 'school', 'science', 'sea', 'sentence', 'ship', 'side', 'sister', 'song', 'sound', 'south', 'space', 'state', 'story', 'thriller', 'top', 'tree', 'watch', 'water', 'week', 'west', 'wind', 'woman', 'women', 'wood', 'word', 'world', 'year']


def check_input(word, alphabet):
    flag = False
    for i in word:
        if alphabet.find(i) != -1:
            flag = False
        else:
            flag = True


def letter_in_word(letter, word, hidden):
    output = ""
    for i in range(len(word)):
        if word[i] == letter:
            output += letter
        else:
            output += hidden[i]

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

    while tries > 0:
        try_word = input("Enter your word or letter! ").upper()

        if len(try_word) < 1 or check_input(try_word, en):
            print("Please enter only english alphabetical letter or word and try again!")
            continue

        if try_word in guessed_words or try_word in guessed_letters:
            print("You already tried this. This try didn't count.")
            continue

        if len(try_word) == 1:
            if try_word in word:
                guessed_letters.append(try_word)
                tries -= 1

                print(display_hangman(tries))
                print(f"You're guessed letter. But didn't guessed word. You have {tries} tries left.")
                word_completion = letter_in_word(try_word, word, word_completion)
                print(f"Your progress is {word_completion}")
            else:
                tries -= 1
                print(display_hangman(tries))
                print(f"The entered letter is not in the guessed word. You have {tries} tries left.")

        if len(try_word) > 1:
            if try_word == word:
                print("Congratulations, you guessed the word! You won!")

                answer = input("Would you like to play again? Enter - yes, or - no: ").upper()

                if answer == "YES":
                    play(chosen_word.upper())
                elif answer == "NO":
                    break
            else:
                tries -= 1
                guessed_words.append(try_word)
                print(display_hangman(tries))
                print(f"You didn't guessed the word. You have {tries} tries left. Try again.")
    else:
        print(display_hangman(tries))
        print("You failed to guess the word.")
        print(f"The word was - {word}")

        answer = input("Would you like to play again? Enter - yes, or - no: ").upper()

        if answer == "YES":
            play(choice(word_list).upper())
        elif answer == "NO":
            return False


play(choice(word_list).upper())
