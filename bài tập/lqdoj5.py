n = int(input())
m = int(input())
k = int(input())
sovong = m // n
sodu = m % n
tong = 0
a = 0
if m <= n:
    for i in range(1,k + 1):
        tong += i
    print(tong % 2026)
elif m % n == 0:
    for i in range(1,sovong + 1):
        tong1 = 0
        for b in range(1 + a,k + a + 1):
            tong1 += b
        a += n
    print(tong1 % 2026)
