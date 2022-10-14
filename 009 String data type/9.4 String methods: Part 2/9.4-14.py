s = input()

if s.count("f") >= 2:
    print(s.index("f"), s.rindex("f"), sep=" ")
elif s.count("f") == 1:
    print(s.index("f"))
else:
    print("NO")
