def encrypt(text):
    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    words_list = text.split()
    encrypted_words_list = []
    encrypted_text = " "

    def out_of_length(step, lang):
        if step >= len(lang):
            return step % len(lang)
        else:
            return step

    for i in words_list:
        word_length = 0
        encrypted_word = ""

        for j in range(len(i)):
            if i[j].isalpha():
                word_length += 1

        for l in range(len(i)):
            if i[l].isalpha():
                if i[l].isupper():
                    encrypted_word += eng_alphabet[out_of_length(eng_alphabet.find(i[l].lower()) + word_length, eng_alphabet
                                                                 )].upper()
                else:
                    encrypted_word += eng_alphabet[out_of_length(eng_alphabet.find(i[l].lower()) + word_length, eng_alphabet)]
            else:
                encrypted_word += i[l]

        encrypted_words_list.append(encrypted_word)

    print(encrypted_text.join(encrypted_words_list))


encrypt(input())
