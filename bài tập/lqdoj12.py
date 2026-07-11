t, d = map(int,input().split())
tong = 0
for i in range(1,t + 1):
    if t < 6:
        tong += 6000
    if t >= 6:
        tong += 5000
if t >= 6:
    tong = tong + 5000
if d == 1:
    print(tong - 2000)
else:
    print(tong)