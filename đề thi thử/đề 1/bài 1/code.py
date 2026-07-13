with open('CDIV.INP','r') as file:
    lines = file.readlines()
    inp = lines[1].strip()
mang = list(map(int,inp.split()))
gtln = max(mang)
count = [0] * (gtln + 1)
for i in mang:
    count[i] += 1
for g in range(gtln, 0, -1):
    soboi = 0
    for sobo in range(g, gtln + 1, g):
        soboi += count[sobo]
        if soboi >= 2:
           with open('CDIV.OUT', 'w') as file2:
               data = file2.write(str(g))
           break
    if soboi >= 2:
        break
    
    
