# Search and Replace
# count() - Method
# count(<sub>, <start>, <end>) -  counts the number of non-overlapping occurrences of the substring <sub> in the original string s.
s = "foo goo moo"
print(s.count("oo"))
print(s.count("oo", 0, 8))   # count from 0 to 7 character


# startswith() - Method
# The startswith(<suffix>, <start>, <end>) method determines whether the source string s begins with the <suffix> substring. If the source string starts with the <suffix> substring, the method returns True, otherwise it returns False.
s = "foobar"
print(s.startswith("foo"))   # True
print(s.startswith("baz"))   # False


# endswith() - Method
# The endswith(<suffix>, <start>, <end>) method determines whether the source string s ends with the <suffix> substring. The method returns True if the source string ends with the substring <suffix> and False otherwise.
s = "foobar"
print(s.endswith("bar"))   # True
print(s.endswith("baz"))   # False


# find() & rfind() - Methods
# The find(<sub>, <start>, <end>) method finds the index of the first occurrence of the substring <sub> in the source string s. If the string s does not contain the substring <sub>, then the method returns -1. We can use this method along with the in operator to check if a given string contains some substring or not.
s = "foo bar foo baz foo qux"
print(s.find("foo"))      # 0
print(s.find("bar"))      # 4
print(s.find("qu"))       # 20
print(s.find("python"))   # -1

# The rfind(<sub>, <start>, <end>) method is identical to the find(<sub>, <start>, <end>) method, except that it searches for the first occurrence of the substring <sub> starting from the end of the string s .


# index() & rindex() - Methods
# The index(<sub>, <start>, <end>) method is identical to the find(<sub>, <start>, <end>) method, except that it throws a ValueError: substring not found error at runtime, if the substring <sub> is not found.
#
# The rindex(<sub>, <start>, <end>) method is identical to the index(<sub>, <start>, <end>) method except that it searches for the first occurrence of the substring <sub> starting from the end of string s .


# strip() - Method
# The strip() method returns a copy of the string s with all spaces at the beginning and end of the string removed.
s = '     foo bar foo baz foo qux      '
print(s.strip())   # "foo bar foo baz foo qux"


# lstrip() - Method
# The lstrip() method returns a copy of the string s with all spaces at the beginning of the string removed.
s = '     foo bar foo baz foo qux      '
print(s.lstrip())   # "foo bar foo baz foo qux⎵ ⎵ ⎵ ⎵ ⎵ ⎵"


# rstrip() - Method
# The rstrip() method returns a copy of the string s with all trailing spaces removed.
s = '      foo bar foo baz foo qux      '
print(s.rstrip())   # "⎵ ⎵ ⎵ ⎵ ⎵ ⎵foo bar foo baz foo qux"

# The strip(), lstrip(), rstrip() methods can take an optional <chars> argument as input. The optional <chars> argument is a string that specifies the set of characters to remove.


# replace() - Method
s = "foo bar foo baz foo qux"
print(s.replace("foo", "grault"))   # grault bar grault baz grault qux

# The replace() method can take an optional third <count> argument that specifies the number of replacements.
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault', 2))   # grault bar grault baz foo qux
