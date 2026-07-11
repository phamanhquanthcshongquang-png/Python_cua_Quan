def tinh_so_mu(a,n):
    ket_qua = 1
    for i in range(n):
        
        ket_qua = ket_qua * a
    return ket_qua
print(tinh_so_mu(2,3))