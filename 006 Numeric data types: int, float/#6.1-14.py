num = int(input())
num1 = num // 100
num2 = (num // 10) % 10
num3 = num % 10
maxNum = max(num1, num2, num3)
minNum = min(num1, num2, num3)
midNum = (num1 + num2 + num3) - maxNum - minNum

if (maxNum - minNum) == midNum:
    print("Число интересное")
else:
    print("Число неинтересное")
