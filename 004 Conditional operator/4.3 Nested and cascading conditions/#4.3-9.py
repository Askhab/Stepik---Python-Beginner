color1 = input()
color2 = input()
if not (color1 == "синий" or color1 == "красный" or color1 == "желтый") or not (color2 == "синий" or color2 == "красный" or color2 == "желтый"):
    print("ошибка цвета")
elif color1 == color2:
    print(color1)
elif (color1 == "синий" or color2 == "синий") and (color1 == "красный" or color2 == "красный"):
    print("фиолетовый")
elif (color1 == "синий" or color2 == "синий") and (color1 == "желтый" or color2 == "желтый"):
    print("зеленый")
elif (color1 == "красный" or color2 == "красный") and (color1 == "желтый" or color2 == "желтый"):
    print("оранжевый")
