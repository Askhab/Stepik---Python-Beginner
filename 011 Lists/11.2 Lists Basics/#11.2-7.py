rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

for i in range(len(rainbow)):
    if rainbow[i] == "Green":
        rainbow[i] = "Зеленый"
    elif rainbow[i] == "Violet":
        rainbow[i] = "Фиолетовый"
print(rainbow)
