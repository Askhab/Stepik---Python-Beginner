first = int(input())
second = int(input())
third = int(input())

if second < first < third or third < first < second:
    print(first)
elif first < second < third or third < second < first:
    print(second)
elif first < third < second or second < third < first:
    print(third)
