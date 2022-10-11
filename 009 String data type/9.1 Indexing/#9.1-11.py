t = input()
flag = False

for i in t:
    for j in range(0, 10, 1):
        if i == str(j):
            flag = True
if not flag:
    print("No numbers")
else:
    print("Number")
