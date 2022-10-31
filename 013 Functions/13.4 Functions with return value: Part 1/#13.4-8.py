def get_factors(num):
    data = []
    for i in range(1, num + 1):
        if num % i == 0:
            data.append(i)
    return data


n = int(input())

print(get_factors(n))
