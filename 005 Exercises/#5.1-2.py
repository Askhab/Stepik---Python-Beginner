# Task -  Two cells of a chessboard are given. Write a program that determines whether the specified cells have the same color or not. If they are painted in the same color, then print the word "YES", and if they are in different colors - then "NO".

col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())
if col1 % 2 == 1 and row1 % 2 == 1 and col2 % 2 == 1 and row2 % 2 == 1:
    print("YES")
elif col1 % 2 == 1 and row1 % 2 == 1 and col2 % 2 == 0 and row2 % 2 == 0:
    print("YES")
elif col1 % 2 == 0 and row1 % 2 == 0 and col2 % 2 == 0 and row2 % 2 == 0:
    print("YES")
elif col1 % 2 == 0 and row1 % 2 == 1 and col2 % 2 == 1 and row2 % 2 == 0:
    print("YES")
elif col1 % 2 == 0 and row1 % 2 == 0 and col2 % 2 == 1 and row2 % 2 == 1:
    print("YES")
elif col1 % 2 == 0 and row1 % 2 == 1 and col2 % 2 == 0 and row2 % 2 == 1:
    print("YES")
elif col1 % 2 == 1 and row1 % 2 == 0 and col2 % 2 == 0 and row2 % 2 == 1:
    print("YES")
elif col1 % 2 == 1 and row1 % 2 == 0 and col2 % 2 == 1 and row2 % 2 == 0:
    print("YES")
else:
    print("NO")
