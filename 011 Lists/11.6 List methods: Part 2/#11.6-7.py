t = input().lower()
li = t.split()
a = li.count("a")
an = li.count("an")
the = li.count("the")

print(f"Общее количество артиклей: {a + an + the}")
