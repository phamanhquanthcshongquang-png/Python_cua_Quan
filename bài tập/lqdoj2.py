n = int(input())
dem = 0
for i in range(19, n + 1):
    tong = 0 
    temp = i
    while temp > 0:
        tong += temp % 10
        temp //= 10
    if tong == 10:
        dem += 1
print(dem)