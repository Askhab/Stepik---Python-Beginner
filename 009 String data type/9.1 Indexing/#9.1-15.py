num = int(input())
s = ""

while num > 0:
    if num % 2 == 1:
        s = "1" + s
    elif num % 2 == 0:
        s = "0" + s
    num = int(num / 2)
print(s)
