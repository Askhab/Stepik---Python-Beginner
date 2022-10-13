# Case conversion
# The methods in this group perform case conversion on strings.

# capitalize() - Method
# The capitalize() method returns a copy of the string s in which the first character is uppercase and all other characters are lowercase.
s = "foO BaR BAZ quX"
print(s.capitalize())   # Foo bar baz qux

# Characters that are not alphabetic characters remain unchanged. The result of executing the following code:
s = "foo123#BAR#"
print(s.capitalize())   # Foo123#bar#


# swapcase() - Method
# The swapcase() method returns a copy of the string s in which all uppercase characters are converted to lowercase characters and vice versa.
s = "FOO Bar 123 baz qUX"
print(s.swapcase())   # foo bAR 123 BAZ Quz


# title() - Method
# The title() method returns a copy of the string s, in which the first character of each word is converted to uppercase.
s = "the sun also rises"
print(s.title())   # The Sun Also Rises


# lower() - Method
# The lower() method returns a copy of the string s in which all characters are lowercase.
s = "FOO Bar 123 baz qUX"
print(s.lower())   # foo bar 123 baz qux


# upper() - Method
# The upper() method returns a copy of the string s in which all characters are uppercase.
s = "FOO Bar 123 baz qUX"
print(s.upper())   # FOO BAR 123 BAZ QUX

# IMPORTANT - One very important note about methods in this category is that they do not modify the original string. If you want to change the string s you need to write the code: s = s.lower().
