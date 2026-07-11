n = int(input())
A = []
tong = 0
while n > 0:
    a = n % 10
    n = n // 10
    if a == 2 or a == 3 or a == 5 or a == 7:
        tong += a
print(tong)



