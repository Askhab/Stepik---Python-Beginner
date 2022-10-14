s = input()
count = 0

for i in range(10):
    count += s.count(str(i))
print(count)
