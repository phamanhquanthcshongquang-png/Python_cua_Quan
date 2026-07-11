tong = 0
n = int(input())
for i in range(1,n):
    if n % i == 0:
        tong += i
if tong == n:
    print(n ,"la so hoan hao")
else:
    print(n ,"khong la so hoan hao")
