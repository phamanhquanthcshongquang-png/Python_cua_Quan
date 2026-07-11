n = int(input())
tong = 0
while n > 1:
    tong += 1
    if n % 2 == 0:
        n //= 2
    else:
        n -= 1
print(tong)
    