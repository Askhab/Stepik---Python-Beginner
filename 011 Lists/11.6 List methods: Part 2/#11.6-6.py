s = input()
a = s.split()
r = []

for i in a:
    r.append(int(i))

max_int = max(r)
min_int = min(r)
max_ind = r.index(max_int)
min_ind = r.index(min_int)

r[max_ind], r[min_ind] = r[min_ind], r[max_ind]

print(*r)
