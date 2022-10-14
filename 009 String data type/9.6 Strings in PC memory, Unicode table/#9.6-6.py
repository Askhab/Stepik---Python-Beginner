n = int(input())
s = input()
d = ""

for i in s:
    t = ord(i) - n
    if t < 97:
        t += 26
        d += f"{chr(t)}"
    else:
        d += f"{chr(t)}"
print(d)
