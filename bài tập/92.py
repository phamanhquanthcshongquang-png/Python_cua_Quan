s = input()
A =[]
for i in s:
    if i.isdigit():
        A.append(i)
print("".join(A))