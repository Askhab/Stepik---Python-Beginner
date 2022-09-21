a = float(input())
b = float(input())
c = float(input())
d = (b ** 2) - 4 * a * c
if d < 0:
    print("Нет корней")
elif d == 0:
    print((b * -1) / (2 * a))
elif d > 0:
    print(min((((b * -1) + (d ** 0.5)) / (2 * a)), (((b * -1) - (d ** 0.5)) / (2 * a))))
    print(max((((b * -1) + (d ** 0.5)) / (2 * a)), (((b * -1) - (d ** 0.5)) / (2 * a))))
