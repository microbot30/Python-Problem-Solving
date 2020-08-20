# printing all the 3 digit numbers in a string using regex
import re

s = input()
temp = re.findall(r"((?<![0-9])[0-9]{3}(?![0-9]))", s)
result = list(temp)
if len(result):
    for i in result:
        print(i, end=" ")
else:
    print("-1")
