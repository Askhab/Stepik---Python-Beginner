def number_of_factors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count


n = int(input())

print(number_of_factors(n))
