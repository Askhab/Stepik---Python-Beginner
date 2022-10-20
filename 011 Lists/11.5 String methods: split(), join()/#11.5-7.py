s = input()
a = s.split(".")
check = False

for i in a:
    if int(i) < 0 or int(i) > 255:
        check = True

if check:
    print("НЕТ")
else:
    print("ДА")
