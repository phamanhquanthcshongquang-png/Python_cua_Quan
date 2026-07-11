#Nhập vào một số nguyên dương có 3 chữ số. Tính tổng các chữ số của số đó
n = int(input())
tong = 0
for i in range(3):
    a = n % 10
    n  = n // 10
    tong += a
print(tong)
    