s = input()
symbol = ""
count = 0

for i in range(len(s)):
    if s.count(s[i]) >= count:
        symbol = s[i]
        count = s.count(s[i])
print(symbol)
