def is_pangram(text):
    alpha = set(text.lower())
    return len(alpha) == 27


text = input()

print(is_pangram(text))
