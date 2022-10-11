line = input()
p = 0
s = 0

for i in line:
    if i == "+":
        p += 1
    elif i == "*":
        s += 1
print("The symbol + occurs", p, "times")
print("The symbol * occurs", s, "times")
