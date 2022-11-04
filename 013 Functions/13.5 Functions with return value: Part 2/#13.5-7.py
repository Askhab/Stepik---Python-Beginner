# function declaration
def is_palindrome(text):
    data = [i.lower() for i in text if i.isalpha()]

    return data == data[::-1]


# reading inputs
txt = input()

# function call
print(is_palindrome(txt))
