n = int(input())
t = 0
for i in range(1,n + 1):
    a = int(input())
    snt = True
    for b in range(2,a):
        if a % b == 0:
            snt = False
    if snt == True and a > 1:
        t += 1
print(f"có {t} số nguyên tố")
