s = input()
hf = s.index("h")
hl = s.rindex("h") + 1

print(s[:hf] + s[hl:])
