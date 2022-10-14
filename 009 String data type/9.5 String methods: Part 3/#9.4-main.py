# Character classification
# isalnum() - Method
# The isalnum() method determines whether the source string consists of alphanumeric characters. The method returns True if the source string is non-empty and contains only alpha-numeric characters, and False otherwise.

s1 = "abc123"
s2 = "abc$*123"
s3 = ""

print(s1.isalnum())   # True
print(s2.isalnum())   # False
print(s3.isalnum())   # False


# isalpha() - Method
# The isalpha() method determines if the input string consists of alphabetic characters. The method returns True if the source string is non-empty and consists only of literal characters, and False otherwise.
s1 = "ABCabc"
s2 = "abc123"
s3 = ""

print(s1.isalpha())   # True
print(s2.isalpha())   # False
print(s3.isalpha())   # False


# isdigit() - Method
# The isdigit() method determines if the input string consists of only numeric characters. The method returns True if the source string is non-empty and consists only of numeric characters, and False otherwise.
s1 = "1234567"
s2 = "abc123"
s3 = ""

print(s1.isdigit())   # True
print(s2.isdigit())   # False
print(s3.isdigit())   # False


# islower() - Method
# The islower() method determines whether all literal characters in the source string are lowercase (lowercase). The method returns True if all alphabetic characters of the source string are lowercase and False otherwise. All non-alphabetic characters are ignored!
s1 = "abc"
s2 = "abc1$d"
s3 = "Abc1$D"

print(s1.islower())   # True
print(s2.islower())   # True
print(s3.islower())   # False


# isupper() - Method
# The isupper() method determines whether all literal characters in the source string are upper case. The method returns True if all literal characters in the source string are uppercase and False otherwise. All non-alphabetic characters are ignored!
s1 = "ABC"
s2 = "ABC1$D"
s3 = "Abc1$D"

print(s1.isupper())   # True
print(s2.isupper())   # True
print(s3.isupper())   # False


# isspace() - Method
# The isspace() method determines if the source string consists of only whitespace characters. The method returns True if the string contains only whitespace characters and False otherwise.
s1 = "      "
s2 = "abc1$d"

print(s1.isspace())   # True
print(s2.isspace())   # False


# String formatting
# age = 27
# txt = "My name is Timur, I am " + age
# print(txt)   # Error

# We amy use str() function
# age = 27
# txt = "My name is Timur, I am " + str(age)
# print(txt)   # Works

# Better way - use format() method
age = 27
txt = "My name is Timur, I am {}".format(age)
print(txt)
# We pass the required parameters to the format method, and Python formats the specified string and puts them in the string in place of the {} placeholders. We can create as many placeholders as we want per line:
age = 27
name = "Timur"
profession = "math teacher"
txt = "My name is {}, I am {} years old, I work as a {}".format(name, age, profession)
print(txt)

# For clarity and formatting flexibility, we can use a serial number in the placeholder: {0}, {1}, {2},.... This number determines the position of the parameter passed to the format method (numbering starts from zero)
age = 27
name = "Timur"
profession = "math teacher"
txt = "My name is {0}, I am {1} years old, I work as a {2}".format(name, age, profession)
print(txt)

# The name parameter goes into the {0} placeholder, the age parameter goes into the {1} placeholder, and so on. We can use the same number in multiple placeholders
name = "Timur"
txt = "My name is {0}-{0}-{0}".format(name)
print(txt)


# f-strings
# Example with format() method
first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print('Hello, {0} {1}. You are {2}. You are a {3}. You were a member of {4}'.format(first_name, last_name, age, profession, affiliation))

# Python 3.6 introduces a new kind of string called f-strings. If you prefix a string with an f, placeholders can include code, such as a variable name. The previous code can be written as:
first_name = "Timur"
last_name = "Guev"
age = 27
profession = "math teacher"
affiliation = "BeeGeek"
print(f"Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}")

#
