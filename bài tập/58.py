a = int(input())
b = int(input())
uc = []
bc = []
for i in range(1,min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        uc.append(i)
print(max(uc))
for h in range(max(a,b),(a*b) + 1):
    if h % a == 0 and h % b == 0:
        bc.append(h)
print(min(bc))
