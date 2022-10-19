n = int(input())
a = []

for i in range(n):
    a.append(input())

request = input()

for w in a:
    if request.lower() in w.lower():
        print(w)
