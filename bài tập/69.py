n = int(input())
le = 0
for i in range(n):
    a = int(input())
    if a % 2 == 1:
        le += a
print(f"tổng các số lẻ là:{le}")
