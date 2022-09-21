str1 = len(input())
str2 = len(input())
str3 = len(input())
minnum = min(str1, str2, str3)
maxnum = max(str1, str2, str3)
midnum = ((str1 + str2 + str3) - minnum) - maxnum
if midnum - minnum == maxnum - midnum:
    print("YES")
else:
    print("NO")
