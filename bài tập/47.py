
n = int(input())
for i in range(1,n):
    tong = 0
    for a in range(1,i):
        if i % a == 0:
            tong += a 
    if tong == i:
        print(i)