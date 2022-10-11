line = input()
check = ""
total = 0

for i in line:
    if check == "":
        check = i
    else:
        if i == check:
            total += 1
    check = i
print(total)
