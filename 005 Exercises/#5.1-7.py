# Task - Two different cells of a chessboard are given. Write a program that determines if a knight can get from the first cell to the second in one move. The program receives as input four numbers from 1 to 8 each, specifying the column number and row number, first for the first cell, then for the second cell. The program should print "YES" if it is possible to get to the second from the first cell by the knight's move, or "NO" otherwise.

col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if (col1 - col2 == 2 or col1 - col2 == -2) and (row1 - row2 == 1 or row1 - row2 == -1):
    print("YES")
elif (col1 - col2 == 1 or col1 - col2 == -1) and (row1 - row2 == 2 or row1 - row2 == -2):
    print("YES")
else:
    print("NO")
