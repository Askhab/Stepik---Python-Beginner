a = int(input())
b = int(input())
c = int(input())
if (a == b and not (a == c)) or (a == c and not (a == b)) or (b == c and not (b == a)):
    print("Равнобедренный")
elif a == b == c:
    print("Равносторонний")
elif not (a == b == c):
    print("Разносторонний")
