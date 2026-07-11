import random
n = int(input())
A = []
B = []
for i in range(1,n + 1):
    so = random.randint(-300,300)
    A.append(so)
tong = A[0]
for a in A[1:]:
    tong += a
    B.append(tong)
print(A)
print(B)
