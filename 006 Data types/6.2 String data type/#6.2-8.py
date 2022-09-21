city1 = input()
city2 = input()
city3 = input()
len1 = len(city1)
len2 = len(city2)
len3 = len(city3)
minlen = min(len1, len2, len3)
maxlen = max(len1, len2, len3)
if minlen == len(city1) and maxlen == len(city2):
    print(city1)
    print(city2)
elif minlen == len(city1) and maxlen == len(city3):
    print(city1)
    print(city3)
elif minlen == len(city2) and maxlen == len(city1):
    print(city2)
    print(city1)
elif minlen == len(city2) and maxlen == len(city3):
    print(city2)
    print(city3)
elif minlen == len(city3) and maxlen == len(city1):
    print(city3)
    print(city1)
elif minlen == len(city3) and maxlen == len(city2):
    print(city3)
    print(city2)
