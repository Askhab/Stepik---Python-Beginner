s = input()
low = 0

for i in range(len(s)):
    if "a" <= s[i] <= "z":
        low += 1
print(low)
