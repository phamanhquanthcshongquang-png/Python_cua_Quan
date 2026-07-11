dem = 0
n = int(input("nhập số vào đây"))
for i in range(1,n+1):
    if n % i == 0:
        dem += 1
if dem == 2:
    print(n ,"là số nguyên tố")
else:
    print(n ,"không là số nguyên tố")