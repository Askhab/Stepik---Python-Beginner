# s = input()
# a = s.split()
# r = s.split()
# count = 0
#
# for i in a:
#     del r[0]
#     for y in r:
#         if i == y:
#             count += 1
#
# print(count)

s = input()
a = s.split()
count = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            count += 1

print(count)
