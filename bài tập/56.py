def tinh_to_hop(n,k):
    ket_qua1 = 1
    ket_qua2 = 1
    ket_qua3 = 1
    for i in range(1,n+1):
        ket_qua1 = ket_qua1 * i
    for a in range(1,k+1):
        ket_qua2 = ket_qua2 * a
    for b in range(1,n - k + 1):
        ket_qua3 = ket_qua3 * b
    return (ket_qua1 /(ket_qua2 * ket_qua3))
n = int(input())
k = int(input())
print(tinh_to_hop(n,k))
    