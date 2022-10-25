numbers = [int(number) for number in input().split()]
print(*numbers, sep='+', end=f'={sum(numbers)}')
