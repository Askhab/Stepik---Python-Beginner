def convert_to_python_case(text):
    data = [text[0].lower()]
    for i in text[1:]:
        if 65 <= ord(i) <= 90:
            data.append("_")
            data.append(i.lower())
        else:
            data.append(i)

    return "".join(data)


txt = input()

print(convert_to_python_case(txt))
