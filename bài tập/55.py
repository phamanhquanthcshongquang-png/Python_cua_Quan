def tinh_giai_thua(n):
    ket_qua = 1
    for i in range(1,n+1):
        ket_qua = ket_qua * i
    return(f" {n}! = {ket_qua}")
a = int(input())
print(tinh_giai_thua(a))