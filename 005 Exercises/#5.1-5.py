# Task - Write a program that takes a number as input and outputs the text "YES" or "NO" depending on the conditions.
# Terms:
#     - if the number is odd, then output "YES";
#     - if the number is even in the range from 2 to 5 (inclusive), then print "NO";
#     - if the number is even in the range from 6 to 20 (inclusive), then print "YES";
#     - if the number is even and greater than 20, then print "NO".

num = int(input())

if num % 2 == 1:
    print("YES")
elif num % 2 == 0 and 2 <= num <= 5:
    print("NO")
elif num % 2 == 0 and 6 <= num <= 20:
    print("YES")
elif num % 2 == 0 and num > 20:
    print("NO")
