with open("BHHAO.INP") as file:
    n = file.readline()
    a = list(map(int,file.readline().split()))
A = []
for h in a:
    chu_so = list(map(int,str(h)))
    tong_chu_so = sum(chu_so)
    A.append(tong_chu_so)
so_hoan_hao = []
for i in A:
    tong_uoc = 0
    for uoc in range(1, i):
        if i % uoc == 0:
            tong_uoc += uoc
    if tong_uoc == i:
        so_hoan_hao.append(i)
output = str(len(so_hoan_hao))
print(output)
with open("BHHAO.OUT", "w") as file2:
    file2.write(output)