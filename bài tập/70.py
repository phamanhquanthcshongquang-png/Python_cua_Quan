n = int(input())
A= []
for i in range(1,n + 1):
    a = int(input())
    A.append(a)
k = int(input())
A.pop(k - 1)
print(A)
