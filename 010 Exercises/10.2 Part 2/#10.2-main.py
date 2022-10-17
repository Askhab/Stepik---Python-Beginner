# 10.2-1
# Insert the missing code snippet so that the output of the program is the length of the string s.
# Answer -
# s = 'Python rocks!'
# print(len(s))


# 10.2-2
# Insert the missing code snippet so that the program outputs the fourth character of the string s.
# Answer -
# s = 'Python rocks!'
# print(s[3])


# 10.2-3
# Insert the missing code snippet so that the program outputs the characters of the string s from 2 to 5 inclusive.
# Answer -
# s = 'Python rocks!'
# print(s[1:5])


# 10.2-4
# Insert the missing code snippet so that the output of the program is the string s without leading or trailing whitespace characters.
# Answer -
# s = '    Python rocks!     '
# print(s.strip())


# 10.2-5
# Insert the missing code snippet so that the output of the program is the string s in capital letters (upper case).
# Answer -
# s = 'Python rocks!'
# print(s.upper())


# 10.2-6
# Insert the missing code snippet so that the output of the program is the string s in which the character "o" is replaced by the character "@".
# Answer -
# s = 'Python rocks!'
# print(s.replace("o", "@"))


# 10.2-7
# The input to the program is a string of text. Write a program that removes from it all characters with indices multiple of 3, i.e. characters with indices 0, 3, 6, ... .

# Input data format
# The input to the program is a string of text.

# Output format
# The program should output a line of text in accordance with the condition of the problem.

# Answer -
# s = input()
# ns = ""
#
# for i in range(len(s)):
#     if i == 0 or i % 3 == 0:
#         continue
#     else:
#         ns += s[i]
# print(ns)


# 10.2-8
# The input to the program is a string of text. Write a program that replaces all occurrences of the number 1 with the word "one".

# Input data format
# The input to the program is a string of text.

# Output format
# The program should display the text in accordance with the condition of the problem.

# Answer -
# s = input()
#
# print(s.replace("1", "one"))


# 10.2-9
# The input to the program is a string of text. Write a program that removes all occurrences of the "@" character.

# Input data format
# The input to the program is a string of text.

# Output format
# The program should display the text in accordance with the condition of the problem.

# Answer -
# s = input()
#
# print(s.replace("@", ""))


# 10.2-10
# The input to the program is a string of text. Write a program that prints the index of the second occurrence of the letter "f". If the letter "f" occurs only once, print the number -1, and if it does not occur even once, print the number -2.

# Input data format
# The input to the program is a string of text.

# Output format
# The program should display the text in accordance with the condition of the problem.

# Answer -
# s = input()
# count = s.count("f")
# ns = s.replace("f", "o", 1)
# i = ns.find("f")
#
# if count >= 2:
#     print(i)
# elif count == 1:
#     print(-1)
# elif count == 0:
#     print(-2)


# 10.2-11
# The input to the program is a line of text in which the letter "h" occurs at least twice. Write a program that returns the original string and reverses the sequence of characters between the first and last occurrences of the letter "h".

# Input data format
# The input to the program is a string of text.

# Output format
# The program should display the text in accordance with the condition of the problem.

# Answer -
# s = input()
# fl = s.find("h") + 1
# ll = s.rfind("h")
# ns = s[fl:ll]
# fs = s[:fl] + ns[::-1] + s[ll:]
#
# print(fs)
