dem = 0
tsnt =[]
for i in range(100,1000):
    snt = True
    for a in range(2,i):
        if i % a == 0:
            snt = False
    if snt == True:
        tsnt.append(i)
print(tsnt)
print(len(tsnt))