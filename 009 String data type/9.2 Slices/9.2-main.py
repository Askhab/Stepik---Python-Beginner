# String slices
# Consider the line s = "abcdefghij"

#  0   1   2   3   4   5   6   7   8   9   - Positive indices
#  a   b   c   d   e   f   g   h   i   j   - Line
# -10 -9  -8  -7  -6  -5  -4  -3  -2  -1   - Negative indices

# With slicing, we can get multiple characters from a source string by creating a colon-separated index range s[x:y]

# print(s[2:5])   - cde
# print(s[0:6])   - abcdef
# print(s[2:7])   - cdefg

# When s[x:y] is sliced, the first number is where the slice starts (inclusive) and the second is where the slice ends (exclusive). By slicing strings, we create a substring, which is essentially a string within another string.


# Slice to the end, from the beginning
# If you omit the second parameter in the slice s[x:] (but put a colon), then the slice is taken up to the end of the string. Similarly, if you omit the first parameter s[:y], then you can take a slice from the beginning of the string. The slice s[:] matches the string s itself

# print(s[2:])   - cdefghij
# print(s[:7])   - abcdefg

# Slice s[:] returns the original string

# Negative indices in slice
# print(s[-9:-4])   - bcdef
# print(s[-3:])     - hij
# print(s[:-3])     - abcdefg


# You can remove the last character from a string using the slice s[:-1]


# Slice step
# We can pass a third optional parameter to the slice, which is responsible for the slice step. For example, slice s[1:7:2] will create a string bdf consisting of every second character (indices 1, 3, 5, right border not included in the slice).

# Negative slice step
# If you specify a negative number as the slice step, then the characters will go in reverse order.

# print(s[::-1])   - jihgedcba

# print(s[1:7:2])   - bdf
# print(s[3::2])    - dfhj
# print(s[:7:3])    - adg
# print(s[::2])     - acegi
# print(s[::-1])    - jihgfedcba
# print(s[::-2])    - jhfdb


# Changing a string character by index
# s[4] = "X"  - doesn't work
s = "abcdefghij"
s = s[:4] + "X" + s[5:]
print(s)
