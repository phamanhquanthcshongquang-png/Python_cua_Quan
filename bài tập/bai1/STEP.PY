with open("STEP.INP") as file:
    n = int(file.readline())
    a = list(map(int,file.readline().split()))
step = []
for i in a:
    chu_so = list(map(int,str(i)))
    chu_so2 = sorted(chu_so)
    if chu_so == chu_so2:
        step.append(i)
with open("STEP.OUT", "w") as file2:
    data = file2.write(str(len(step)))