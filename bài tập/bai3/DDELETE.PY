import math
with open("DDELETE.INP") as file:
    n = file.readline()
    a = list(map(int,file.readline().split()))
so_chan = []
so_le = []
for i in a:
    if i % 2 == 0:
        so_chan.append(i)
    if i % 2 == 1:
        so_le.append(i)
so_cach1 = len(so_le) * len(so_chan)
so_cach2 = math.comb(len(so_chan), 2) + math.comb(len(so_le), 2)
if len(so_le) % 2 == 1:
    output = so_cach1
else:
    output = so_cach2
with open("DDELETE.OUT", "w") as fileout:
    fileout.write(str(output))
