def is_correct_bracket(text):
    data = list(text)

    while len(data) != 0:
        if data[0] != "(" or data.count("(") != data.count(")"):
            return False
        else:
            del data[0]
            del data[data.index(")")]
    return True


txt = input()

print(is_correct_bracket(txt))
