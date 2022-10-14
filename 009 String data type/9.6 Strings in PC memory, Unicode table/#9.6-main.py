# Lesson topic: representation of strings in computer memory, ASCII and Unicode

# ord() - Function
# The ord function allows you to determine the code of some character in the Unicode character table. The argument to this function is a single character.
num1 = ord("A")
num2 = ord("B")
num3 = ord("a")
print(num1, num2, num3)   # 65 66 97

# Note that the ord function only accepts a single character. If you try to pass a string containing more than one character:
# num = ord('Abc')
# print(num)   # TypeError: ord() expected a character, but string of length 3 found


# chr() - Function
# The chr function allows you to determine the character itself by the character code. The argument of this function is a numerical code.
chr1 = chr(65)
chr2 = chr(75)
chr3 = chr(110)
print(chr1, chr2, chr3)   # A K n

# The ord and chr functions often work in pairs. We can use the following code to print all uppercase letters of the English alphabet:
for i in range(26):
    print(chr(ord("A") + i))
# Note. The ord and chr functions are mutually inverse. For them, the following equalities are satisfied:
# print(chr(ord('A')))   # 'A'
# print(ord(chr(65)))    # 65
