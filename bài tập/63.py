def tong_cac_chu_so(n):
    tong = 0
    goc_n = n
    while n > 0:
        chu_so_cuoi = n % 10
        tong += chu_so_cuoi
        n //= 10
    print(f"tổng các chữ số của {goc_n} = {tong}")
n = int(input())
(tong_cac_chu_so(n))