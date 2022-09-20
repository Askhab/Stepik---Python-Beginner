# Task -  Write a program that determines if a year with a given number ends with two zeros. If the year ends, then print "YES", otherwise print "NO".

num = int(input())

if num % 100 == 0 and num % 10 == 0:
    print("YES")
else:
    print("NO")
