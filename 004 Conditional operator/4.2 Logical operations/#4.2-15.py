col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())
if (1 <= col1 <= 8 and 1 <= row1 <= 8 and 1 <= col2 <= 8 and 1 <= row2 <= 8) and ((col1 == col2 or col1 == col2 + 1 or col1 == col2 -1) and (row1 == row2 or row1 == row2 + 1 or row1 == row2 - 1)):
    print('YES')
else:
    print('NO')
