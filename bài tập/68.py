n = int(input())
A = 0
for i in range(1,n + 1):
    a = int(input())
    if a % 2 == 0:
        A += a
print(f"tổng các số chẵn là:{A}")
