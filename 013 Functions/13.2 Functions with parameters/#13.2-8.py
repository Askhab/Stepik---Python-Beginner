from math import ceil


def draw_triangle(fill, base):
    average = ceil(base / 2)
    for i in range(base):
        if not i >= average:
            print(fill * (i + 1))
        else:
            print(fill * (average - 1))
            average -= 1


# reading inputs
fill = input()
base = int(input())

# executing function
draw_triangle(fill, base)
