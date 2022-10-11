line = input()
g = "ауоыиэяюёеАУОЫИЭЯЮЁЕ"
s = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
g_total = 0
s_total = 0

for i in range(0, len(line)):
    if line[i] in g:
        g_total += 1
    if line[i] in s:
        s_total += 1
print("Количество гласных букв равно", g_total)
print("Количество согласных букв равно", s_total)
