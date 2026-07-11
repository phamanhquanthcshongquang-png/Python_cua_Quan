n = int(input())
tsnt = []
for i in range(2,n):
    snt = True
    for a in range(2,i):
        if i % a == 0:
            snt = False
            break
    if snt == True:
        tsnt.append(i)
print(f"tất cả các sô nguyên tố nhỏ hơn {n} là:{tsnt}")