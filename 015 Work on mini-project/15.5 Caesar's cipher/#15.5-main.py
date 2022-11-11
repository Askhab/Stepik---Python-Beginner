# CAESAR'S CIPHER
# The Caesar cipher (shift cipher) is one of the simplest and most widely known encryption methods. A Caesar cipher is a type of substitution cipher in which each character in the plaintext is replaced by a character that is some constant number of positions to the left or right of it in the alphabet.

# NOTE: A substitution cipher is an encryption method that replaces elements of the original plaintext with others, in accordance with a certain rule.

# For example, in a right-shift cipher by 33 positions, A is replaced by D, B is replaced by E, and so on, until Z is replaced by C.

# The Caesar cipher is easy to crack and has almost no practical use.


# MATHEMATICAL MODEL
# If we match each character of the alphabet with its serial number (numbering from 00), then encryption and decryption can be expressed by modular arithmetic formulas:
# y=(x+k) mod n,
# x=(y−k) mod n,

# where xx is the plaintext character, yy is the ciphertext character, nn is the cardinality of the alphabet (number of characters), and kk is the key.

# The mod operation means the operation of finding the remainder. In Python, to find the remainder of a division of two numbers, we use the % operator.

# EXAMPLE:
# Encryption using key k=3. The letter "Е" "shifts" three letters forward and becomes the letter "З". A solid sign "Ъ" moved forward three letters becomes an "Э", a letter "Я" moved forward three letters becomes a "Б", and so on:

# Initial alphabet: А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я
# Encrypted: Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я А Б В

# Original text:
# Съешь же ещё этих мягких французских булок, да выпей чаю.

# Ciphertext:
# Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн, жг еютзм ъгб.


# CRACKING THE CIPHER
# The Caesar cipher can be easily broken even if the cracker only knows the ciphertext. Two situations can be considered:

# 1. The cracker knows (or assumes) that a simple substitution cipher was used, but does not know that it is a Caesar scheme.
# 2. The cracker knows that a Caesar cipher was used, but does not know the value of the shift.

# In the first case, the cipher can be broken using the frequency analysis method. Using this method, a cracker is likely to quickly notice the regularity in the solution and realize that the cipher being used is a Caesar cipher.

# In the second case, breaking the cipher is even easier. There are not many options for shift values (26 for English, 32 for Russian), all of them can be checked by enumeration.


# NOTES:
# Note 1. The transformation used in the Caesar cipher is usually denoted as ROT N, where N is a shift,
# ROT is an abbreviation for the word ROTATE, in this case "cyclic shift". For example, the notation ROT 2 denotes a shift of 22 positions, that is, "а" becomes "в", "б" becomes "г", and so on, and at the end "ю" becomes "а" and "я" - in "б".

# Note 2. The number of different transformations depends on the length of the alphabet:

# - for the Russian language, 3232 different transformations are possible (the transformations ROT 0 and ROT 33 retain the original text, and then repetitions begin);
# - for the English language, 2525 different transformations are possible (the transformations ROT 0 and ROT 26 preserve the original text, and then repetitions begin).

# Note 3: Non-alphabetic characters - punctuation marks, spaces, numbers - do not change.

# Note 4. A natural development of the Caesar cipher was the Vigenère's cipher.
