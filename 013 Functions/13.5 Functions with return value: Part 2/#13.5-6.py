# function declaration
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count == 1:
            return True
        else:
            return False


# reading inputs
txt1 = input()
txt2 = input()

# function call
print(is_one_away(txt1, txt2))