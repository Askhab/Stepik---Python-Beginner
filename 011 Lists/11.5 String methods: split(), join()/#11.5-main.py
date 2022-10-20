# String methods

# split() - Method
# The split() method splits a string into words using a sequence of whitespace characters as the delimiter.
s = 'Python is the most powerful language'
words = s.split()
print(words)   # ["Python", "is", "the", "most", "powerful", "language"]
# Thus, calling the split() method splits the string into words and returns a list containing all the words.

# Example
numbers = input().split()   # 1, 2, 3, 4, 5
print(numbers)              # ["1", "2", "3", "4", "5"]
# If you enter the string 1 2 3 4 5 when you run this program, then the list of numbers will be ['1', '2', '3', '4', '5']. Note that the list will consist of strings, not numbers. If you want to get exactly a list of numbers, then you need to convert the elements of the list one by one to numbers:

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


# Optional parameter
# The split() method has an optional parameter that specifies which set of characters will be used as a separator between list items. For example, calling the split('.') method will return a list obtained by splitting the source string on the character '.'.

ip = "192.168.1.24"
number = ip.split(".")
print(numbers)   # ["192", "168", "1", "24"]


# join() - Method
# The join() method collects a string from the elements of the list, using the string to which the method is applied as a delimiter.

words = ["Python", "is", "the", "most", "powerful", "language"]
s = " ".join(words)
print(s)   # Python is the most powerful language

# Note that all the words are separated by a single space, since the join() method was called on a string consisting of a single space character ' '.

words = ['Мы', 'учим', 'язык', 'Python']
print('*'.join(words))        # Мы*учим*язык*Python
print('-'.join(words))        # Мы-учим-язык-Python
print('?'.join(words))        # Мы?учим?язык?Python
print('!'.join(words))        # Мы!учим!язык!Python
print('*****'.join(words))    # Мы*****учим*****язык*****Python
print('abc'.join(words))      # МыabcучимabcязыкabcPython
print('123'.join(words))      # Мы123учим123язык123Python

# Remember: The split() string method is used to convert a string to a list, and the join() method is to convert a list to a string.


# Note 1: There is a big difference between the results of calling the s.split() and s.split(' ') methods. The difference in behavior appears when a string contains multiple spaces between words.
s = 'Python    is   the  most  powerful  language'
words1 = s.split()
words2 = s.split(' ')
print(words1)   # ['Python', 'is', 'the', 'most', 'powerful', 'language']
print(words2)   # ['Python', '', '', '', 'is', '', '', 'the', '', 'most', '', 'powerful', '', 'language']


# Note 2: The split() and join() methods are string methods. The following code results in an error:

print([1, 2].split())    # AttributeError: 'list' object has no attribute 'split'
print([1, 2].join([3, 4, 5]))    # AttributeError: 'list' object has no attribute 'join'


# Note 3: The join() string method only works on a list of strings. The following code results in an error:

numbers = [1, 2, 3, 4]  # список чисел
s = '*'.join(numbers)
print(s)   # TypeError: sequence item 0: expected str instance, int found
