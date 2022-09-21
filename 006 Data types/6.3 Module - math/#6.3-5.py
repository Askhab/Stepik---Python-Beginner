from math import pi, sin, cos, tan

x = float(input())
r = (x * pi) / 180

print(sin(r) + cos(r) + (tan(r) * tan(r)))
