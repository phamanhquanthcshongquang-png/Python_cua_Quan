import random
n = int(input())
A = []
for i in range(1,n + 1):
    so = random.randint(-100,100)
    A.append(so)
print(A)
so_dau = A[0]
so_cuoi = A[-1]
if (so_cuoi + so_dau) * n / 2 == sum(A):
    print("đây là cấp số cộng")
else:
    print("đây không là cấp số cộng")



