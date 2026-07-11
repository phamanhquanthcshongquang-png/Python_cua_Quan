n = int(input())
A = []
for i in range(1,n + 1):
    a = int(input())
    if a % 2 == 1:
        A.append(a)
B = len(A)
C = sum(A)
print(C / B)