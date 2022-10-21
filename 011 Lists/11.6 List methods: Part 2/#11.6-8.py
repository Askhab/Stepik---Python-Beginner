n = input()
m = int(n.replace("#", ""))

for i in range(m):
    s = input()
    if "#" in s:
        s = s[:s.index("#")].rstrip()
        print(s)
    else:
        print(s)
