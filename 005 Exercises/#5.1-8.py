# Task - Two different cells of a chessboard are given. Write a program that determines if the queen can move from the first cell to the second in one move. The program receives as input four numbers from 1 to 8 each, specifying the column number and row number, first for the first cell, then for the second cell. The program should print "YES" if it is possible to get to the second from the first cell by the queen's move, or "NO" otherwise.

col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if (col1 - row1) == (col2 - row2) or (col1 + row1) == (col2 + row2):
    print("YES")
elif (1 <= col1 <= 8 and 1 <= row1 <= 8 and 1 <= col2 <= 8 and 1 <= row2 <= 8) and (col1 == col2 or row1 == row2):
    print("YES")
else:
    print("NO")
