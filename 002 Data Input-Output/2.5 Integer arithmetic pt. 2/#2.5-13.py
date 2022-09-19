number = int(input())
firstNum = number // 100
midNUm = (number % 100) // 10
lastNum = number % 10
print('Сумма цифр =', firstNum + midNUm + lastNum)
print('Произведение цифр =', firstNum * midNUm * lastNum)
