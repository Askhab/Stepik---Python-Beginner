a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a2 < b2 < a1 or b1 < a2 < b2:
    print("пустое множество")
elif a2 < a1 == b2 < b1:
    print(a1)
elif a1 < a2 == b1 < b2:
    print(a2)
elif a2 < a1 < b1 == b2:
    print(a1, b2, sep=" ")
elif a1 < a2 < b2 == b1:
    print(a2, b1, sep=" ")
elif a2 == a1 < b1 < b2:
    print(a2, b1, sep=" ")
elif a1 == a2 < b2 == b1:
    print(a1, b2, sep=" ")
elif a2 < a1 < b1 < b2:
    print(a1, b1, sep=" ")
elif a1 < a2 < b1 < b2:
    print(a2, b1, sep=" ")
elif a2 < a1 < b2 < b1:
    print(a1, b2, sep=" ")
elif a2 < a1 == b2 < b1:
    print(a1)
elif a1 < a2 < b2 < b1:
    print(a2, b2, sep=" ")
elif a2 < a1 < b1 < b2:
    print(a1, b1, sep=" ")
