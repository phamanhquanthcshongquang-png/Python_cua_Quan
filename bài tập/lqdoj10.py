n ,m = map(int,input().split())
tong = 0
so = 0
thutu = 1
A =[]
danhsach = [int(x) for x in input().split()][:n]
for a in danhsach:
    tong += a
    sucmanh = a * thutu
    thutu += 1
    A.append(sucmanh)
conlai = m - tong
manhnhat = A.index(max(A)) + 1
if tong <= m:
    print("Yes")
    print(manhnhat)
    print(conlai)
else:
    print("No")
