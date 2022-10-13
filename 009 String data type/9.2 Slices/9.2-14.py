from math import ceil, floor

s = input()
fh = ceil(len(s) / 2)

print(s[fh:] + s[:fh])
