n = int(input())
full = []

for i in range(n):
    full += [int(i) for i in input().split()]


def quick_merge(data):
    return sorted(data)


print(*quick_merge(full))
