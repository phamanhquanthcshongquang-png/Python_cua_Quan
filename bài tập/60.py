n = int(input())
tsnt = []
i = 2
while len(tsnt) < n:
    snt = True 
    for a in range(2,i):
        if i % a == 0:
            snt = False
            break
    if snt == True:
        tsnt.append(i)
    i += 1
print(tsnt)
