def find_all(target, symbol):
    data = []
    for i in range(len(target)):
        if target[i] == symbol:
            data.append(i)
    return data


s = input()
char = input()

print(find_all(s, char))
