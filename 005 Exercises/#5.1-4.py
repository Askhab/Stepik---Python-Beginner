# Task - Write a program that reads an integer and outputs its corresponding Roman numeral. If the number is outside the range 1-10, then the program should display the text "error".

num = int(input())

if 1 > num or num > 10:
    print("ошибка")
elif num == 1:
    print("I")
elif num == 2:
    print("II")
elif num == 3:
    print("III")
elif num == 4:
    print("IV")
elif num == 5:
    print("V")
elif num == 6:
    print("VI")
elif num == 7:
    print("VII")
elif num == 8:
    print("VIII")
elif num == 9:
    print("IX")
elif num == 10:
    print("X")
