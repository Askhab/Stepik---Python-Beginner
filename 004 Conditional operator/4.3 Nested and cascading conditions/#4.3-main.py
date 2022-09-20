# Conditional operator
# nested operator
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print('First quarter')
    else:
        print('Fourth quarter')
else:
    if y > 0:
        print('Second quarter')
    else:
        print('Third quarter')

# In this example, the nesting level is so deep that the code becomes hard to understand.
grade = int(input('Enter your mark on 100-point system: '))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70:
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)

# Cascading conditional operator
# if condition:
#     code block
# elif condition2:
#     code block
# else:
#     code block

# Rewrite code from last exercise
grade = int(input('Enter your mark: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)
