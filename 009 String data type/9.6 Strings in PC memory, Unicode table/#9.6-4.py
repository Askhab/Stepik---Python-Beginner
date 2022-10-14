n1 = int(input())
n2 = int(input())
s = ""

for i in range(n1, n2 + 1):
    s += f"{chr(i)} "
print(s)
