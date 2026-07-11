import re
n = input()
b = re.findall(r'\D+',n)
print(b)